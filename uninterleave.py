#! /usr/bin/env python
###Splits RevBayes pp .log files into separate run files. need to edit if you have different number of runs. 
import os
import glob

#make sure you are in directory that you are calling script from 
maindir = os.getcwd()
os.chdir(maindir)

#iterate through gene folders, need to have some handle to iterate through these. could be *.nex
for g in glob.glob('*.4'):
	#split off locus name, dependant on what your iterating handle files are
	gene = g.split(".")[0]
	#move into output folder for locus
	pathname = os.path.join(gene,"output/")
	os.chdir(pathname)
	#1 gene/output
	print os.getcwd()
	for p in glob.glob('posterior_predictive_sim_*'):
		#2 ppsim#
		print p
		#2.5 gene/output folder
		print os.getcwd()
		os.chdir(p)
		#3 ppsim#path
		print os.getcwd()
		with open(gene + "_posterior.log") as flog:

			f1=open(gene + '_posterior_run_1.log', 'w')
			f2=open(gene + '_posterior_run_2.log', 'w')
			f3=open(gene + '_posterior_run_3.log', 'w')
			f4=open(gene + '_posterior_run_4.log', 'w')
			f1.write(flog.readline())
			f1.write(flog.readline())
			f2.write(flog.readline())
			f2.write(flog.readline())
			f3.write(flog.readline())
			f3.write(flog.readline())
			f4.write(flog.readline())
			f4.write(flog.readline())
			
			x=0

			for line in flog.readlines():
				if x==0:
					f1.write(line)
					x+=1
				elif x==1:
					f2.write(line)
					x+=1
				elif x==2:
					f3.write(line)
					x+=1		
				elif x==3:
					f4.write(line)
					x=0
			f1.close()
			f2.close()
			f3.close()
			f4.close()

		with open(gene + "_posterior.trees") as ftrees:

			t1=open(gene + '_posterior_run_1.trees', 'w')
			t2=open(gene + '_posterior_run_2.trees', 'w')
			t3=open(gene + '_posterior_run_3.trees', 'w')
			t4=open(gene + '_posterior_run_4.trees', 'w')
			t1.write(ftrees.readline())
			t1.write(ftrees.readline())
			t2.write(ftrees.readline())
			t2.write(ftrees.readline())
			t3.write(ftrees.readline())
			t3.write(ftrees.readline())
			t4.write(ftrees.readline())
			t4.write(ftrees.readline())
			
			x=0

			for line in ftrees.readlines():
				if x==0:
					t1.write(line)
					x+=1
				elif x==1:
					t2.write(line)
					x+=1
				elif x==2:
					t3.write(line)
					x+=1		
				elif x==3:
					t4.write(line)
					x=0
			t1.close()
			t2.close()
			t3.close()
			t4.close()
		os.chdir('../')
		#4 gene folder
		print os.getcwd()
	os.chdir(maindir)

####
# would like to add sectiont to rename all runs by sim number and put in a single folder for easier access. 
# this function is currently in a bash script