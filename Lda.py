#引入库文件
import jieba.analyse as analyse
import jieba
import pandas as pd
from gensim import corpora, models, similarities
import gensim
import numpy as np
import matplotlib.pyplot as plt


def getLda(filename,stopwords,numTopics):
    ###用来获得lda模型，返回lda以及去掉停用词的总词语数wordNum
    ###filename: csv语料文件的绝对路径
    ###stopwords：对应的停用词文件
    ###numTopics：生成的LDA模型的主题个数

    df = pd.read_csv(filename, encoding='UTF-8')
    # 删除Nan行
    df.dropna(inplace=True)
    lines = df.content.values.tolist()
    # 开始分词
    sentences = []
    wordNum = 0
    for line in lines:
        try:
            segs = jieba.lcut(line)
            segs = [v for v in segs if not str(v).isdigit()]  # 去数字
            segs = list(filter(lambda x: x.strip(), segs))  # 去左右空格
            segs = list(filter(lambda x: x not in stopwords, segs))  # 去掉停用词
            wordNum += len(segs)
            sentences.append(segs)
        except Exception:
            print(line)
            continue
    # print(sentences)
    # 构建词袋模型
    dictionary = corpora.Dictionary(sentences)
    corpus = [dictionary.doc2bow(sentence) for sentence in sentences]
    # lda模型，num_topics是主题的个数，这里定义了5个
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=numTopics)
    return lda,wordNum

def saveLda(lda,modelname):
    lda.save(modelname)




