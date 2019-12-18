class Animal:
    def __init__(self):
        print("-----Animal初始化------")
    def eat(self):
        print("-----eat------")
    def drink(self):
        print("-----drink-----")
    def run(self):
        print("-----run--------")
class Dog(Animal):
    def __init__(self,name):
        self.name=name
        print("My name is {}".format(self.name))
    def run(self):
        print("要着尾巴跑!")
class Cat(Animal):
    def __init__(self,name):
        self.name=name
        print("My name is {}".format(self.name))
animal=Animal()
animal.run()

wangcai=Dog("wangcai")
wangcai.run()

tom=Cat("Tom")
tom.run()
