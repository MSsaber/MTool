#!/user/bin/python

class Activer():

    def __init__(self,event={},mask="",etype="",res=None):
        self.event = event
        self.mask = mask
        self.etype = etype
        self.res = res
        self.isTran = False

    def getEventType(self):
        return self.etype

    def getResult(self):
        return self.res

    def isTransfer(self):
        return self.isTran

    def setResult(self,res):
        self.res = res

    def setEvent(self):
        self.etype = ""
        self.event["empty"] = None

    def isEvent(self,event):
        for name in self.event.keys():
            if name == event:
                self.mask=self.event[event]
                return True
        self.mask=""
        return False

    def fireEvent(self):
        print("无效命令")
