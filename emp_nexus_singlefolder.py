#! /usr/bin/env python
## converts a file of newick trees to a nexus file 
## run in folder where all trees are to be turned into nexus files
import dendropy
import os
import sys
import glob
import shutil
import itertools


mainDir = os.getcwd()

#iterate through gene folders, need to have some handle to iterate through these. 
#using _mstx.txt since we need these files anyway later
for g in glob.glob('*.trees'):
	
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split(".")[0]+"."+g.split(".")[1]

	# check version of dendropy 
	version=dendropy.__version__.split(".")[0]
	if version == '4':
		#open tree file, create output file name, initiate tree list for mstxrm file
		with open(g) as trees:
			print gene
			Out = gene + 'nex.trees'
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
