#!/user/bin/python
import activer

def xmap():
    print("MathTool        数学工具库命令")
    print("命令格式:        math -commond")
    print("-cal -p         求和")
    print("-cal -s         求差")
    print("-cal -m         求积")
    print("-cal -d         求余")
    print("-line           计算线段的正弦或者余弦值")
    print("-area -tri      计算三角形面积")
    print("-area -quad     计算四边形面积")
    print("-area -rad      计算圆面积")
    print("-area -oval     计算椭圆面积")
    print("-v -b           计算棱台体积")
    print("-v -b -ss       通过已知的台体上下面积计算棱台体积")
    print("-v -p -sh       通过已知的锥体底面积计算锥体体积")
    print("-v -p -tri      计算三棱锥体积")
    print("-v -p -quad     计算四棱锥体积")
    print("-v -p -rad      计算圆锥体积")
    print("-v -p -oval     计算椭圆锥体积")
    print("-v -es          计算椭球体积")
    print("-show -o        查看记录的某一个参数,-o后可接参数名称")
    print("-show -all      查看记录的所有参数")
    print("-show -s        查看记录的多个参数,-s后必须接参数名")
    print("-add -arg       输入一个参数并保存,若命令后接多个参数等式则可以一次性添加多个参数")
    print("-catch          抓取上一次计算结果")
    print("-check          计算两个数值之间的误差率")
    print("-file -w 文件名  将所有catch参数保存成文件")
    print("-file -r 文件名  读取参数文件并记录到参数库中")
    print("-log 文件名      将本次计算的所有流程全部保存到文件中,直到quit为止")
    print("-map             查看所有命令")
    print("-quit           退出MathTool")
    print("直接输入quit     退出MathTool")
    print("")

class mapActiver(activer.Activer):
    def __init__(self,event={},mask="",etype="",res=None):
        self.event = event
        self.mask = mask
        self.etype = etype
        self.res = res
        self.isTran = False

    def setEvent(self):
        self.event["-map"] = "Map"
        self.event["-quit"] = "Quit"

    def fireEvent(self):
        if self.mask == "Map":
            xmap()
        elif self.mask == "Quit":
            quit()
