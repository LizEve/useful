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
for g in glob.glob('*.trees'):
	
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split(".")[0]

	# missing taxa list file
	mstxrm_file = "mstx.txt"
	
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
		with open(g) as trees:
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
				print i.split()[0]
			#write out tree list of mstxrm
			mstxrmTreeList.write(path=mstxrmOut, schema='nexus')
	elif version == '3':
		print "Please install Dendropy4 or edit script to work with Dendropy 3"
	else:
		print "Your version of Dendropy is either REAL old or non-existant. Please install Dendropy4"
