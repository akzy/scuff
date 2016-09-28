# -*- coding: utf-8 -*-
"""
Created on Tue May 24 21:14:11 2016
/Converts the output (input.csv) from the compute.sh into output.csv for paraview and RF.dat for Mathemtica. mage units of V/mm and magh units of H/mm
@author: agrin
"""

import csv
import math

with open('input.csv', 'rb') as csvfile:
  infile = csv.reader(csvfile, delimiter=' ')
  data = list(infile)
csvfile.close()
    
outdata = [] 
for row in data:
    x = abs(complex(float(row[3]),float(row[4])))
    y = abs(complex(float(row[5]),float(row[6])))
    z = abs(complex(float(row[7]),float(row[8])))
    mage = math.sqrt((x*x)+(y*y)+(z*z))/4
    x = abs(complex(float(row[9]),float(row[10])))
    y = abs(complex(float(row[11]),float(row[12])))
    z = abs(complex(float(row[13]),float(row[14])))
    magh = math.sqrt((x*x)+(y*y)+(z*z))/4
    outdata.append([row[0],row[1],row[2],mage,magh])
    
with open("output.csv", "wb") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(outdata)
csvfile.close()

with open("RF.dat", "wb") as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerows(outdata)
csvfile.close()
