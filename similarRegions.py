#!/usr/bin/env python3

#section 3.2.3
#Compares similar regions identified in Honshu, IndiaWolf and ID165 to find the regions uniquely similar between Honshu and Pleistocene wolf

import sys

#GET DATA

#PLEISTOCENE AND JAPANESE WOLVES
PW_Honshu_regions = []
infile = open('/groups/hologenomics/juliej/data/MUMmer/PW.joined_japaneseWolf.Honshu.tab', 'r')

for line in infile:
	line = line.split()
	PWstart = line[0]
	PWend = line[1]
	chromosome = line[7]
	PW_Honshu_regions.append([PWstart,PWend,chromosome])
infile.close()


#MONGOLIAN WOLF
infile = open('/groups/hologenomics/juliej/data/MUMmer/PW.joined_mongolianWolf.InnerMongoliaWolf.tab', 'r')
pos_list = []
mongolian_list = []
	
for line in infile:
	line=line.split()
	start = line[0]
	end = line[1]
	chromosome = line[7]
	mongolian_list.append([start,end,chromosome])	
infile.close()


#INDIAN WOLVES
wolves = ['indianWolf.IndiaWolf', 'mongolianWolf.InnerMongoliaWolf']
indian_list = []

for wolf in wolves:
	infile = open('/groups/hologenomics/juliej/data/MUMmer/PW.joined_'+wolf+'.tab', 'r')
	pos_list = []	
	for line in infile:
		line=line.split()
		start = line[0]
		end = line[1]
		chromosome = line[7]
		pos_list.append([start,end,chromosome])		
	indian_list.append(pos_list)
infile.close()

#-------------------------------------------------------------------------------
#COMPARE TO MONGOLIAN

notUnique_loose = []
notUnique_strict = []

for PWregion in PW_Honshu_regions:
	PWstart = int(PWregion[0])
	PWend = int(PWregion[1])
	PWchr = PWregion[2]
	
	for region in mongolian_list:
		mongolianStart = int(region[0])	
		mongolianEnd = int(region[1])
		mongolianChr = region[2]
		
		#Check if the regions can be considered the same
		startDiff = PWstart - mongolianStart
		endDiff = PWend - mongolianEnd
		
		#If region found in mongolianWolf it is not considered unique
		if -100 < startDiff < 100 and  -100 < endDiff < 100 and mongolianChr==PWchr:
			notUnique_loose.append(PWregion)

			#STRICTER TEST
			check = 0
			for indianWolf in indian_list:
				for indianRegion in indianWolf:
					indianStart = int(indianRegion[0])
					indianEnd = int(indianRegion[1])
					indianChr = indianRegion[2]
					
					startDiff = PWstart - indianStart
					endDiff = PWend - indianEnd
					if -100 < startDiff < 100 and  -100 < endDiff < 100 and indianChr==PWchr:
						check += 1
					
			if check == 2:
				notUnique_strict.append(PWregion)
						
print('Loose:',notUnique_loose)
print('Strict:',notUnique_strict)

"""
notUnique = []
for wolfRegion in comparison_list:
	
	for PWregion in PW_Honshu_regions:
		PWstart = int(PWregion[0])
		PWend = int(PWregion[1])
		PWchr = PWregion[2]
		
		for comparisonRegion in wolfRegion:
			comparisonStart = int(comparisonRegion[0])	
			comparisonEnd = int(comparisonRegion[1])
			comparisonChr = comparisonRegion[2]
			
			#Check if the regions can be considered the same
			startDiff = PWstart - comparisonStart
			endDiff = PWend - comparisonEnd

			#Region found in other wolf than the Japanese wolf, means it is not unique
			if -100 < startDiff < 100 and  -100 < endDiff < 100 and comparisonChr==PWchr:
				notUnique.append(PWregion)

			
print('Not unique:', len(notUnique))
"""

#IDENTIFY UNIQUE REGIONS

unique_loose = []
unique_strict = []
for region in PW_Honshu_regions:
	if region not in notUnique_loose:
		unique_loose.append(region)
	if region not in notUnique_strict:
		unique_strict.append(region)
		
print('Regions:',len(PW_Honshu_regions))
print('Loose:', len(unique_loose))
print('Strict:', len(unique_strict))


#-------------------------------------------------------------------------------
#PRINT RESULTS

outfile = open('uniqueRegions_loose.txt', 'w')
for region in unique_loose:
	start = region[0]
	end = region[1]
	chromosome = region[2]
	outfile.write(chromosome+'\t'+start+'\t'+end+'\n')
outfile.close()

outfile = open('uniqueRegions_strict.txt', 'w')
for region in unique_strict:
	start = region[0]
	end = region[1]
	chromosome = region[2]
	outfile.write(chromosome+'\t'+start+'\t'+end+'\n')
outfile.close()