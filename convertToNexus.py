#! /usr/bin/env python

###Useage: ./convertToNexus.py path/to/newick/tree/file
### converts a file of newick trees to a nexus file
import dendropy
import os
import sys
import ntpath


if len(sys.argv) ==1:
	print 'you need the filename as an argument'
	sys.exit(-1)
else:
	file = sys.argv[1]

out=ntpath.basename(file).split(".")[0]+"_r1.t"


pp_trees = dendropy.TreeList()
pp_trees.read_from_path(file, 'newick', rooting='force-unrooted')
pp_trees.write_to_path(out, schema='nexus')