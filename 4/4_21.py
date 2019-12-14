def robot(func):
    def say():
        print("can i help you")
        func()
        print("Pls input num {1|2|3|4}")
        score=input()
        print("thank you")
        return
    return say

@robot
def contact():
        q=input("wen:")
        print("sorry!{}".format(q))
        return
contact()
