#!/user/bin/python

class Activer():

    def __init__(self,event={},mask=""):
        self.event = event
        self.mask = mask

    def setEvent(self):
        self.event["empty"] = "none"

    def isEvent(self,event):
        for name in self.event.keys():
            if name == event:
                self.mask=self.event[event]
                return True
        self.mask=""
        return False

    def fireEvent(self):
        print("无效命令")
