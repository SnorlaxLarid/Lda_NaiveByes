# Lda_NaiveByes
[语料来源](https://github.com/CallMeJiaGu/WordSimilarityAnalogyData)<br />  

对NLP挺感兴趣，寒假折腾了一会...

核心思路是把分类之后的结果分为几类；
1. LDA（Latent Dirichlet Allocation）模型可提取出来的且精度可以识别出来的
2. LDA模型可提取出来的但精度不够
3. LDA未提取到，没有出现在特征词表中
4. 对文本的内容毫无帮助的，比如标点符号和部分虚词

第二类和第三类的词的概率该项目中都同时粗略地用了一种概率值，同时假设了LDA个各主题等概率

gensim的api看了半天我也没找到可以返回主题概率分布的函数还有模型初始化时使各词概率精度更高的参数...不过结果到还是可以，可能我参数设置的运气还行吧

Result：

  训练集中：
  
         分类为财经：TP = 991; FN = 9;        分类为体育：TP = 996; FN = 4;
                    FP = 4;   TN = 996;                 FP = 9;   TN = 991;
                    accuracy = 99.35%;                  accuracy = 99.35%;
                    recall = 99.10%;                     recall = 99.60%;
                    F1 = 99.22%;                         F1 = 99.47%;
                    
  测试集中：
  
         分类为财经：TP = 487; FN = 11;        分类为体育：TP = 493; FN = 5;
                    FP = 5;   TN = 493;                  FP = 11;   TN = 487;
                    accuracy = 98.39%;                   accuracy = 98.39%;
                    recall = 97.79%;                     recall = 99.00%;
                    F1 = 98.09%;                         F1 = 98.69%;             


