#!/bin/bash
for f in *_mstxrm.trees
do 
gene=`basename $f _mstxrm.trees`
outFile1=$gene'_conSumt0.5.t'
outFile2=$gene'_mcctSumt0.5.t'

echo $gene

sumtrees.py -s consensus --min-clade-freq=0.5 --edges mean-length --burnin=0 --support-as-labels --output=$outFile1 $f

echo $outFile1

sumtrees.py -s mcct --min-clade-freq=0.5 --edges mean-length --burnin=0 --support-as-labels --output=$outFile2 $f

echo $outFile2

done


