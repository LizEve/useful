#! /usr/bin/env python

import os
import glob
import shutil 
import itertools
import dendropy


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#takes tree file, burnin, output file length and returns a treelist object
def subsample(tree_file, burnin, final_file_len):
	numTrees = file_len(tree_file) - burnin - 1
	counter = numTrees/final_file_len 
	stop = final_file_len*counter + 1 + burnin
	if min(file_len(tree_file), numTrees, counter, stop) > 0:
		if numTrees > final_file_len*counter + 1:
			#check dendropy version
			version=dendropy.__version__.split(".")[0]
			if version == '4':
				#open tree file, create output file name, initiate dendropy tree list
				with open(tree_file) as trees:
					tree_list = dendropy.TreeList()
					#iterate through lines in file, split out newick string, transform to tree object, add to tree list
					for i in itertools.islice(trees, burnin, stop, counter):
						newTree = (i.split()[4])
						tree = dendropy.Tree.get(data=newTree, schema='newick')
						tree_list.append(tree)
						#print(len(tree_list))
			elif version == '3':
				with open(t) as trees:
					tOut = tName + '.t'
					tree_list = dendropy.TreeList()
					for i in itertools.islice(trees, burnin, stop, counter):
						newTree = (i.split()[4])
						tree = dendropy.Tree.get_from_string(newTree, schema='newick')
						tree_list.append(tree)
						#print(len(tree_list))
		#if file isn't long enough. 			
		elif numTrees <= final_file_len*counter + 1:
			print t+" is too short. A .t file has NOT been created."
	elif min(file_len(tree_file), numTrees, counter, stop) <= 0:
			print t+" is too short"
	return tree_list

#writes to file a tree list
def write_tree_list(tree_list,out_file):
	tree_list.write_to_path(out_file, schema='nexus')

#takes dendropy tree list, creates 50% consensus tree and max clade credibility tree and write to file.
def consensus_trees(tree_list,file_prefix,out_dir):
	conOut = os.path.join(out_dir, file_prefix + '_con.nex')
	mcctOut = os.path.join(out_dir, file_prefix + '_mcct.nex')
	con=tree_list.consensus(min_freq=0.5)
	con.write_to_path(conOut, schema="nexus")
	mcct=tree_list.maximum_product_of_split_support_tree()
	mcct.write_to_path(mcctOut, schema="nexus")

#iterates through gene folders, subsamples emp files, and outputs consensus trees
def iterate_emp_subsamp(root_dir, out_dir, final_file_len=100, burnin=1):
	if not os.path.exists(out_dir): #make output dir if not there
		os.mkdir(out_dir)
	for gene in os.listdir(root_dir): #iterate through list of gene files only
		print gene
		gene_folder = os.path.join(root_dir,gene)
		output_folder = os.path.join(gene_folder,"output/")
		print gene_folder
		if os.path.exists(output_folder):
			print output_folder
			tree_file = os.path.join(gene_folder,"output/",gene + '_posterior.trees')
			emp_trees = subsample(tree_file,burnin,final_file_len)
			out_file = os.path.join(out_dir,gene + '_subsamp.t')
			write_tree_list(emp_trees,out_file)
			consensus_trees(emp_trees,gene,out_dir)

# iterates through .t files in _amp folders. Outputs consensus tree files
def iterate_consensus_amp(root_dir, out_dir):
	os.chdir(root_dir)
	for folder in glob.glob('*_amp'):
		gene = folder.split("_")[0]
		amp_folder = os.path.join(root_dir,folder)
		for tree in glob.glob('*.t'):
			tree_file = os.path.join(amp_folder,'tree')
			file_prefix = gene+'_'+tree.split("_")[1]
			tree_list = dendropy.TreeList()
			tree_list.read_from_path(tree_file, 'nexus', rooting='force-unrooted')
			consensus_trees(tree_list,file_prefix)




