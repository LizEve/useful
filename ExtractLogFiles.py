#! /usr/bin/env python

import os
import glob
import shutil 
import itertools


mainDir = os.getcwd()

#iterate through gene folders, need to have some handle to iterate through these. could be *.nex
for g in glob.glob('*.nex'):
	
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split(".")[0]
	#create path to amp folder
	logDirPath = os.path.join(mainDir,gene + "_logs/")
	#make directory for amp files
	if not os.path.exists(logDirPath):
		os.mkdir(logDirPath)	#move into gene folder
	outputDirPath = os.path.join(mainDir,gene,"output/")
	os.chdir(outputDirPath)
	#put emp files into ampDir
	for r in glob.glob('*_run_*.log'):
		runNum = r.split("_")[3]
		#create amp file name structure
		outFile = gene + "_emp_r" + runNum
		#move to amp folder
		shutil.copy2(r,logDirPath+outFile)
	# iterate through pp out files
	for p in glob.glob('posterior_predictive_sim_*'):
		simNum = p.split("_")[3]
		# move into each pp folder
		os.chdir(p)
		#iterate run files, rename and move to ampDir
		for r in glob.glob('*_run_*.log'):
			runNum = r.split("_")[3]
			outFile = gene + "_" + simNum + "_r" + runNum
			shutil.copy2(r,logDirPath+outFile)
		#move to gene/output
		os.chdir(outputDirPath)
	#move out of folder and begin again
	os.chdir(mainDir)
