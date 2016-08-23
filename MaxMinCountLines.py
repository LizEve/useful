#! /usr/bin/env python

import os
import glob

f1=open('./SimTreeLen.txt', 'wb')
for f in glob.glob('*.nex'):
	gene = f.split(".")[0]
	pathname = os.path.join(gene,"output")
	numfiles = len(os.listdir(pathname))
	simtree = gene + "_posterior.trees"
	if numfiles > 159:
		os.chdir(pathname)
		flens = []
		for sim in glob.glob('posterior_predictive_sim_*'):
			os.chdir(sim)
			nlines = sum(1 for line in open(simtree))
			#print nlines
			flens.append(nlines)
			os.chdir("../")
		mx=max(flens)
		mn=min(flens)
		f1.write(gene + "max - " + str(mx) + "\n")
		f1.write(gene + "min - " + str(mn) + "\n")
		os.chdir("../../")
	else:
		f1.write(gene + " nope" + "\n")
