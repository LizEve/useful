#! /usr/bin/env python
import os
import glob
import tree_distances as dist
dir_30 = '/Users/ChatNoir/Projects/Squam/RevBayes/Consensus_prm30/'
dir_100 = '/Users/ChatNoir/Projects/Squam/RevBayes/Consensus_prm100/'
os.chdir(dir_30)
for file_30 in glob.glob('*con.nex'):
	os.chdir(dir_100)
	for file_100 in glob.glob('*con.nex'):
		if file_30 == file_100:
			print file_30
			t_30 = os.path.join(dir_30,file_30)
			t_100 = os.path.join(dir_100,file_100)
			d = dist.rf_unweighted(t_30,t_100)
			print d