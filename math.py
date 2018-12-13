#!/user/bin/python

import commond
import activer
import line
import area
import check
import xmap
import volume

ac = activer.Activer()
la = line.lineActiver()
aa = area.areaActiver()
c = check.checkActiver()
xm = xmap.mapActiver()
v = volume.volumeActiver()

cm = commond.Commond()
done = False
cm.addActiver(ac)
cm.addActiver(la)
cm.addActiver(aa)
cm.addActiver(c)
cm.addActiver(xm)
cm.addActiver(v)

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
    cm.doCommond(cmdStr.rstrip())
    cm.readCommond([])

print(" ")
print("计算结束")
cm.doCommond("-area -tri")
cm.doCommond("-area -quad")
cm.doCommond("-area -rad")
