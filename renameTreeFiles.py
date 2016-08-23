#! /usr/bin/env python

import os
import glob

for t in glob.glob('*.trees'):
	name = t.split(".")[0]
	gene = name.split("_")[0]
	num = name.split("_")[1]
	run = name.split("_")[2]
	newName = gene + "_" + num + "_r" + run + ".trees"
	print newName
	os.rename( t , newName)