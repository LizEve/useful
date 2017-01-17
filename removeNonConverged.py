#! /usr/bin/env python
##Usage:
## run in folder containing gene.nex and gene/ and GENE_amp/ folders

import os
import glob
import shutil 
import itertools

#User Input

#File name of sims not converged and folder with all non-converged files

removeFiles='removeFiles.txt'

problemChildren = 'problemChildren'

#make sure you are in directory that you are calling script from 
mainDir = os.getcwd()
os.chdir(mainDir)

#create folder to put non-converged files in
if not os.path.exists(problemChildren):
    os.makedirs(problemChildren)   
pCpath = os.path.join(mainDir,problemChildren)

#store list of files
with open(removeFiles) as f:
	removeList = f.read().splitlines()

#iterate through gene folders, need to have some handle to iterate through these. could be *.nex
for g in glob.glob('*.nex'):
	
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split(".")[0]

	#create path to amp folder
	ampDirPath = os.path.join(mainDir,gene + "_amp/")

	#move to ampdir
	os.chdir(ampDirPath)

	for t in glob.glob('*.t'):
		geneSim = t.split("_")[0] + "_" + t.split("_")[1]
		if geneSim in removeList:
			tnewPath = os.path.join(pCpath,t)
			shutil.move(t,tnewPath)

	#move back to main dir
	os.chdir(mainDir)
