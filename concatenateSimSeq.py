
#! /usr/bin/env python

import os
import glob
from Bio.Nexus import Nexus

mainDir = os.getcwd()

for g in glob.glob('*_sims'):
	# pull out gene name
	gene = g.split("_")[0]
	# create path to gene folder
	geneDirPath = os.path.join(mainDir,g)
	# move into gene folder
	os.chdir(geneDirPath)
	for p in glob.glob('posterior_predictive_sim_*'):
		simNum = p.split("_")[3]
		# make name for concat nexus file
		concatNex = gene + "_" + simNum + ".nex"
		# make folder for sim seq
		mbRunDirPath = os.path.join(mainDir, gene + "_" + simNum)
		nexOutPath = os.path.join(mbRunDirPath,concatNex)
		if not os.path.exists(mbRunDirPath):
			os.mkdir(mbRunDirPath)
		#debug
		print simNum, concatNex, mbRunDirPath, nexOutPath

		# move into sim seq folder
		os.chdir(p)
		seqList =["phyloSeq[1].nex", "phyloSeq[2].nex", "phyloSeq[3].nex"]
		nexConvert =  [(f, Nexus.Nexus(f)) for f in seqList]
		combine = Nexus.combine(nexConvert)
		combine.write_nexus_data(filename=open(nexOutPath, 'w'))
		os.chdir(geneDirPath)
	os.chdir(mainDir)

