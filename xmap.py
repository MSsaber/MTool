#!/user/bin/python
import activer

def xmap():
    print("MathTool      数学工具库命令")
    print("命令格式:     math -commond")
    print("-line         计算线段的正弦或者余弦值")
    print("-area -tri    计算三角形面积")
    print("-area -quad   计算四边形面积")
    print("-area -rad    计算圆面积")
    print("-area -oval   计算椭圆面积")
    print("-v -b         计算棱台体积")
    print("-v -p -tri    计算三棱锥体积")
    print("-v -p -quad   计算四棱锥体积")
    print("-v -p -rad    计算圆锥体积")
    print("-v -p -oval   计算椭圆锥体积")
    print("-v -es        计算椭球体积")
    print("-check        计算两个数值之间的误差率")
    print("-map          查看所有命令")
    print("-quit         退出MathTool")
    print("直接输入quit  退出MathTool")
    print("")

class mapActiver(activer.Activer):
    def __init__(self,event={},mask=""):
        self.event = event
        self.mask = mask

    def setEvent(self):
        self.event["-map"] = "Map"
        self.event["-quit"] = "Quit"

    def fireEvent(self):
        if self.mask == "Map":
            xmap()
        elif self.mask == "Quit":
            quit()