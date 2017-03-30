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
burnin = 860
#far is how many stds you want to flag for possible issues
#far = 4

######

def get_emp_values(gene,emp_file,open_out_file):
	with open(emp) as f:
		#start lists of values
		e_stat1_list = []
		e_stat2_list = []
		e_stat3_list = []
		e_stat4_list = []
		e_tl_list = []

		#skip burnin line
		for header in xrange(1):
			next(f)
		#iterate through lines, pull out param values. Append to lists. 
		for line in f:
			e_stat4 = float(line.split("\t")[-2])
			e_stat3 = float(line.split("\t")[-3])
			e_stat2 = float(line.split("\t")[-4])
			e_stat1 = float(line.split("\t")[-5])
			e_tl = float(line.split("\t")[-1])

			# add paramters to list
			e_stat1_list.append(e_stat1)
			e_stat2_list.append(e_stat2)
			e_stat3_list.append(e_stat3)
			e_stat4_list.append(e_stat4)
			e_tl_list.append(e_tl)

			# store std for each
			e_stat1_std = np.std(e_stat1_list)
			e_stat2_std = np.std(e_stat2_list)
			e_stat3_std = np.std(e_stat3_list)
			e_stat4_std = np.std(e_stat4_list)
			e_tl_std = np.std(e_tl_list)
		e_std_list = [e_stat1_std, e_stat2_std, e_stat3_std, e_stat4_std, e_tl_std]
		# write out to file
		open_out_file.write(gene + " stat1 " + str(e_stat1_std) + "\n")
		open_out_file.write(gene + " stat2 " + str(e_stat2_std) + "\n")
		open_out_file.write(gene + " stat3 " + str(e_stat3_std) + "\n")
		open_out_file.write(gene + " stat4 " + str(e_stat4_std) + "\n")
		open_out_file.write(gene + " tl " + str(e_tl_std) + "\n")
		return e_std_list

def get_sim_values(gene,emp_std_list,outputDirPath,open_out_file):
	for pps in glob.glob('posterior_predictive_sim_*'):
		#get sim num
		sim = pps.split("_")[3]
		logName = gene+'_posterior.log'
		logDirPath = os.path.join(outputDirPath,pps,logName)
		tag = gene+"_"+sim
		e_std1 = emp_std_list[0]
		e_std2 = emp_std_list[1]
		e_std3 = emp_std_list[2]
		e_std4 = emp_std_list[3]
		e_tl = emp_std_list[4]
		# open sim log file
		with open(logDirPath) as f:
			# initiate lists
			stat1List = []
			stat2List = []
			stat3List = []
			stat4List = []
			stlList = []
			#skip burnin lines
			for badline in xrange(burnin):
				next(f)
			#iterate through lines, pull out Likelihood and posterior values. Append to lists. 
			for line in f:
				s_stat4 = float(line.split("\t")[-2])
				s_stat3 = float(line.split("\t")[-3])
				s_stat2 = float(line.split("\t")[-4])
				s_stat1 = float(line.split("\t")[-5])
				s_tl = float(line.split("\t")[-1])
				
				# add paramters to list
				stat1List.append(s_stat1) 
				stat2List.append(s_stat2) 
				stat3List.append(s_stat3)
				stat4List.append(s_stat4)  
				stlList.append(s_tl) 

			# store std for each 
			s_stat4_std = np.std(stat4List)
			s_stat3_std = np.std(stat3List)
			s_stat2_std = np.std(stat2List)
			s_stat1_std = np.std(stat1List)
			s_tl_std = np.std(stlList)
		# if the std for any of these is outside one std of the emp std, print name and which value to output file
			if round(s_stat1_std, 3) > round(float(e_std1),3):
				issue = tag + " stat1 " + str(s_stat1_std) + "\n"
				open_out_file.write(issue)
			elif round(s_stat2_std, 3) > round(float(e_std2), 3):
				issue = tag + " stat2 " + str(s_stat2_std) + "\n"
				open_out_file.write(issue)
			elif round(s_stat3_std, 3) > round(float(e_std3), 3):
				issue = tag + " stat3 " + str(s_stat3_std) + "\n"
				open_out_file.write(issue)
			elif round(s_stat4_std, 3) > round(float(e_std4), 3):
				issue = tag + " stat4 " + str(s_stat4_std) + "\n"
				open_out_file.write(issue)
			elif round(s_tl_std, 3) > round(float(e_tl), 3):
				issue = tag + " TL " + str(s_tl_std) + "\n"
				open_out_file.write(issue)

#make sure you are in directory that you are calling script from 
mainDir = os.getcwd()

#open a file to write issues to
outFileDirPath = os.path.join(mainDir,'Problem_children.txt')
with open(outFileDirPath, 'w') as fp:

	#iterate through gene folders, need to have some handle to iterate through these. could be *.nex
	for g in glob.glob('*.nex'):
		#split off locus name, dependant on what your iterating handle files are
		gene = g.split(".")[0]
		print gene
		#create path to output
		outputDirPath = os.path.join(mainDir,gene, "output/")
		#move to logsdir
		os.chdir(outputDirPath)
		#open emp run and get std and mean for parameters
		emp = gene + '_posterior.log'
		#get_emp_values(gene,emp,fp)
		emp_stds = get_emp_values(gene,emp,fp)
		#iterate through sim log files. 
		get_sim_values(gene,emp_stds,outputDirPath,fp)
		linebreak = "-----------------------------" + "\n"
		fp.write(linebreak)
		#move out of folder and begin again
		os.chdir(mainDir)

