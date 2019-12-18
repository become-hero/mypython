class Dog:
    def __init__(self,name):
        self.name=name
        self.__age=1
    def __set_age(self,age):
        self.__age=age
    def set_info(self,name,age):
        if name!="":
            self.name=name
        if age>0 and age<=20:
            self.__set_age(age)
        else:
            print("年龄设置失败！")
    def get_info(self):
        print("name={},age={}".format(self.name,self.__age))
wangcai=Dog("wangcai")
wangcai.get_info()
print("我长大了")
wangcai.set_info("",10)
wangcai.get_info()
print("------------")
print("name={}age={}".format(wangcai.name,wangcai.__age))
