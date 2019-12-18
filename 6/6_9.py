class Animal:
    def eat(self):
        print("----eat----")
    def drink(self):
        print("----drink----")
    def run(self):
        print("----run----")
class Dog(Animal):
    def hand(self):
        print("******hand*******")
class GoldenDog(Dog):
    def guide(self):
        print("+++++++I can guide+++++")
wangcai=Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.hand()
print("------------------------------")
duoduo=GoldenDog()
duoduo.guide()
duoduo.hand()
duoduo.eat()
