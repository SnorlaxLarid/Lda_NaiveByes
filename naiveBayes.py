#引入库文件
import jieba
import pandas as pd
import gensim
import math


class Model:
    #从finance训练集中得到的特征词表集合
    vocalSet_finance = []
    #与vocalSet_finance各特征词对应的概率（没有除以主题数目）
    proList_finance = []
    vocalSet_sport = []
    proList_sport = []
    stopwords = []

    def initModel(self):
        # 设置文件路径
        dir = "C://Users//larid//Desktop//Study//NLP//语料//"
        file_desc = "".join([dir, 'test.csv'])
        stop_words = "".join([dir, 'car.txt'])


        # 定义停用词
        stopwords = pd.read_csv(stop_words, index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='utf-8')
        self.stopwords = stopwords['stopword'].values

        #储存要进行处理的各个主题的词汇概率形如'0.026*"比赛" + 0.010*"球队" + 0.009*"中....'
        strList_finance = []

        lda_finance = gensim.models.ldamodel.LdaModel.load("finance.model")
        for topic in lda_finance.print_topics(num_topics=20, num_words=500):
            # print(topic[1])
            strList_finance.append(topic[1])

        strList_sport = []
        lda_sport = gensim.models.ldamodel.LdaModel.load("sport.model")
        for topic in lda_sport.print_topics(num_topics=20, num_words=500):
            # print(topic[1])
            strList_sport.append(topic[1])

        self.vocalSet_finance, self.proList_finance = self.getFeature(strList_finance)
        self.vocalSet_sport, self.proList_sport = self.getFeature(strList_sport)

    def getFeature(self,strList):
        ###获取对应语料的特征词表与概率，返回vocalSet, proList
        ### strList：未作处理的lda各主题的词汇分布

        wordsProSet = []
        for str in strList:
            word = str.split("+")
            wordsProSet.append(word)

        vocalSet = set([])
        vocalProList = []

        # 对LDA结果集进行裁剪，得到各词与概率
        for wordPro in wordsProSet:
            for word in wordPro:
                vocalProList.append([word.split('*')[1].split('"')[1], word.split("*")[0]])

        # 获取特征词空间
        for vocalPro in vocalProList:
            vocalSet = vocalSet | set([vocalPro[0]])

        # set转换位list保证顺序
        vocalSet = list(vocalSet)

        # 得到特征词对应的概率
        proList = [0] * len(vocalSet)

        for i in range(0, len(vocalSet)):
            for vocalPro in vocalProList:
                if (vocalSet[i] == vocalPro[0]):
                    proList[i] += float(vocalPro[1])

        return vocalSet, proList


    def classfly(self,file_desc):
        ###对输入文档进行分类
        ### file_desc:待分类文档的绝对路径

        #储存待处理文档的分词结果
        sentences = []
        with open(file_desc, 'r', encoding='utf-8') as filein:
            for line in filein:
                try:
                    segs = jieba.lcut(line)
                    segs = [v for v in segs if not str(v).isdigit()]  # 去数字
                    segs = list(filter(lambda x: x.strip(), segs))  # 去左右空格
                    segs = list(filter(lambda x: x not in self.stopwords, segs))  # 去掉停用词
                    sentences.append(segs)
                except Exception:
                    print(line)
                    continue
        filein.close()
        # print(sentences)

        #文档分类为 体育 的概率
        document_sport = 0.0
        # 文档分类为 财经 的概率
        document_finance = 0.0

        # minPro_fin = 10/414171
        # minPro_spt = 10/337566

        #对于特征词汇表里没有的词，防止概率结果为0，设置一个极小的概率
        minPro_fin = 1 / 400000
        minPro_spt = 1 / 400000

        for segs in sentences:
            for word_unkonwn in segs:
                for i in range(0, len(self.vocalSet_sport)):
                    if (self.vocalSet_sport[i] == word_unkonwn):
                        if (self.proList_sport[i] != 0.0):
                            document_sport += math.log10(self.proList_sport[i] / 20)
                        else:
                            #lda结果精度不够，统一视为一种概
                            document_sport += math.log10(0.0005 / 20)
                        # print(self.vocalSet_sport[i])
                        # print(self.proList_sport[i])
                        break
                    if (i >= len(self.vocalSet_sport) - 1):
                        document_sport += math.log10(minPro_spt)
        # print("next")
        for segs in sentences:
            for word_unkonwn in segs:
                for i in range(0, len(self.vocalSet_finance)):
                    if (self.vocalSet_finance[i] == word_unkonwn):
                        if (self.proList_finance[i] != 0.0):
                            document_finance += math.log10(self.proList_finance[i] / 20)
                        else:
                            document_finance += math.log10(0.0005 / 20)
                        # print(self.vocalSet_finance[i])
                        # print(self.proList_finance[i])
                        break
                    if (i >= len(self.vocalSet_finance) - 1):
                        document_finance += math.log10(minPro_fin)
        # print(document_sport, document_finance)
        if (document_finance > document_sport):
            return ("fin")
        if (document_finance < document_sport):
            return ("spt")


    def useModel(self,docType,area):

        ###使用模型进行分类
        ###docType：待分类文档实际的种类
        ###area： 是在训练集中测试，还是测试集中

        txtDir = ""
        start = 0
        end = 0
        if (docType == "finance"):
            txtDir = "C://Users//larid//Desktop//Study//NLP//语料//八大类语料，各1500篇//财经//"
            if (area == "train"):
                start = 798977
                end = 799977
            elif (area == "test"):
                start = 799978
                end = 800476

        elif (docType == "sport"):
            txtDir = "C://Users//larid//Desktop//Study//NLP//语料//八大类语料，各1500篇//体育//"
            if (area == "train"):
                start = 0
                end = 1000
            elif (area == "test"):
                start = 1001
                end = 1499

        num_all = 0
        finance_num = 0
        sport_num = 0

        for i in range(start, end):
            filename = str(i) + ".txt"
            file_desc = "".join([txtDir, filename])
            result = self.classfly(file_desc)
            # print("Now:"+str(i))
            num_all += 1
            if(result == "spt"):
                sport_num +=1
            elif(result == "fin"):
                finance_num += 1
        return num_all,sport_num,finance_num









