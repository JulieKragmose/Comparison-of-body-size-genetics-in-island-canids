#!/usr/bin/env python3

#section 3.1.4 in report
#Makes a dataframe of the united topX genes in paired samples and finds the heterozygosities

import sys


# Argument: <speciesType>


#INPUT ARGUMENTS
if len(sys.argv) == 1:
	sys.stderr.write('No input arguments \n')
	sys.exit(1)	
elif len(sys.argv) == 2:
	speciesType = sys.argv[1]



top = ['500', '750', '1000', '1250', '1500', '1750', '2000']



for X in top:
	pairfile = open('/groups/hologenomics/juliej/data/wilcoxonTest/pairs.'+speciesType+'.txt', 'r')
	#Find first X genes and heterozygosities for both species
	for speciesPair in pairfile:
		split = speciesPair.split()		
		species1 = split[0]
		ID1 = split[1]
		species2 = split[2]
		ID2 = split[3]
		genes1 = {}
		genes2 = {}
		
		print(ID1, 'X', ID2, '- top'+X)
		
		hetfile = open('/groups/hologenomics/juliej/data/allData.txt' ,'r')
		for line in hetfile:
			ID = line.split()[1]
			
			if ID == ID1 and len(genes1) < int(X):
				gene = line.split()[2]			
				het = float(line.split()[6])
				if gene in genes1:
					genes1[gene].append(het)
				else: 
					genes1[gene] = [het]
				
					
			if ID == ID2 and len(genes2) < int(X):
				gene = line.split()[2]
				het = float(line.split()[6])
				if gene in genes2:
					genes2[gene].append(het)						
				else: 
					genes2[gene] = [het]
		
		#Calculate mean of heterozygosities
		for i in genes1.items():
			gene = i[0]
			hets = i[1]	
			summation = sum(hets)
			if len(hets) > 1:
				het = summation/len(hets)
			else:
				het = summation
			genes1[gene]=het
		
		for i in genes2.items():
			gene = i[0]
			hets = i[1]	
			summation = sum(hets)
			if len(hets) > 1:
				het = summation/len(hets)
			else:
				het = summation
			genes2[gene]=het


		#Check how many genes there are in total between the two species
		check = []
		for gene in genes1.keys():
			check.append(gene)
		for gene in genes2.keys():
			if gene not in check:
				check.append(gene)
			
	
	
		#FIX THE MISSING VALUES
		#Find missing genes for ID1
		missing1 = []
		for gene in genes2.keys():
			if gene not in genes1:
				missing1.append(gene)
				
		#Find missing genes for ID2
		missing2 = []
		for gene in genes1.keys():
			if gene not in genes2:
				missing2.append(gene)
				
		#Find heterozygosities for missing genes
		hetfile = open('/groups/hologenomics/juliej/data/allData.txt', 'r')
		for line in hetfile:
			split = line.split()
			ID = split[1]
			gene = split[2]
			
			#Add the missing genes and heterozygosities to ID1
			if ID == ID1 and gene in missing1:
				het = float(split[6])
				if gene in genes1:
					genes1[gene] += het
					genes1[gene] = (genes1[gene])/2
				else:
					genes1[gene] = het
			
			#Add the missing genes and heterozygosities to ID2
			if ID == ID2 and gene in missing2:
				het = float(split[6])
				if gene in genes2:
					genes2[gene] += het
					genes2[gene] = (genes2[gene])/2
				else:
					genes2[gene] = het
			
	
#OUTPUT STATS
	#Genes with NA or mysteriously not existing 
		genelist1 = []
		genelist2 = []
		missinglist1 = []
		missinglist2 = []
		
		#List genes
		for gene in genes1.keys():
			genelist1.append(gene)
		
		for gene in genes2.keys():
			genelist2.append(gene)
		
		#Check the missing ones
		for gene in check:
			if gene not in genelist1:
				missinglist1.append(gene)
			if gene not in genelist2:
				missinglist2.append(gene)
		
	
	
		#COMBINE DATAFRAMES
		count = 0
		outfile = open('top'+X+'.'+ID1+'_'+ID2+'.txt', 'w')
		outfile.write('Gene \t ID1_het \t ID2_het \n')
		for gene in check:
			if gene in genes1 and gene in genes2:
				outfile.write(gene+'\t'+str(genes1[gene])+'\t'+str(genes2[gene])+'\n')
				count += 1	
		outfile.close()
		
		#PRINT STATS
		print('# genes supposed to be in output:', len(check))
		print('# genes actually in output:', count)
		print('# genes omitted due to NA:', len(check)-count)
		print('\n')
				
		
pairfile.close()
hetfile.close()

