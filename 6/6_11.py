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
        print("******Dog start*****")
    def hand(self):
        print("*******hand*********")

class GoldenDog(Dog):
    def guide(self):
        print("++++++++++guide+++++++++++")
duoduo=GoldenDog()
duoduo.guide()
#
wangcai=Dog()
wangcai.hand()
