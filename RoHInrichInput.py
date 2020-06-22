#!/usr/bin/env python3

#Section 3.2.2 in report
#Takes output file of PLINK with runs of homozygosities, turns it into a position file and runs INRICH

import sys
import os

#-------------------------------------------------------------------------------
#INPUT

if len(sys.argv) == 1:
	sys.stderr.write('No input arguments \n')
	sys.exit(1)	
elif len(sys.argv) == 3:
	species = sys.argv[1]
	ID = sys.argv[2]
	
infile = open('/groups/hologenomics/juliej/data/'+species+'/'+ID+'/plink.hom', 'r')
outfile = open('positions.RoH.'+species+'.'+ID+'.txt', 'w')


#-------------------------------------------------------------------------------
#MAKE POSITION FILE

for line in infile:
	line = line.split()
	FID = line[0]
	
	if FID == '0':
		chromosome = line[3]
		start = line[6]
		end = line[7]
		
		outfile.write(chromosome+'\t'+start+'\t'+end+'\n')

infile.close()
outfile.close()


#-------------------------------------------------------------------------------
#USE INRICH

os.system('module load htslib/v1.9 angsd/v0.929 samtools/v1.9 python/v3.6.9 java GATK/v4.1.2.0 plink/v1.90b3.42 perl/v5.28.1 MUMmer/v4.0.0beta2 bedtools/v2.29.0 inrich/v1.1')
os.system('xsbatch -c 1 -- inrich \
			-g /groups/hologenomics/juliej/data/inrich/refGeneFile.txt \
			-m /groups/hologenomics/juliej/data/inrich/snpList.txt \
			-t /groups/hologenomics/juliej/data/inrich/targetGeneList.txt \
			-a positions.RoH.'+species+'.'+ID+'.txt\
			-i 2 \
			-c \
			-o '+ID+'.RoH \
			')
