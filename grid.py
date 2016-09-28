# -*- coding: utf-8 -*-
"""
Spyder Editor
/Creates the multiple .epfiles depending on the grid size you want. Pointcounter at 40,000 for 64GB systems. Adjust as needed. Units of mm
This is a temporary script file.
"""
import numpy as np
import os as os

xmin = 0
xmax = 1
ymin = 0
ymax = 0.61
zmin = 0.050
zmax = 0.300
stepxy = 0.0025
stepz = 0.005
pointcounter = 0
filecounter = 0

tmp = []
nx=0
ny=0
nz=0
for x in np.arange(xmin,xmax,stepxy):
  nx+=1
  for y in np.arange(ymin,ymax,stepxy):
    ny+=1
    for z in np.arange(zmin,zmax,stepz):
      nz+=1
      tmp.append(str(x) + ' ' + str(y) + ' ' + str(z) + '\n')

print(str(nx) + " " + str(ny/nx) + " " + str(nz/ny))

print(len(tmp))
     

fout = open("trap.epfile0","wb")
for line in tmp:
  fout.write(line)
  pointcounter+=1
  if pointcounter%700000 == 0:
    fout.close()
    filecounter+=1
    fout = open("trap.epfile%d"%(filecounter),"wb")

fout.close()  
 


