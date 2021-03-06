#! /usr/bin/env python

###Useage: ./convertToNexus.py path/to/newick/tree/file
## run in folder containing gene.nex and gene/ 
### converts a file of newick trees to a nexus file
import dendropy
import os
import sys
import glob
import shutil
import itertools

###### USER INPUT
# desired number of trees in subsampled file for amp
ssFileLen = 100
# burnin should always be at least 1 to avoid the header
burnin = 1
# handle to iterate through files. Gene must be before the first _
handle = '*_dog'

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#make sure you are in directory that you are calling script from 
mainDir = os.getcwd()

#iterate through gene folders, need to have some handle to iterate through these. using _mstx.txt since we need these files anyway later
for g in glob.glob(handle):
	
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split("_")[0]
	#create path to empTree folder. stolen from amp script so leaving "amp" in script
	empDirPath = os.path.join(mainDir,gene + "_empTree/")
	#make directory for emp files
	if not os.path.exists(empDirPath):
		os.mkdir(empDirPath)	#move into gene folder
	outputDirPath = os.path.join(mainDir,gene,"output/")
	os.chdir(outputDirPath)
	#call name for emp trees concat file and new output name. 
	r = gene + "_posterior.trees"
	t = gene + "_posterior.trees"
	#copy to empTree directory
	shutil.copy2(r,empDirPath+t)

	#move to empdir
	os.chdir(empDirPath)

	#get some info, number of trees, counter for subsampling file, when to stop sampling file
	numTrees = file_len(t) - burnin - 1
	counter = numTrees/ssFileLen
	stop = ssFileLen*counter + 1 + burnin
	#debug
	print os.getcwd(),gene,numTrees,counter,stop
	#check if there are enough trees in file
	if min(file_len(t), numTrees, counter, stop) > 0:
		if numTrees > ssFileLen*counter + 1:
			#check dendropy version
			version=dendropy.__version__.split(".")[0]
			if version == '4':
				#open tree file, create output file name, initiate tree list for out file and mstxrm file
				with open(t) as trees:
					tOut = gene + '_subsam100.t'
					#mstxrmOut = gene + '_mstxrm500.t'
					conOut = gene + '_consensus75.t'
					conOut2 = gene + '_consensus95.t'
					mcctOut = gene + '_mcct.t'
					phyOut = gene + '_consensus50phy.t'
					ppTreeList = dendropy.TreeList()
					mstxrmTreeList = dendropy.TreeList()
					#iterate through lines in file, split out newick string, transform to tree object, add to tree list
					for i in itertools.islice(trees, burnin, stop, counter):
						newTree = (i.split()[4])
						ppTree = dendropy.Tree.get(data=newTree, schema='newick')
						ppTreeList.append(ppTree)
					##output tree list to outfile that is now readable into amp
					ppTreeList.write(path=tOut, schema='nexus')
					#mstxrmTreeList.write(path=mstxrmOut, schema='nexus')
					#con=mstxrmTreeList.consensus(min_freq=0.75)
					#con.write_to_path(conOut, schema="nexus")
					con2=ppTreeList.consensus(min_freq=0.95)
					con2.write_to_path(conOut2, schema="nexus")
					mcct=ppTreeList.maximum_product_of_split_support_tree()
					mcct.write_to_path(mcctOut, schema="nexus")

			"""elif version == '3':
													with open(t) as trees:
														tOut = gene + '_subsamp100.t'
														ppTreeList = dendropy.TreeList()
														for i in itertools.islice(trees, burnin, stop, counter):
															newTree = (i.split()[4])
															ppTree = dendropy.Tree.get_from_string(newTree, schema='newick')
															ppTreeList.append(ppTree)
															#print(len(ppTreeList))
														ppTreeList.write_to_path(tOut, schema='nexus')"""
		#if file isn't long enough. 			
		elif numTrees <= ssFileLen*counter + 1:
			print t+" is too short. A subsamp.t file has NOT been created."
	elif min(file_len(t), numTrees, counter, stop) <= 0:
			print t+" is too short"
	#move out of folder and begin again
	os.chdir(mainDir)