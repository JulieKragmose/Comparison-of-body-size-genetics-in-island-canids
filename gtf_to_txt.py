#!/usr/bin/env python3

#Section 3.1 in report
#Takes a gtf file and turns it to positions file for ANGSD input, while filtering out unsuccesfully mapped genes.

import sys
import re 

infile = open('canFam3.ncbiRefSeq.transcripts.gtf', 'r')
outfile = open('canFam3.ncbiRefSeq.transcripts.txt', 'w')

count = 0

for line in infile:
	chr = re.search(r'(chr(\d+|X|Y))', line)
	if chr is not None:
		count += 1
		pos = re.findall(r'\s+(\d+)', line)
		gene = re.search(r'gene_name\s*"(\S+)";', line)
		if gene is None:
			print('ERROR')
			print(pos[0]+'-'+pos[1])
			sys.exit()
			
		outfile.write(chr.group(0)+':'+pos[0]+'-'+pos[1]+'\t'+'#'+gene.group(1)+'\n')
		

print('Gene count:',count)
	

