import  naiveBayes

model = naiveBayes.Model()
try:
    model.initModel()
    print("Model completed")
    print("finance  训练集结果: 总数 判断为体育的数量  判断位财经的数目")
    print(model.useModel("finance","train"))
    print("finance 测试集结果：总数 判断为体育的数量  判断位财经的数目")
    print(model.useModel("finance","test"))

    print("sport  训练集结果:  总数 判断为体育的数量  判断位财经的数目")
    print(model.useModel("sport","train"))
    print("sport 测试集结果： 总数 判断为体育的数量  判断位财经的数目")
    print(model.useModel("sport","test"))

except Exception:
    print("something wrong")



