#! /usr/bin/env python
##Usage:
## run in folder containing gene.nex and gene/ and convertToNexus.py
## This script is currently setup to assume there are four replicate runs for each emperical run.
## burninSamples should be the number of printed lines that are burning in your simulated run. 
## the emperical run will already have burnin removed.
## the resulting files should have the following format
##  <basename>_<simfile#>_<rep#>.t, 
##  <basename>_emp_<rep#>.t  

import os
import glob
import shutil 
import itertools
import dendropy

###### USER INPUT
# desired number of trees in subsampled file for amp
ssFileLen = 100
# burnin number of lines. 2000 gen burnin / 10 gen print rate = burnin of 200 lines
# because we count from 0, burnin will automatically include header line
# for all files, emperical and simulated. make two options later
burnin = 250
"""
import sys
if len(sys.argv) ==1:
	print 'you need the XXX as an argument'
	sys.exit(-1)
else:
	file = sys.argv[1]
"""
######


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#make sure you are in directory that you are calling script from 
mainDir = os.getcwd()

#iterate through gene folders, need to have some handle to iterate through these. could be *.nex
for g in glob.glob('*.nex'):
	
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split(".")[0]
	#create path to amp folder
	ampDirPath = os.path.join(mainDir,gene + "_amp/")
	#make directory for amp files
	#move to ampdir
	os.chdir(ampDirPath)
	#iterate through tree files
	for t in glob.glob('*.trees'):
		#get some info, file name, number of trees, counter for subsampling file, when to stop sampling file
		tName = t.split(".")[0]
		gene = tName.split("_")[0]
		run = tName.split("_")[2]
		numTrees = file_len(t) - burnin - 1
		counter = numTrees/ssFileLen
		stop = ssFileLen*counter + 1 + burnin
		#debug
		variables = [tName,file_len(t),numTrees,counter,burnin,stop]
		print variables
		#check if there are enough trees in file
		if min(file_len(t), numTrees, counter, stop) > 0:
			if numTrees > ssFileLen*counter + 1:
				#check dendropy version
				version=dendropy.__version__.split(".")[0]
				if version == '4':
					#open tree file, create output file name, initiate dendropy tree list
					with open(t) as trees:
						tOut = tName + '.t'
						ppTreeList = dendropy.TreeList()
						#iterate through lines in file, split out newick string, transform to tree object, add to tree list
						for i in itertools.islice(trees, burnin, stop, counter):
							newTree = (i.split()[4])
							print (i.split()[0])
							ppTree = dendropy.Tree.get(data=newTree, schema='newick')
							ppTreeList.append(ppTree)
							#print(len(ppTreeList))
						#output tree list to outfile that is now readable into amp
						ppTreeList.write(path=tOut, schema='nexus')
						print file_len(tOut)
				elif version == '3':
					with open(t) as trees:
						tOut = tName + '.t'
						ppTreeList = dendropy.TreeList()
						for i in itertools.islice(trees, burnin, stop, counter):
							newTree = (i.split()[4])
							ppTree = dendropy.Tree.get_from_string(newTree, schema='newick')
							ppTreeList.append(ppTree)
							print(len(ppTreeList))
						ppTreeList.write_to_path(tOut, schema='nexus')
			#if file isn't long enough. 			
			elif numTrees <= ssFileLen*counter + 1:
				print t+" is too short. A .t file has NOT been created."
		elif min(file_len(t), numTrees, counter, stop) <= 0:
				print t+" is too short"

	#move out of folder and begin again
	os.chdir(mainDir)
