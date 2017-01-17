#! /usr/bin/env python
##Usage:
## run in folder containing gene.nex and gene/ and GENE_amp/ folders

import os
import glob
import shutil 
import itertools
import fnmatch

mainDir = os.getcwd()
os.chdir(mainDir)

renamedGuide = [('Old_name','New_name')]

for g in glob.glob('*_amp'):
	
	# split off locus name, dependant on what your iterating handle files are
	gene = g.split("_")[0]
	renamed = os.path.join(mainDir,gene+"_renamed")
	print gene
	if not os.path.exists(renamed):
		os.makedirs(renamed)

	# change to gene folder
	os.chdir(g)

	# get file path
	gfolder = os.getcwd()

	count=1

	for t in glob.glob('*r1.t'):

		sim = t.split("_")[1]

		if sim == 'emp':
			ewild = gene+"_"+str(sim)+"_*"
			for file in os.listdir('.'):
				if fnmatch.fnmatch(file, ewild):
					empNewPath = os.path.join(renamed,file)
					shutil.copy(file,empNewPath)
		else:
			#name r1 log file and create a wildcard to pick up other runs from same simulation
			wild = gene+"_"+str(sim)+"_*"
			#find all files in the current folder from the same simulation number as the current r1.log 
			for file in os.listdir('.'):
				if fnmatch.fnmatch(file, wild):
					r = file.split("_")[2]
					tnewName = gene+'_'+str(count)+'_'+r
					tnewPath = os.path.join(renamed,tnewName)
					tuprename = (file,tnewName)
					renamedGuide.append(tuprename)
					shutil.copy(file,tnewPath)
			count += 1

	os.chdir(mainDir)

with open('renamedGuide.txt', 'w') as fp:
		fp.write('\n'.join('{} {}'.format(*x) for x in renamedGuide))
