#!/bin/bash
for f in *.t
do 
gene=`basename $f .t`
outFile1=$gene'_conSumt0.5.t'
outFile2=$gene'_mcctSumt0.5.t'

echo $gene

sumtrees.py -s consensus --min-clade-freq=0.5 --edges mean-length --burnin=0 --support-as-labels --output=$outFile1 $f

echo $outFile1

sumtrees.py -s mcct --min-clade-freq=0.5 --edges mean-length --burnin=0 --support-as-labels --output=$outFile2 $f

echo $outFile2

done


sumtrees.py -s consensus --min-clade-freq=0.5 --edges mean-length --burnin=0 --support-as-labels --output=unordered_conSumt0.5.t unordered.nex.run1.t unordered.nex.run2.t unordered.nex.run3.t unordered.nex.run3.t
sumtrees.py -s mcct --min-clade-freq=0.5 --edges mean-length --burnin=0 --support-as-labels --output=unordered_mcctSumt0.5.t unordered.nex.run1.t unordered.nex.run2.t unordered.nex.run3.t unordered.nex.run3.t