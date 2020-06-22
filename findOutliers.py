#!/usr/bin/env python3

#Section 3.1.2 in report
#Finds the genes above the outlier threshold


import sys
import numpy as np
import os


###
species = 'banksIsl'
ID = 'BanksIsland'
###


filename = 'het.'+species+'.'+ID+'.txt'
path = '/groups/hologenomics/juliej/data/'+species+'/'+ID+'/'+filename

infile = open(path, 'r')

#Get heterozygosities
hets = []
for line in infile:
	het = float(line.split()[4])
	hets.append(het)


#Find threshold
Q3, Q1 = np.percentile(hets, [99.9,0.1])
IQR = Q3 - Q1
threshold = Q3 + (IQR*1.5)


#Find outliers 
infile = open(path, 'r')		
outfile = open('outliers.'+species+'.'+ID+'.txt', 'w')																								#CHANGE

count = 0
for line in infile:
	tmp = line.split()
	het = float(tmp[4])
	if het >= threshold:
		outfile.write(line)
		count += 1
				
print('Threshold:',threshold)
print('#Outliers: ',count)

infile.close()
outfile.close()
