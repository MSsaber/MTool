#!/user/bin/python

import activer
import commond
import json
import xml
import sys
import log

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

def mathInput(s):
	global commondMana
	act = commondMana.getActiver("-catch/-show")
	if act == None:
		print("指令库出错")
	else:
		if act.isLog:
			print(s,end="")
			res = input()
			act.stdout.writeFile(res)
			return res
		else:
			return input(s)

def getNum(n):
	num = None
	while num == None:
		inp = mathInput(str(n))
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
		self.args = []
		self.isLog = False
		self.stdout = None

	def setDataName(self):
		n = ""
		if len(self.args) == 0:
			n = input("设置参数名称:")
		else:
			n = self.args[0]
		self.catchs[str(n)] = self.res
		print(" ")

	def showOne(self):
		if len(self.args) == 0:
			n = input("参数名称:")
		else:
			n = self.args[0]
		found = False
		for name in self.catchs.keys():
			if n == name:
				print("内容:" + str(self.catchs[str(n)]))
				found = True
		if found == False:
			print("未记录该参数")
		print(" ")

	def addArg(self):
		if len(self.args) == 0:
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
		else:
			for arg in self.args:
				strs = arg.split("=")
				if len(strs)!=2 or is_number(str(strs[1])) == False:
					print("参数" + str(strs[0]) + "设置错误" )
				elif is_number(strs[1]):
					self.catchs[str(strs[0])] = float(strs[1])

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

	def showSome(self):
		if len(self.args) == 0:
			print("未设置查找参数")
		else:
			for arg in self.args:
				if self.catchs[arg] == None:
					print("参数" + str(arg) + "不存在")
				else:
					print("参数" + str(arg) + ":" + str(self.catchs[arg]))
		print("")

	def writeFile(self):
		if len(self.args) == 0:
			print("未输入文件名,无法保存计算结果")
		elif len(self.args) > 1:
			print("文件名过多,请确保只有一个有效文件名")
		else:
			filename = self.args[0]
			filename = filename + ".json"
			with open(filename,"w") as fobj:
				json.dump(self.catchs,fobj)
			print("数据保存成功")

	def readFiles(self):
		if len(self.args) == 0:
			print("未输入导入文件名")
		else:
			try:
				filename = self.args[0]
				filename = filename + ".json"
				with open(filename) as fobj:
					self.catchs = json.load(fobj)
			except FileNotFoundError:
				print("目标文件不存在")

	def outputLog(self):
		if self.isLog == False:
			self.stdout = log.Logger(self.args[0] + ".txt")
			sys.stdout = self.stdout 
			self.isLog = True

	def logOut(self):
		print("计算流程开始输出...")

	def isEvent(self,event):
		isEve = False
		for name in self.event.keys():
			if name in event:
				isEve = True
				args = event.split()
				for arg in args:
					if arg != name and arg not in name:
						self.args.append(arg)
				self.mask = self.event[name]
				return isEve
		return isEve

	def setEvent(self):
		self.etype = "-catch/-show"
		self.event["-catch"] = self.setDataName
		self.event["-show -o"] = self.showOne
		self.event["-show -all"] = self.showAll
		self.event["-add -arg"] = self.addArg
		self.event["-show -s"] = self.showSome
		self.event["-file -w"] = self.writeFile
		self.event["-file -r"] = self.readFiles
		self.event["-log"] = self.outputLog
		self.event["-log -out"] = self.logOut

	def fireEvent(self):
		self.mask()
		self.args = []