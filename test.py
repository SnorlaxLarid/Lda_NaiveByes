import jieba
import pandas as pd
import Lda
from gensim import corpora, models, similarities
import gensim
# strList = ['0.039*"裁判" + 0.026*"比赛" + 0.013*"中" + 0.012*"受贿" + 0.010*"布拉特" + 0.009*"被" + 0.009*"安排" + 0.009*"协会" + 0.007*"局长" + 0.006*"亚洲杯" + 0.006*"持续" + 0.006*"说" + 0.006*"澳大利亚" + 0.006*"球员" + 0.005*"亚足联" + 0.005*"队员" + 0.005*"网上" + 0.005*"承办" + 0.005*"发布" + 0.004*"前"'
#       , '0.026*"比赛" + 0.010*"球队" + 0.009*"中" + 0.009*"韩" + 0.008*"实力" + 0.008*"对手" + 0.008*"队" + 0.008*"名" + 0.007*"之内" + 0.007*"朱广沪" + 0.006*"队员" + 0.006*"一块" + 0.006*"赛事" + 0.006*"最终" + 0.006*"球员" + 0.006*"启动" + 0.005*"主场" + 0.005*"战胜" + 0.005*"补充" + 0.005*"平"'
#       ,'0.015*"联赛" + 0.015*"裁判" + 0.011*"中" + 0.011*"球队" + 0.010*"比赛" + 0.009*"支" + 0.007*"队伍" + 0.007*"国奥" + 0.006*"备战" + 0.006*"全运会" + 0.006*"情况" + 0.006*"中甲" + 0.006*"说" + 0.006*"目标" + 0.005*"冠军" + 0.005*"对抗" + 0.005*"组" + 0.005*"进展" + 0.005*"实力" + 0.005*"被"'
#         ]
#
# wordsProSet = []
# for str in strList:
#     word =  str.split("+")
#     wordsProSet.append(word)
#
# vocabSet = set([])
# vocalProList = []
#
#
# #对LDA结果集进行裁剪，得到各词与概率
# for wordPro in wordsProSet:
#     for word in wordPro:
#         vocalProList.append([word.split('*')[1].split('"')[1],word.split("*")[0]])
#
# #获取特征词空间
# for vocalPro in vocalProList:
#     vocabSet = vocabSet | set([vocalPro[0]])
#
# #set转换位list保证顺序
# vocabSet = list(vocabSet)
#
# #得到特征词对应的概率
# proList = [0] * len(vocabSet)
#
# for i in range(0,len(vocabSet)):
#     for vocalPro in vocalProList:
#         if(vocabSet[i] == vocalPro[0]):
#             proList[i] += float(vocalPro[1])
#
# print(vocalProList)
# print(vocabSet)
# print(proList)

def getFeature(strList):
    wordsProSet = []
    for str in strList:
        word = str.split("+")
        wordsProSet.append(word)

    vocabSet = set([])
    vocalProList = []

    # 对LDA结果集进行裁剪，得到各词与概率
    for wordPro in wordsProSet:
        for word in wordPro:
            vocalProList.append([word.split('*')[1].split('"')[1], word.split("*")[0]])

    # 获取特征词空间
    for vocalPro in vocalProList:
        vocabSet = vocabSet | set([vocalPro[0]])

    # set转换位list保证顺序
    vocabSet = list(vocabSet)

    # 得到特征词对应的概率
    proList = [0] * len(vocabSet)

    for i in range(0, len(vocabSet)):
        for vocalPro in vocalProList:
            if (vocabSet[i] == vocalPro[0]):
                proList[i] += float(vocalPro[1])
    return vocabSet,proList
    # print(strList)
    # print(vocabSet)
    # print(proList)
    #
    # t = 0.0
    # for pro in proList:
    #     t += pro
    #     pro = pro/20
    # print(len(proList))
    # print(t / 20)
    # print(proList)


dir = "C://Users//larid//Desktop//Study//NLP//语料//"
file_desc = "".join([dir,'test.csv'])
stop_words = "".join([dir,'car.txt'])

stopwords=pd.read_csv(stop_words,index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')
stopwords=stopwords['stopword'].values

# txtDir = "C://Users//larid//Desktop//Study//NLP//语料//八大类语料，各1500篇//教育//"
# filename = str(285940) + ".txt"
# file_desc = "".join([txtDir, filename])
# sentences = []
# with open(file_desc, 'r', encoding='utf-8') as filein:
#     for line in filein:
#         try:
#             segs = jieba.lcut(line)
#             segs = [v for v in segs if not str(v).isdigit()]  # 去数字
#             segs = list(filter(lambda x: x.strip(), segs))  # 去左右空格
#             segs = list(filter(lambda x: x not in stopwords, segs))  # 去掉停用词
#             sentences.append(segs)
#         except Exception:
#             print(line)
#             continue
# filein.close()
# print(sentences)
# lda,wordNum = Lda.getLda("sport_train_1000.csv",stopwords,20)
# print(wordNum)
# lda.save("sport.model")
#
# lda,wordNum = Lda.getLda("finance_train_1000.csv",stopwords,20)
# print(wordNum)
# lda.save("finance.model")

for i in range(0,5):
    i = i
print(i)