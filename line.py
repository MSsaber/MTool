#!/user/bin/python
import math
import activer
import catch

def line(len1,angle,t):
    rad = math.radians(angle)
    if t == 1:
        return math.sin(rad) * len1
    return math.cos(rad) * len1

class lineActiver(activer.Activer):
    def __init__(self,event={},mask="",etype="",res=None):
        self.event = event
        self.mask = mask
        self.etype = etype
        self.res = res
        self.isTran = False

    def setEvent(self):
        self.etype = "-line"
        self.event["-line"] = "line"

    def fireEvent(self):
        print("")
        print("计算线段正弦/余弦值")
        Len1 = catch.getNum("请输入斜边长:")
        angle = catch.getNum("请输入角度:")
        t = catch.getNum("计算1.正弦 2.余弦[输入序号]")
        self.res = line(float(Len1),float(angle),int(t))
        print("线段计算结果:" + str(self.res))
        print(" ")


