#! /usr/bin/env python

###Useage: ./convertToNexus.py path/to/newick/tree/file
### converts a file of newick trees to a nexus file
import dendropy
import os
import sys
import glob
import ntpath


if len(sys.argv) ==1:
	print 'you need the filename as an argument'
	sys.exit(-1)
else:
	file = sys.argv[1]



file="UBN1_emp.t"

base=ntpath.basename(file).split("_")[0]
out1=base+"_r1.t"
out2=base+"_mstxrm.t"

pp_trees = dendropy.TreeList()
pp_trees.read_from_path(file, 'newick', rooting='force-unrooted')
pp_trees.write_to_path(out1, schema='nexus')


mstxrm_trees = dendropy.TreeList()
mstxrm_file = base+"_mstx.txt"
txrm = []
for tx in open(mstxrm_file,'r'):
	txrm.append(tx.strip())
	for x in txrm:
		y=x.split("_")
		taxa=y[0]+" "+y[1]
		taxaremoved.append(taxa)

for tree in pp_trees:
	tree.prune_taxa_with_labels(taxaremoved)
	mstxrm_trees.append(tree)

mstxrm_trees.write_to_path(out2, schema='nexus')



"""
for f in glob.glob('*_empTree'):
	gene = f.split("_")[0]
	tfile = gene + "_emp.t"
	fpath = os.path.join(f,tfile)
	tree = dp.Tree.get_from_path(fpath,schema='newick')
	tree.prune_taxa_with_labels(taxaremoved)
"""