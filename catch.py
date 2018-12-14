#!/user/bin/python

import activer
import commond

commondMana=None

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass
	return False

def getNum(n):
	num = None
	while num == None:
		inp = input(str(n))
		if is_number(inp):
			return float(inp)
		else:
			global commondMana
			act = commondMana.getActiver("-catch/-show")
			if act == None:
				print("输入错误参数，请重新输入!")
			else:
				num = act.getArg(str(inp))
				if num == None:
					pass
				else:
					return float(num)

def setGlobalMana(commond):
	global commondMana
	commondMana = commond

class catchActiver(activer.Activer):
	def __init__(self,event={},mask="",etype="",res=None,carchs={}):
		self.event = event
		self.mask = mask
		self.etype = etype
		self.res = res
		self.isTran = True
		self.catchs = carchs

	def setDataName(self):
		n = input("设置参数名称:")
		self.catchs[str(n)] = self.res
		print(" ")

	def showOne(self):
		n = input("参数名称:")
		found = False
		for name in self.catchs.keys():
			if n == name:
				print("内容:" + str(self.catchs[str(n)]))
				found = True
		if found == False:
			print("未记录该参数")
		print(" ")

	def addArg(self):
		n = input("设置参数名称:")
		isSecc = False;
		arg = 0
		while isSecc == False:
			arg = input("设置参数:")
			if is_number(arg):
				isSecc = True
			else:
				print("无效输入,请重新输入")
		self.catchs[str(n)] = float(arg)
		print(" ")

	def showAll(self):
		for f,s in self.catchs.items():
			print("参数" + str(f) + ":" + str(s))
		print(" ")

	def getArg(self,n):
		if n in self.catchs:
			return self.catchs[n]
		else:
			print("参数不存在！")
			return None
		return None

	def setEvent(self):
		self.etype = "-catch/-show"
		self.event["-catch"] = self.setDataName
		self.event["-show -one"] = self.showOne
		self.event["-show -all"] = self.showAll
		self.event["-add -arg"] = self.addArg

	def fireEvent(self):
		self.mask()