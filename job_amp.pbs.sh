#!/bin/bash
#PBS -q workq
#PBS -l nodes=1:ppn=16
#PBS -l walltime=1:00:00
#PBS -N Amp
#PBS -o $PBS_JOBNAME.out
#PBS -e $PBS_JOBNAME.err
#PBS -A hpc_phyleaux08


cd /work/gmount/RevBayes/Amp/test
# run job
python2.7 ./amp0.99e1.py -q 999,1000,99,100,3,4,2,4,1,4 -e -i -T -V  -lut -o "test.amp.out" --debug --timeit --nworkers 16 -v PTGER4 119 4 > ampLog.txt

exit