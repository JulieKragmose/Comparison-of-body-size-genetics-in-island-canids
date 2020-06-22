#!/usr/bin/env python3

#Section 3.2.4
#Finds top10 most enriched GO terms in windows with extreme heterozygosity and compares to mainland samples

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


island = [	['dhole', 'SardinianDhole'],
			['japaneseWolf', 'Honshu']
			]
			
			
wolfMainland = [['mongolianWolf', 'InnerMongoliaWolf'],
			['PW', 'CGG23'], ['PW', 'CGG28'], ['PW','CGG29'], ['PW','CGG32'], ['PW', 'CGG33'],]

dholeMainland = [['dhole', 'BeijingZooDhole'], ['dhole', 'BerlinZoo']]

#Wolves
wolfMainlandSet = set()
for sample in wolfMainland:
	ID = sample[1]
	highInfile = open(ID+'.top200.highest.sw.out.inrich', 'r')
	lowInfile = open(ID+'.top200.lowest.sw.out.inrich', 'r')
	flag = False
	
	for line in highInfile:
		line = line.split()
	
		#Get GOs
		if 'Target_P_Threshold' in line:
			flag = False
		if flag is True and len(line)>1:
			GO = line[4]
			wolfMainlandSet.add(GO)
		if 'T_Size' in line:
			flag = True	
	highInfile.close()
	
	for line in lowInfile:
		line = line.split()
	
		#Get GOs
		if 'Target_P_Threshold' in line:
			flag = False
		if flag is True and len(line)>1:
			GO = line[4]
			wolfMainlandSet.add(GO)
		if 'T_Size' in line:
			flag = True	
	lowInfile.close()

#Dholes
dholeMainlandSet = set()
for sample in dholeMainland:
	ID = sample[1]
	highInfile = open(ID+'.top200.highest.sw.out.inrich', 'r')
	lowInfile = open(ID+'.top200.lowest.sw.out.inrich', 'r')
	flag = False
	
	for line in highInfile:
		line = line.split()
	
		#Get GOs
		if 'Target_P_Threshold' in line:
			flag = False
		if flag is True and len(line)>1:
			GO = line[4]
			dholeMainlandSet.add(GO)
		if 'T_Size' in line:
			flag = True	
	highInfile.close()
	
	for line in lowInfile:
		line = line.split()
	
		#Get GOs
		if 'Target_P_Threshold' in line:
			flag = False
		if flag is True and len(line)>1:
			GO = line[4]
			dholeMainlandSet.add(GO)
		if 'T_Size' in line:
			flag = True	
	lowInfile.close()


################################################################################

for sample in island:
	ID = sample[1]
	highInfile = open(ID+'.top200.highest.sw.out.inrich', 'r')
	lowInfile = open(ID+'.top200.lowest.sw.out.inrich', 'r')
	flag = False 
	
	highDict = {}
	for line in highInfile:
		line = line.split()
	
		#Get GOs
		if 'Target_P_Threshold' in line:
			flag = False
		if flag is True and len(line)>1:
			GO = line[4]
			pvalue = line[2]
			highDict[GO] = pvalue
		if 'T_Size' in line:
			flag = True	
	highInfile.close()
	
	lowDict = {}
	flag = False
	for line in lowInfile:
		line = line.split()
	
		#Get GOs
		if 'Target_P_Threshold' in line:
			flag = False
		if flag is True and len(line)>1:
			GO = line[4]
			pvalue = line[2]
			lowDict[GO] = pvalue
		if 'T_Size' in line:
			flag = True	
	lowInfile.close()

#Print results
	sort_orders = sorted(highDict.items(), key=lambda x: x[1], reverse=True)
	outfile = open('/groups/hologenomics/juliej/data/inrich/slidingWindow/SW.top10.'+ID+'.highest.txt', 'w')
	count = 0
	for i in sort_orders:
		count += 1
		if count <= 10:
			if (ID=='SardinianDhole' and i[0] in dholeMainlandSet) or (ID=='Honshu' and i[0] in wolfMainlandSet):
				outfile.write(i[0]+'\t'+str(i[1])+'\t Unique \t'+GOterms[i[0]]+'\n')
			else:
				outfile.write(i[0]+'\t'+str(i[1])+'\t Not unique \t'+GOterms[i[0]]+'\n')
	outfile.close()
	
	sort_orders = sorted(lowDict.items(), key=lambda x: x[1], reverse=True)
	outfile = open('/groups/hologenomics/juliej/data/inrich/slidingWindow/SW.top10.'+ID+'.lowest.txt', 'w')
	count = 0
	for i in sort_orders:
		count += 1
		if count <= 10:
			if (ID=='SardinianDhole' and i[0] in dholeMainlandSet) or (ID=='Honshu' and i[0] in wolfMainlandSet):
				outfile.write(i[0]+'\t'+str(i[1])+'\t Unique \t'+GOterms[i[0]]+'\n')
			else:
				outfile.write(i[0]+'\t'+str(i[1])+'\t Not unique \t'+GOterms[i[0]]+'\n')
	outfile.close()

################################################################################	
	