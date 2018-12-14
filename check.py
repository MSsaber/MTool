#!/user/bin/python

import activer
import catch

def check():
    print(" ")
    num1 = catch.getNum("请输入第一个数据:")
    num2 = catch.getNum("请输入第二个数据:")
    wc = 1 - float(num1)/float(num2)
    print("误差:" + str(wc))
    return wc

class checkActiver(activer.Activer):
    def __init__(self,event={},mask="",etype="",res=None):
        self.event = event
        self.mask = mask
        self.etype = etype
        self.res = res
        self.isTran = False

    def setEvent(self):
        self.etype = "-check"
        global check
        self.event["-check"] = check

    def fireEvent(self):
        self.res = self.mask()

