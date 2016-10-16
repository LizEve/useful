#! /usr/bin/env python

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
for g in glob.glob('*_mstx.txt'):
	
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split("_")[0]

	#create path to empTree folder. stolen from amp script so leaving "amp" in script
	ampDirPath = os.path.join(mainDir,gene + "_empTree/")
	
	#make directory for emp files if needed
	if not os.path.exists(ampDirPath):
		os.mkdir(ampDirPath)	

	#move into gene output folder
	outputDirPath = os.path.join(mainDir,gene,"output/")
	os.chdir(outputDirPath)

	#copy posterior tree file to empTree directory
	t = gene + "_posterior.trees"
	shutil.copy2(t,ampDirPath+t)

	# move to main directory and copy missing taxa file into empTree folder
	os.chdir(mainDir)
	mstxrm_file = gene +"_mstx.txt"
	shutil.copy2(mstxrm_file,ampDirPath+mstxrm_file)

	#move to empTree folder
	os.chdir(ampDirPath)

	#store missing taxa information into memory
	txrm = []
	taxaremoved =[]
	for tx in open(mstxrm_file,'r'):
		txrm.append(tx.strip())
		for x in txrm:
			y=x.split("_")
			taxa=y[0]+" "+y[1]
			taxaremoved.append(taxa)

	# check version of dendropy 
	version=dendropy.__version__.split(".")[0]
	if version == '4':
		#open tree file, create output file name, initiate tree list for mstxrm file
		with open(t) as trees:
			print gene
			mstxrmOut = gene + '_mstxrm.trees'
			mstxrmTreeList = dendropy.TreeList()
			#skip first line
			next(trees)
			#iterate through lines in file
			for i in trees:
				# 4th column has newick tree, grab this
				newTree = (i.split()[4])
				#turn into tree object
				ppTree = dendropy.Tree.get(data=newTree, schema='newick')
				#prune taxa
				ppTree.prune_taxa_with_labels(taxaremoved)
				#add to tree list
				mstxrmTreeList.append(ppTree)
			#write out tree list of mstxrm
			mstxrmTreeList.write(path=mstxrmOut, schema='nexus')
	elif version == '3':
		print "Please install Dendropy4 or edit script to work with Dendropy 3"
	else:
		print "Your version of Dendropy is either REAL old or non-existant. Please install Dendropy4"

	#move out of folder and begin again
	os.chdir(mainDir)