#!/usr/bin/env python3

#section 
#Identifies which unique outliers island samples have in common

import sys

###
species1, ID1 = 'dhole', 'BeijingZooDhole'
species2, ID2 = 'dhole', 'SardinianDhole'
###



file1 = 'outliers.'+species1+'.'+ID1+'.txt'
file2 = 'outliers.'+species2+'.'+ID2+'.txt'
path1 = '/groups/hologenomics/juliej/data/'+species1+'/'+ID1+'/'+file1
path2 = '/groups/hologenomics/juliej/data/'+species2+'/'+ID2+'/'+file2
infile1 = open(path1, 'r')
infile2 = open(path2, 'r')
outfile = open('commonOutliers.'+ID1+'.'+ID2+'.txt', 'w')

list1 = []
list2 = []

# List 1
for line in infile1:
	gene = ''.join(line.split()[0])
	list1.append(gene)	
infile1.close()


#List 2
for line in infile2:
	gene = ''.join(line.split()[0])
	list2.append(gene)
infile2.close()


#Find common
common = list(set(list1).intersection(list2))
if len(common)==0:
	print('No common outliers')
else:
	print('#Common outliers:',len(common))
	for gene in common:
		outfile.write(gene+'\n')


outfile.close()
