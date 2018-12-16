#!/user/bin/python

import sys
class Logger(object):
	def __init__(self, fileN="Default.log"):
		self.terminal = sys.stdout
		self.log = open(fileN, "w")

	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def writeFile(self,inpt):
		self.log.write(str(inpt) + "\r\n")

	def flush(self):
		print("",end="\r\n")
		pass

#sys.stdout = Logger("xx.txt")
#print("MathTool      数学工具库命令")