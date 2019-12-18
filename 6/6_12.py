class Animal:                                                                   
    def __init__(self):
        print("*****start********")
    def eat(self):
        print("--------eat------")
    def drink(self):
        print("-------drink------")
    def run(self):
        print("-------run---------")

class Dog(Animal):
    def __init__(self):
        print("*****Dog 初始化*****")
    def hand(self):
        print("*****握手*****")
class GoldenDog(Dog):
    def guide(self):
        print(">>>>我能导航<<<<")
        print("提示想让我导航，请先跟我握手！")
       # Dog.hand(self)
        super().hand()
duoduo=GoldenDog()
duoduo.guide()
