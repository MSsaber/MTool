#!/user/bin/python

import catch
import activer

class calActiver(activer.Activer):
	def __init__(self,event={},mask="",etype="",res=None):
		self.event = event
		self.mask = mask
		self.etype = etype
		self.res = res
		self.isTran = False

	def plus(self):
		num1 = catch.getNum("请输入第一个数:")
		num2 = catch.getNum("请输入第二个数:")
		res = float(num1) + float(num2)
		print("和为:" + str(res))
		print(" ")
		return res

	def sub(self):
		num1 = catch.getNum("请输入被减数:")
		num2 = catch.getNum("请输入减数:")
		res = float(num1) - float(num2)
		print("差为:" + str(res))
		print(" ")
		return res

	def multi(self):
		num1 = catch.getNum("请输入第一个数")
		num2 = catch.getNum("请输入第二个数")
		res = float(num1) * float(num2)
		print("积为:" + str(res))
		print(" ")
		return res

	def divide(self):
		num1 = catch.getNum("请输入被除数")
		num2 = catch.getNum("请输入除数")
		res = float(num1) / float(num2)
		print("余为:" + str(res))
		print(" ")
		return res

	def setEvent(self):
		self.etype = "-cal"
		self.event["-cal -p"] = self.plus
		self.event["-cal -s"] = self.sub
		self.event["-cal -m"] = self.multi
		self.event["-cal -d"] = self.divide

	def fireEvent(self):
		self.res = self.mask()
