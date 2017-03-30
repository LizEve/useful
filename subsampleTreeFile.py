#! /usr/bin/env python
##Usage:
import os
import glob
import itertools
import dendropy

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def rb_treelist(t,burn,total_trees):
	# For RevBayes we also use this to delete the header file
	rb_burnin = burn + 2
	# Get number of trees in post-burnin sample	
	numTrees = file_len(t) - rb_burnin
	# Sampler counter
	counter = numTrees/total_trees
	# When to stop
	stop = total_trees*counter + rb_burnin
	#debug
	variables = [file_len(t),numTrees,counter,rb_burnin,stop]
	#print("numbers for debugging - " + str(variables))
	#check if there are enough trees in file
	if min(file_len(t), numTrees, counter, stop) > 0:
		if numTrees > total_trees*counter:
			#check dendropy version
			version=dendropy.__version__.split(".")[0]
			if version == '4':
				#open tree file, create output file name, initiate dendropy tree list
				with open(t) as trees:
					sub_tree_list = dendropy.TreeList()
					#iterate through lines in file, split out newick string, transform to tree object, add to tree list
					print(t + " - reading in files...")
					print("numbers for debugging - " + str(variables))
					for i in itertools.islice(trees, rb_burnin, stop, counter):
						tree = (i.split()[4])
						sub_tree = dendropy.Tree.get(data=tree, schema='newick')
						sub_tree_list.append(sub_tree)
					print("subsampled trees  - "+str(len(sub_tree_list)))
					return sub_tree_list
			elif version == '3':
				with open(t) as trees:
					tOut = tName + '.t'
					sub_tree_list = dendropy.TreeList()
					print(t + " - reading in files...")
					print("numbers for debugging - " + str(variables))
					for i in itertools.islice(trees, rb_burnin, stop, counter):
						tree = (i.split()[4])
						sub_tree = dendropy.Tree.get_from_string(newTree, schema='newick')
						sub_tree_list.append(sub_tree)
					print("subsampled trees  - "+str(len(sub_tree_list)))
					return sub_tree_list			
		elif numTrees <= total_trees*counter:
			print(t+" is too short")
	elif min(file_len(t), numTrees, counter, stop) <= 0:
			print(t+" your variables are wrong")

def mb_treelist(t,burn,total_trees):
	# Account for computer starting from 0. So generation 4 is actually 5 trees into the file. 
	mb_burnin = burn + 1
	print(t + " - reading in files...")
	in_trees = dendropy.TreeList.get(path=t, schema = 'nexus')
	# Number of valid trees (no burnin)
	numTrees = len(in_trees) - mb_burnin
	# Sampler counter
	counter = numTrees/total_trees
	# When to stop
	stop = total_trees*counter + mb_burnin
	# Debug
	variables = [len(in_trees),numTrees,counter,mb_burnin,stop]
	print("numbers for debugging - " + str(variables))
	#Check if there are enough trees in file
	if min(file_len(t), numTrees, counter, stop) > 0:
		if numTrees > total_trees*counter:
			#check dendropy version
			version=dendropy.__version__.split(".")[0]
			if version == '4':
				sub_tree_list = dendropy.TreeList()
				for i in itertools.islice(in_trees, mb_burnin, stop, counter):
					sub_tree_list.append(i)
				print("subsampled trees - "+str(len(sub_tree_list)))
				return sub_tree_list
			elif version == '3':
				print "install dendropy version 4 or figure out the version 3 code and write it here :)"
			#if file isn't long enough. 			
		elif numTrees <= total_trees*counter:
			print(t+" is too short")
	elif min(file_len(t), numTrees, counter, stop) <= 0:
			print(t+" your variables are wrong")

def save_treelist(in_file,out_file,burn_in,total_trees,file_type):
	if file_type == 'mb':
		treez = mb_treelist(in_file,burn_in,total_trees)
		treez.write(path=out_file, schema='nexus')
	elif file_type == 'rb':
		treez = rb_treelist(in_file,burn_in,total_trees)
		treez.write(path=out_file, schema='nexus')
	else:
		"houston we have a problem"

def save_treelist_multi_input(in_file_suffix,out_file,burn_in,total_trees,file_type):
	if file_type == 'mb':
		# Instantiate master list of subsampled trees
		master_tree_list = dendropy.TreeList()
		# Iterate through tree files
		for in_file in glob.glob('*'+in_file_suffix):
			treez = mb_treelist(in_file,burn_in,total_trees)
			master_tree_list.extend(treez)
		print("total trees in output - " + str(len(master_tree_list)))
		master_tree_list.write(path=out_file, schema='nexus')
	elif file_type == 'rb':
		# Instantiate master list of subsampled trees
		master_tree_list = dendropy.TreeList()
		# Iterate through tree files
		for in_file in glob.glob('*'+in_file_suffix):
			treez = rb_treelist(in_file,burn_in,total_trees)
			master_tree_list.extend(treez)
		print("total trees in output - " + str(len(master_tree_list)))
		master_tree_list.write(path=out_file, schema='nexus')

###### USER INPUT
# in_file - In file path, for single input only
# out_file - Out file path
# burn_in - Number of generations for burnin 
# total_trees - Number of trees subsampled from each infile
# file_type - mb for mrbayes, rb for revbayes 

## Single Input Examples
#save_treelist('PTGER4_1.nex.run4.t','sOut.tre',250,100,'mb')
#save_treelist('AHR_posterior_run_4.trees','tOut.tre',250,100,'rb')

## Multiple Input Examples
#save_treelist_multi_input('.trees','multi_tOut.tre',250,100,'rb')
#save_treelist_multi_input('.t','multi_tOut.tre',250,100,'mb')