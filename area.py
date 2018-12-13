#!/user/bin/python
import math 
import activer

def TriangleArea(len1,len2,angle):
    rad = math.radians(angle)
    h = len1 * math.sin(rad)
    return h * len2 / 2

def RadArea(R):
    return math.pi * R * R

def QuadArea(cb,db,h):
    return (cb + db) * h / 2

def OvalArea(a,b):
    return math.pi * a * b

def Triangle():
    print("")
    print("三角形面积计算")
    len1 = input("请输入第一条斜边:")
    len2 = input("请输入第二条斜边:")
    angle = input("请输入夹角:")
    area = TriangleArea(float(len1),float(len2),float(angle))
    print("三角形面积:" + str(area))
    return area

def Rad():
    print("")
    print("圆面积计算")
    R = input("请输入半径:")
    area = RadArea(float(R))
    print("圆面积:" + str(area))
    return area

def Quad():
    print("")
    print("四边形面积计算")
    cb = input("请输入长边:")
    db = input("请输入短边:")
    h = input("请输入高:")
    area = QuadArea(float(cb),float(db),float(h))
    print("四边形面积:" + str(area))
    return area

def Oval():
    print("")
    print("椭圆面积计算")
    a = input("请输入长边a:")
    b = input("请输入短边b:")
    area = OvalArea(float(a),float(b))
    print("椭圆面积:" + str(area))
    return area


class areaActiver(activer.Activer):
    def __init__(self,event={},mask=""):
        self.event = event
        self.mask = mask

    def setEvent(self):
        self.event["-area -tri"] = "Triangle"
        self.event["-area -quad"] = "Quad"
        self.event["-area -rad"] = "Rad"
        self.event["-area -oval"] = "Oval"

    def fireEvent(self):
        if self.mask == "Triangle":
            Triangle()
        elif self.mask == "Quad":
            Quad()
        elif self.mask == "Rad":
            Rad()
        elif self.mask == "Oval":
            Oval()

