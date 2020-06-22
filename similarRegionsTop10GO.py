#!/usr/bin/env python3

#Section 3.2.4 in report
#Finds the top10 GO terms with highest empirical pvalue found in the similar regions between Honshu and Pleistocene wolf. 

################################################################################
#GOterms 
GOterms = {}
infile = open('/groups/hologenomics/juliej/data/inrich/targetGeneList.txt', 'r')
for line in infile:
	line = line.split('\t')
	GO = line[1]
	description = line[2][:-1]
	GOterms[GO] = description
infile.close()

################################################################################

infile = open('similarRegions_strict.out.inrich', 'r')

GOdict = {}
flag = False
for line in infile:
	line = line.split()

	#Get GOs
	if 'Target_P_Threshold' in line:
		flag = False
	if flag is True and len(line)>1:
		GO = line[4]
		pvalue = line[2]
		GOdict[GO] = pvalue
	if 'T_Size' in line:
		flag = True	
infile.close()
	

sort_orders = sorted(GOdict.items(), key=lambda x: x[1], reverse=True)
outfile = open('/groups/hologenomics/juliej/data/inrich/similarRegions/SR.Top10GO.txt', 'w')
count = 0
for i in sort_orders:
	count += 1
	if count <= 10:
		outfile.write(i[0]+'\t'+str(i[1])+'\t'+GOterms[i[0]]+'\n')
outfile.close()