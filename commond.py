#!/user/bin/python
import activer

class Commond():

    def __init__(self,Args = [],Commond = [],Activer = []):
        self.Args = Args
        self.Commond = Commond
        self.Activer = Activer

    def readCommond(self,Commond):
        self.Commond = Commond

    def readArgs(self,Args):
        self.Args = Args

    def analysisArgs(self):
            strCm = ""
            index = 1
            for arg in self.Args:

                if arg == " " and strCm != "":
                    self.Commond.append(strCm)
                    strCm = ""
                elif index == len(self.Args):
                    strCm += arg
                    self.Commond.append(strCm)
                elif arg != " ":
                    strCm += arg

                index += 1
    
    def checkCommond(self):
        if self.Commond[0] != "math":
            print("无效命令")
            print('请以"math -commond... 格式输入命令"')
            return False
        return True

    def isCommond(self,p):
        for arg in self.Commond:
            if arg == p:
                return True
        return False

    def getCommond(self):
        index = 0
        cmd = ""
        for arg in self.Commond:
            if index != 0:
                cmd = cmd + arg +" "
            index += 1
        return cmd

    def doCommond(self,p):
        for activer in self.Activer:
            if activer.isEvent(p):
                activer.fireEvent()

    def addActivers(self,cmds):
        for cmd in cmds:
            cmd.setEvent()
            self.Activer.append(cmd)

    def addActiver(self,cmd):
        cmd.setEvent()
        self.Activer.append(cmd)

    def showCm(self):
        print(self.Commond)

    def showArgs(self):
        print(self.Args)
