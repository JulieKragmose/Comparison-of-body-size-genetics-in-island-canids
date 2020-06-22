#!/usr/bin/env python3

#Section 3.2.4
#Finds top10 most enriched GO terms found in runs of homozygosity in Honshu, and compares to Mongolian- and Pleistocene wolf.

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

island = [['japaneseWolf', 'Honshu']]
			
			
wolfMainland = [['mongolianWolf', 'InnerMongoliaWolf'],
			['PW', 'CGG23'], ['PW', 'CGG28'], ['PW','CGG29'], ['PW','CGG32'], ['PW', 'CGG33'],]
			

wolfMainlandSet = set()
for sample in wolfMainland:
	ID = sample[1]
	infile = open(ID+'.RoH.out.inrich', 'r')
	flag = False
	
	for line in infile:
		line = line.split()
	
		#Get GOs
		if 'Target_P_Threshold' in line:
			flag = False
		if flag is True and len(line)>1:
			GO = line[4]
			pvalue = line[2]
			wolfMainlandSet.add(GO)
		if 'T_Size' in line:
			flag = True	
	infile.close()

islandDict = {}
for sample in island:
	ID = sample[1]
	infile = open(ID+'.RoH.out.inrich', 'r')
	flag = False 
	
	for line in infile:
		line = line.split()
	
		#Get GOs
		if 'Target_P_Threshold' in line:
			flag = False
		if flag is True and len(line)>1:
			GO = line[4]
			pvalue = line[2]
			islandDict[GO] = pvalue
		if 'T_Size' in line:
			flag = True	
	infile.close()
	
################################################################################
#Print output
	sort_orders = sorted(islandDict.items(), key=lambda x: x[1], reverse=True)
	outfile = open('/groups/hologenomics/juliej/data/inrich/RoH/'+ID+'.RoH.Top10.txt', 'w')
	count = 0
	for i in sort_orders:
		count += 1
		if count <= 10:
			if i[0] in wolfMainlandSet:
				outfile.write(i[0]+'\t'+str(i[1])+'\t Unique \t'+GOterms[i[0]]+'\n')
			else:
				outfile.write(i[0]+'\t'+str(i[1])+'\t Not unique \t'+GOterms[i[0]]+'\n')
	outfile.close()