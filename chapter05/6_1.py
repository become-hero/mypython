class Dog:
    def eat(self):
        print("正在啃骨头")
    def drink(self):
        print("正在喝水")
    def run(self):
        print("正在跑")
print("----hello wangcai----")
wangcai=Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
print("----hello tuofu------")
tuofu=Dog()
tuofu.eat()
tuofu.drink()
tuofu.run()
print("--------对比两只狗的ID-------")
print("wangcai id is {}".format(id(wangcai)))
print("tuofu   id is {}".format(id(tuofu)))
