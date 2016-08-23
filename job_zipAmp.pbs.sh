#!/bin/bash
#PBS -q single
#PBS -l nodes=1:ppn=1
#PBS -l walltime=2:00:00
#PBS -N tenureamp_zip2
#PBS -o $PBS_JOBNAME.out
#PBS -e $PBS_JOBNAME.err
#PBS -A hpc_phyleaux08

cd /work/gmount/PP_all_RevBayes/
# run job

cd PTGER4_amp
zip -r PTGER4_trees.zip *.trees
rm *.trees
cd ../PTPN_amp
zip -r PTPN_trees.zip *.trees
rm *.trees
cd ../R35_amp
zip -r R35_trees.zip *.trees
rm *.trees
cd ../
zip -r tenure_amp.zip PTGER4_amp PTPN_amp R35_amp

zip -r tenure_logs.zip PTGER4_logs PTPN_logs R35_logs

zip -r PTGER4_PP081816.zip PTGER4

zip -r R35_PP081816.zip R35
