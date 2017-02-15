#!/bin/bash
#PBS -q single
#PBS -l nodes=1:ppn=1
#PBS -l walltime=03:00:00
#PBS -N ampprep
#PBS -o $PBS_JOBNAME.out
#PBS -e $PBS_JOBNAME.err
#PBS -A hpc_phyleaux08

cd /work/gmount/PP_all_RevBayes/
# run job
python uninterleave4.py

python AmpPrep.py
exit