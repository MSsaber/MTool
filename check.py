#!/user/bin/python

import activer

def check():
    print(" ")
    num1 = input("请输入第一个数据:")
    num2 = input("请输入第二个数据:")
    wc = 1 - float(num1)/float(num2)
    print("误差:" + str(wc))

class checkActiver(activer.Activer):
    def __init__(self,event={},mask=""):
        self.event = event
        self.mask = mask

    def setEvent(self):
        self.event["-check"] = "Check"

    def fireEvent(self):
        check()

