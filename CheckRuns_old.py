#! /usr/bin/env python
##Usage:
## run in folder containing gene.nex and GENE_log/ files
## This script is currently setup to assume there are replicate runs (r1, r2..) for each emperical and sim run.
## burninSamples should be the number of printed lines that are burning in your simulated run. 
## the emperical run will already have burnin removed.
## the resulting files should have the following format
##  <basename>_<simfile#>_<rep#>.t, 
##  <basename>_emp_<rep#>.t  

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

# set max standard deviation allow for likelihood and posterior for each run. 
# I just skimmed a few trace files to get a sense for what numbers seemed reasonable. 
# theoretically this should be calculated in a more logical way that I don't have time or energy to figure out right now. 
#max_LH_std = float(15)
#max_P_std = float(17)

######
#start a list to store information in
problemChildren=[]

#make sure you are in directory that you are calling script from 
mainDir = os.getcwd()

#iterate through gene folders, need to have some handle to iterate through these. could be *.nex
for g in glob.glob('*.nex'):
	
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split(".")[0]
	#create path to logs folder
	logsDirPath = os.path.join(mainDir,gene + "_logs/")

	#move to logsdir
	os.chdir(logsDirPath)

	#create lists to store information in
	std_LHs=[]
	std_Ps=[]
	mean_LHs=[]
	mean_Ps=[]
	all_sim_stats = [["simName", "sim_mean_LH_means", "sim_std_LH_means", "sim_mean_P_means", "sim_std_P_means"]]

	#iterate through only r1 tree files. Because we want to find all files with same sim number, but only once. so only use r1 files to iterate through.
	for log in glob.glob('*r1.log'):
		#get some info, file name, gene name, run #
		logName = log.split(".")[0]
		gene = logName.split("_")[0]
		sim = logName.split("_")[1]
		run = logName.split("_")[2]

		#create temporary list for all runs of this sim #
		sim_LHs = []
		sim_Ps = []
		sim_LH_std = []
		sim_P_std = []

		#if its an emp file skip it, already checked these by hand. dont need to delete burnin. 
		if str(sim) == "emp":
			print "skip emp files"

		else:
			#name r1 log file and create a wildcard to pick up other runs from same simulation
			r1log = gene+"_"+str(sim)+"_"
			wild = gene+"_"+str(sim)+"_*"

			#find all files in the current folder from the same simulation number as the current r1.log 
			for file in os.listdir('.'):
				if fnmatch.fnmatch(file, wild):
					print file
					#grab deets about the file for later
					fname = file.split(".")[0]
					fgene = fname.split("_")[0]
					fsim = fname.split("_")[1]
					frun = fname.split("_")[2]
					tag = gene+"_"+fsim+"_"+frun
					sim = gene+"_"+fsim

					
					# open each log file for a sim.
					with open(file) as f:
						#start lists of values
						listLH = []
						listP =[]
						#skip burnin lines
						for badline in xrange(burnin):
							next(f)
						#iterate through lines, pull out Likelihood and posterior values. Append to lists. 
						for line in f:
							LH = float(line.split("\t")[2])
							P = float(line.split("\t")[1])
							listLH.append(LH)
							listP.append(P)

						#get std for LH and P for run
						run_std_LH = np.std(listLH)
						run_std_P = np.std(listP)

						#add to list for future calcs
						sim_LH_std.append(run_std_LH)
						sim_P_std.append(run_std_P)


						#create tuple with run ID and run std
						tup_std_LH = (tag, run_std_LH)
						tup_std_P = (tag, run_std_P)

						#add run std to gene std list
						std_LHs.append(tup_std_LH)
						std_Ps.append(tup_std_P)

						# add run ID to problems list if stds are larger than preset values
						'''
						if run_std_LH > max_LH_std:
							problemChildren.append(tup_std_LH)
						if run_std_P > max_P_std:
							problemChildren.append(tup_std_P)
						'''
						#get mean for LH and P for run
						run_mean_LH = np.mean(listLH)
						run_mean_P = np.mean(listP)

						#create tuple with run ID and run mean
						tup_mean_LH = (tag, run_mean_LH)
						tup_mean_P = (tag, run_mean_P)

						#add run mean to gene mean list
						mean_LHs.append(tup_mean_LH)
						mean_Ps.append(tup_mean_P)

						#add run mean to sim mean list
						sim_LHs.append(tup_mean_LH)
						sim_Ps.append(tup_mean_P)

			# calculate mean and std for run means of current sim
			list_sim_LHs = [x[1] for x in sim_LHs]
			list_sim_Ps = [x[1] for x in sim_Ps]
			sim_mean_LH=np.mean(list_sim_LHs)
			sim_med_std_LH=np.median(sim_LH_std)
			sim_mean_P=np.mean(list_sim_Ps)
			sim_med_std_P=np.median(sim_P_std)

			# add run ID to problem list if run mean LH or P is outside of 2 stds of sim mean
			for tup in sim_LHs:
				if tup[1] > float(sim_mean_LH+sim_med_std_LH):
					problemChildren.append(tup)
				elif tup[1] < float(sim_mean_LH-sim_med_std_LH):
					problemChildren.append(tup)

			for tup in sim_Ps:
				if tup[1] > float(sim_mean_P+sim_med_std_P):
					problemChildren.append(tup)
				elif tup[1] < float(sim_mean_P-sim_med_std_P):
					problemChildren.append(tup)
			# record sim stats and add to meta list
			# sim_stats=[simName,sim_mean_LH,sim_std_LH_mean]
			sim_stats=[sim, sim_mean_LH, sim_med_std_LH, sim_mean_P, sim_med_std_P]
			print sim_stats
			all_sim_stats.append(sim_stats)

	with open('stds_LH_out.txt', 'w') as fp:
		fp.write('\n'.join('{} {}'.format(*x) for x in std_LHs))
	
	with open('stds_P_out.txt', 'w') as fp:
		fp.write('\n'.join('{} {}'.format(*x) for x in std_Ps))
		
	with open('means_LH_out.txt', 'w') as fp:
		fp.write('\n'.join('{} {}'.format(*x) for x in mean_LHs))
		
	with open('means_P_out.txt', 'w') as fp:
		fp.write('\n'.join('{} {}'.format(*x) for x in mean_Ps))

	with open('sim_stats_out.txt', 'w') as fp:
		fp.write("\n".join((item[0] + ', ' + ', '.join(str(i) for i in item[1:])) for item in all_sim_stats))
			
	#move out of folder and begin again
	os.chdir(mainDir)

#pull out sim names only, and make list of unique sim names
problemSims=[tup[0] for tup in problemChildren]
uniqProblemSims = []
for sim in problemSims:
	simName = sim.split("_")[0]+"_"+sim.split("_")[1]
	if simName not in uniqProblemSims:
		uniqProblemSims.append(simName)



with open('problemChildren.txt', 'w') as fp:
		fp.write('\n'.join(uniqProblemSims))
					

