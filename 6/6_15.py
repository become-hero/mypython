class AI:
    def face_re(self):
        print("---人脸识别----")
    def hand(self):
        print("aaaaaaaaaaaai")
class BigDate:
    def date_an(self):
        print("----数据分析-----")
    def hand(self):
        print("Bbbbbbbbbbbbd")
class All(AI,BigDate):
    def operation(self):
        print("+++运维+++")
py=All()
print(All.__mro__)
py.hand()

#py.date_an()
#py.face_re()
#py.operation()
