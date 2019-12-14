def robot(func):
    def say():
        print("can i help you")
        func()
        print("Pls input num {1|2|3|4}")
        score=input()
    return say

def contact():
    q=input("wen:")
    print("sorry!{}".format(q))
    return

func_closure=robot(contact)
func_closure()
