class Dog:
    def __init__(self,variety,gender):
        print("开始初始化")
        self.variety=variety
        self.gender=gender
        print("初始化结束")
wangcai=Dog("金毛","雄性")
print("wangcai的品种：{}".format(wangcai.variety))
print("wangcai的性别：{}".format(wangcai.gender))
wangcai.name="wangcai"
wangcai.age=1
print("name ={},age={}".format(wangcai.name,wangcai.age))
