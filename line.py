#!/user/bin/python
import math
import activer

def line(len1,angle,t):
    rad = math.radians(angle)
    if t == 1:
        return math.sin(rad) * len1
    return math.cos(rad) * len1

class lineActiver(activer.Activer):
    def __init__(self,event={},mask=""):
        self.event = event
        self.mask = mask

    def setEvent(self):
        self.event["-line"] = "line"

    def fireEvent(self):
        print("")
        print("计算线段正弦/余弦值")
        len1 = input("请输入斜边长:")
        angle = input("请输入角度:")
        t = input("计算1.正弦 2.余弦[输入序号]")
        print("线段计算结果:" + str(line(float(len1),float(angle),int(t))))


