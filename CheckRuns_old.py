#! /usr/bin/env python
##Usage:
## run in folder containing gene.nex and GENE/ files/folders
## This script is currently setup to work with the raw output from revbayes posterior prediction pipeline
## One run per simulated dataset is assumed
## burninSamples should be the number of printed lines that are burning in your simulated run. 
## the emperical run will already have burnin removed.
## This script attempts to identify runs with poor mixing or that have gotten stuck in the wrong treespace
## It looks for simulated data that have parameteres with posterior distributions that are more variable than the emperical, for example, double peaked traces or burnin that needs to be removed
## It also looks to make sure the sim posterior distributions are not more than 3 devs of the emp mean. I'm not sure if this is really checking what i want it to. 


import os
import glob
import shutil 
import itertools
import fnmatch
import numpy as np

###### USER INPUT
# desired number of trees in subsampled file for amp
ssFileLen = 100
# burnin number of lines. 2000 gen burnin / 10 gen print rate = burnin of 200 lines
# because we count from 0, burnin will automatically include header line
# for all files, emperical and simulated. make two options later
burnin = 250

######
#make sure you are in directory that you are calling script from 
mainDir = os.getcwd()

#open a file to write issues to
outFileDirPath = os.path.join(mainDir,'Problem_children.txt')
with open(outFileDirPath, 'w') as fp:

	#iterate through gene folders, need to have some handle to iterate through these. could be *.nex
	for g in glob.glob('*.nex'):
		#split off locus name, dependant on what your iterating handle files are
		gene = g.split(".")[0]
		#create path to output
		outputDirPath = os.path.join(mainDir,gene, "output/")

		#move to logsdir
		os.chdir(outputDirPath)

		#open emp run and get std and mean for parameters
		emp = gene + '_posterior.log'
		with open(emp) as f:
			#start lists of values
			eprm1List = []
			eprm2List = []
			eprm3List = []
			etlList = []

			#skip burnin lines
			for header in xrange(1):
				next(f)
			#iterate through lines, pull out param values. Append to lists. 
			for line in f:
				prm1 = float(line.split("\t")[-2])
				prm2 = float(line.split("\t")[-3])
				prm3 = float(line.split("\t")[-4])
				TL = float(line.split("\t")[-1])

				# add paramters to list
				eprm1List.append(prm1) 
				eprm2List.append(prm2) 
				eprm3List.append(prm3)  
				etlList.append(TL) 

				#store std and mean for each one
				empprm1_std = np.std(eprm1List)
				empprm1_mean = np.mean(eprm1List)

				empprm2_std = np.std(eprm2List)
				empprm2_mean = np.mean(eprm2List)

				empprm3_std = np.std(eprm3List)
				empprm3_mean = np.mean(eprm3List)

				emptl_std = np.std(etlList)
				emptl_mean = np.mean(etlList)
		fp.write(gene + " prm1 mean, std" + "\n")
		fp.write(str(empprm1_mean) + ", ")
		fp.write(str(empprm1_std) + "\n")
		fp.write(gene + " prm2 mean, std" + "\n")
		fp.write(str(empprm2_mean) + ", ")
		fp.write(str(empprm2_std) + "\n")
		fp.write(gene + " prm3 mean, std" + "\n")
		fp.write(str(empprm3_mean) + ", ")
		fp.write(str(empprm3_std) + "\n")
		fp.write(gene + " TL mean, std" + "\n")
		fp.write(str(emptl_mean) + ", ")
		fp.write(str(emptl_std) + "\n")
		#create lists to store information in
		std_LHs=[]
		std_Ps=[]
		mean_LHs=[]
		mean_Ps=[]
		all_sim_stats = [["simName", "sim_mean_LH_means", "sim_std_LH_means", "sim_mean_P_means", "sim_std_P_means"]]

		#iterate through sim log files. 
		for pps in glob.glob('posterior_predictive_sim_*'):
			#get sim num
			sim = pps.split("_")[3]
			logName = gene+'_posterior.log'
			logDirPath = os.path.join(outputDirPath,pps,logName)
			tag = gene+"_"+sim

			# open sim log file
			with open(logDirPath) as f:
				# initiate lists
				sprm1List = []
				sprm2List = []
				sprm3List = []
				stlList = []
				#skip burnin lines
				for badline in xrange(burnin):
					next(f)
				#iterate through lines, pull out Likelihood and posterior values. Append to lists. 
				for line in f:
					prm1 = float(line.split("\t")[-2])
					prm2 = float(line.split("\t")[-3])
					prm3 = float(line.split("\t")[-4])
					TL = float(line.split("\t")[-1])
					# add paramters to list
					sprm1List.append(prm1) 
					sprm2List.append(prm2) 
					sprm3List.append(prm3)  
					stlList.append(TL) 

				# store std and mean for each one (not sure I need stds for sims)
				simprm1_std = np.std(sprm1List)
				simprm1_mean = np.mean(sprm1List)
				simprm1_median = np.median(sprm1List)

				simprm2_std = np.std(sprm2List)
				simprm2_mean = np.mean(sprm2List)
				simprm2_median = np.median(sprm2List)

				simprm3_std = np.std(sprm3List)
				simprm3_mean = np.mean(sprm3List)
				simprm3_median = np.median(sprm3List)

				simtl_std = np.std(stlList)
				simtl_mean = np.mean(stlList)
				simtl_median = np.median(stlList)

				# if the mean for any of these is outside one std of the emp mean, print name and which value to output file
				if simprm1_mean > float(empprm1_mean+3*empprm1_std):
					issue = str(simprm1_mean) + ' - ' + tag + "  part_rate_mult_1_mean" + "\n"
					fp.write(issue)
				elif simprm1_mean < float(empprm1_mean-3*empprm1_std):
					issue = str(simprm1_mean) + ' - ' + tag + "  part_rate_mult_1_mean" + "\n"
					fp.write(issue)

				if simprm2_mean > float(empprm2_mean+3*empprm2_std):
					issue = str(simprm2_mean) + ' - ' + tag + "  part_rate_mult_2_mean" + "\n"
					fp.write(issue)
				elif simprm2_mean < float(empprm2_mean-3*empprm2_std):
					issue = str(simprm2_mean) + ' - ' + tag + "  part_rate_mult_2_mean" + "\n"
					fp.write(issue)

				if simprm3_mean > float(empprm3_mean+3*empprm3_std):
					issue = str(simprm3_mean) + ' - ' + tag + "  part_rate_mult_3_mean" + "\n"
					fp.write(issue)
				elif simprm3_mean < float(empprm3_mean-3*empprm3_std):
					issue = str(simprm3_mean) + ' - ' + tag + "  part_rate_mult_3_mean" + "\n"
					fp.write(issue)

				if simtl_mean > float(emptl_mean+3*emptl_std):
					issue = str(simtl_mean) + ' - ' + tag + "  TL_mean" + "\n"
					fp.write(issue)
				elif simtl_mean < float(emptl_mean-3*emptl_std):
					issue = str(simtl_mean) + ' - ' + tag + "  TL_mean" + "\n"
					fp.write(issue)

			# if the std for any of these is outside one std of the emp std, print name and which value to output file
				if simprm1_std > float(empprm1_std):
					issue = str(simprm1_std) + ' - ' + tag + "  part_rate_mult_1_std" + "\n"
					fp.write(issue)

				if simprm2_std > float(empprm2_std):
					issue = str(simprm2_std) + ' - ' + tag + "  part_rate_mult_2_std" + "\n"
					fp.write(issue)
				
				if simprm3_std > float(empprm3_std):
					issue = str(simprm3_std) + ' - ' + tag + "  part_rate_mult_3_std" + "\n"
					fp.write(issue)
				
				if simtl_std > float(emptl_std):
					issue = str(simtl_std) + ' - ' + tag + "  TL_std" + "\n"
					fp.write(issue)
								
		#move out of folder and begin again
		os.chdir(mainDir)
