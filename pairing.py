#!/usr/bin/env python3

#Section 3.1.4 in report
#Creates every possible unique pair within island and mainland samples separately, as well as pairing the islands with the mainlands.

import sys
from itertools import combinations


samples = [	['baffinIsl', 'NorthBaffin'], ['baffinIsl', 'SouthBaffin'],
			['banksIsl', 'BanksIsland'],
			['dhole', 'SardinianDhole'], ['dhole', 'BeijingZooDhole'], ['dhole', 'BerlinZoo'],
			['indianWolf', 'ID165'], ['indianWolf', 'IndiaWolf'],
			['japaneseWolf', 'Honshu'],
			['mongolianWolf', 'InnerMongoliaWolf'],
			['oldDog', 'CGG6'],
			['PW', 'CGG23'], ['PW', 'CGG28'], ['PW','CGG29'], ['PW','CGG32'], ['PW', 'CGG33'],
			['victoriaIsl', 'VictoriaIsland']
			]
			
island = [	['baffinIsl', 'NorthBaffin'], ['baffinIsl', 'SouthBaffin'],
			['banksIsl', 'BanksIsland'],
			['dhole', 'SardinianDhole'],
			['japaneseWolf', 'Honshu'],
			['victoriaIsl', 'VictoriaIsland']
			]
			
			
mainland = [['dhole', 'BeijingZooDhole'], ['dhole', 'BerlinZoo'],
			['indianWolf', 'ID165'], ['indianWolf', 'IndiaWolf'],
			['mongolianWolf', 'InnerMongoliaWolf'],
			['oldDog', 'CGG6'],
			['PW', 'CGG23'], ['PW', 'CGG28'], ['PW','CGG29'], ['PW','CGG32'], ['PW', 'CGG33'],
			]
SD_JW =[['dhole', 'SardinianDhole'],
		['japaneseWolf', 'Honshu']
		]

PW_JW =[['PW', 'CGG23'], ['PW', 'CGG28'], ['PW','CGG29'], ['PW','CGG32'], ['PW', 'CGG33'],
		['japaneseWolf', 'Honshu']
		]
		
dholes = [['dhole', 'SardinianDhole'], ['dhole', 'BeijingZooDhole'], ['dhole', 'BerlinZoo']]
			


#Create all possible pair combinations within group
combos = []
[combos.append(pair) for pair in combinations(dholes, r=2)]

outfile = open('pairs.dholes.txt', 'w')
for pair in combos:
	species1 = pair[0][0]
	species2 = pair[1][0]
	ID1 = pair[0][1]
	ID2 = pair[1][1]
	outfile.write(species1+'\t'+ID1+'\t'+species2+'\t'+ID2+'\n')



#Create pairs between island and mainland
outfile = open('pairs.island_mainland.txt', 'w')
for x in island:
	for y in mainland:
		species1 = x[0]
		species2 = y[0]
		ID1 = x[1]
		ID2 = y[1]
		outfile.write(species1+'\t'+ID1+'\t'+species2+'\t'+ID2+'\n') 