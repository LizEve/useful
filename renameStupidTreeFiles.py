#! /usr/bin/env python
##Usage:
## run in folder GENE_amp/ to rename GENE_sim_run_#.trees to GENE_sim_r#.trees

import os
import glob
import shutil 
import itertools
import fnmatch

mainDir = os.getcwd()

for t in glob.glob('*.trees'):
	gene = t.split("_")[0]
	sim = t.split("_")[1]
	num = t.split("_")[3]

	newName = gene+'_'+str(sim)+'_r'+num
	shutil.copy(t,newName)