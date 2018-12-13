#!/user/bin/python

import area
import activer
import math

def Bridge(s1,s2,h):
    return 1/3 * h * (s1 + s2 + math.sqrt(s1*s1))

def Pyramid(s,h):
    return 1/3 * h * s

def Ellipsoid():
    print("")
    a = input("请输入椭球a:")
    b = input("请输入椭球b:")
    c = input("请输入椭球c:")
    return 4/3 * math.pi * float(a) * float(b) * float(c)

def OutVolume(t,v):
    print(" ")
    print(t + "体积:" + str(v))


class volumeActiver(activer.Activer):
    def __init__(self,event={},mask=""):
        self.event = event
        self.mask = mask

    def setEvent(self):
        self.event["-v -b"] = "Bridge"
        self.event["-v -p -tri"] = "Ptri"
        self.event["-v -p -quad"] = "Pquad"
        self.event["-v -p -rad"] = "Prad"
        self.event["-v -p -oval"] = "Poval"
        self.event["-v -es"] = "Es"
        
    def fireEvent(self):
        if self.mask == "Bridge":
            s1 = area.Quad()
            s2 = area.Quad()
            h = input("请输入棱台高度:")
            OutVolume("棱台",Bridge(s1,s2,float(h)))
        elif self.mask == "Ptri":   
            s = area.Triangle()
            h = input("请输入三棱锥高度:")
            OutVolume("三棱锥",Pyramid(s,float(h)))
        elif self.mask == "Pquad":
            s = area.Quad()
            h = input("请输入四棱锥高度:")
            OutVolume("四棱锥",Pyramid(s,float(h)))
        elif self.mask == "Prad":
            s = area.Rad()
            h = input("请输入圆锥高度:")
            OutVolume("圆锥",Pyramid(s,float(h)))
        elif self.mask == "Poval":
            s = area.Oval()
            h = input("请输入椭圆锥高度:")
            OutVolume("椭圆锥",Pyramid(s,float(h)))
        elif self.mask == "Es":
            OutVolume("椭球",Ellipsoid())




