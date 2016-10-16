#! /usr/bin/env python
##morhplogy version
###Useage: ./convertToNexus.py path/to/newick/tree/file
## run in folder containing gene.nex and original gene/ folders from revbayes output
## also need list of taxa that are to be removed from tree gene_mstx.txt
### converts a file of newick trees to a nexus file AND removes a list of taxa
import dendropy
import os
import sys
import glob
import shutil
import itertools


mainDir = os.getcwd()

#iterate through gene folders, need to have some handle to iterate through these. 
#using _mstx.txt since we need these files anyway later
for g in glob.glob('morphology_*'):
	
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split("_")[1]

	#create path to empTree folder. stolen from amp script so leaving "amp" in script
	ampDirPath = os.path.join(mainDir,gene + "_empTree/")
	
	#make directory for emp files if needed
	if not os.path.exists(ampDirPath):
		os.mkdir(ampDirPath)	

	#move into gene output folder
	outputDirPath = os.path.join(mainDir,g,"output/")
	os.chdir(outputDirPath)

	#copy posterior tree file to empTree directory
	t = g + "_posterior.trees"
	shutil.copy2(t,ampDirPath+t)

	# move to main directory 
	os.chdir(mainDir)
	
	#move to empTree folder
	os.chdir(ampDirPath)

	# check version of dendropy 
	version=dendropy.__version__.split(".")[0]
	if version == '4':
		#open tree file, create output file name, initiate tree list for mstxrm file
		with open(t) as trees:
			print gene
			Out = gene + '.trees'
			TreeList = dendropy.TreeList()
			#skip first line
			next(trees)
			#iterate through lines in file
			for i in trees:
				# 4th column has newick tree, grab this
				newTree = (i.split()[4])
				#turn into tree object
				ppTree = dendropy.Tree.get(data=newTree, schema='newick')
				#add to tree list
				TreeList.append(ppTree)
				print i.split()[0]
			#write out tree list of mstxrm
			TreeList.write(path=Out, schema='nexus')
	elif version == '3':
		print "Please install Dendropy4 or edit script to work with Dendropy 3"
	else:
		print "Your version of Dendropy is either REAL old or non-existant. Please install Dendropy4"

	#move out of folder and begin again
	os.chdir(mainDir)