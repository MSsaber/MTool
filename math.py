#!/user/bin/python

import commond
import activer
import line
import area
import check
import xmap
import volume
import catch
import cal

ac = activer.Activer()
la = line.lineActiver()
aa = area.areaActiver()
c = check.checkActiver()
xm = xmap.mapActiver()
v = volume.volumeActiver()
ca = catch.catchActiver()
cal = cal.calActiver()

cm = commond.Commond()
done = False
cm.addActiver(ac)
cm.addActiver(la)
cm.addActiver(aa)
cm.addActiver(c)
cm.addActiver(xm)
cm.addActiver(v)
cm.addActiver(ca)
cm.addActiver(cal)

while done == False:
    args = input("等待命令:")
    cm.readArgs(args)
    cm.analysisArgs()
    done= cm.isCommond("quit")
    if done == True:
        quit()
    real = cm.checkCommond()
    if real == False:
        continue
    cmdStr = cm.getCommond()
    print("")
    cmdStr.rstrip()
    isDone = cm.doCommond(cmdStr.rstrip())
    cm.readCommond([])
    if isDone == False:
        print("无效命令!")
        print(" ")

print(" ")
print("计算结束")

