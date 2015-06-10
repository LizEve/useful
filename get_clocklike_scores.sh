#!/bin/bash


for f in *_cat.log; 
do
suffix="_misstxremoved_clockLH.log"
f="athena_cat.log"
gene=`echo $f | awk -F'_' '{ print $1}' `
base=`echo $f | awk -F'.' '{ print $1}' `
outfile=$gene$suffix
cat $f | grep 'criterion' | awk '{print $4","$5","$6","$7}' >> $outfile
cat $f | grep 'lnL' | awk '{print $4","$5","$6","$7}' >> $outfile
cat $f | grep 'AICc' | awk '{print $1","$2","$3","$4}' >> $outfile
cat $f | grep 'BIC'| awk '{print $1","$2","$3","$4}' >> $outfile
#tail -n 12 $f | head -n 6 >> $outfile
done
#rm *clockLH.log


awk '{print $4$5$6$7}' athena_misstxremoved_clockscores.log  > new_file.log


awk '{print $3","}' athena_misstxremoved_clockscores.log  > new_file.log

athena_misstxremoved_clockscores.log




for f in *.log; 
do
gene=`echo $f | awk -F'_' '{ print $1}' `
echo $gene
x=`cat $f | grep "lnL"`
echo $x
done
#Original Script
#gives all info:  tree     times   lengths   criterion         clock     non-clock        diff        P*
#for f in *_cat.log; 
#do
#suffix="_misstxremoved_clockscores.log"
#f="athena_cat.log"
#gene=`echo $f | awk -F'_' '{ print $1}' `
#base=`echo $f | awk -F'.' '{ print $1}' `
#outfile=$gene$suffix
#cat $f | grep 'criterion'  >> $outfile
#cat $f | grep 'lnL' >> $outfile
#cat $f | grep 'AICc' >> $outfile
#cat $f | grep 'BIC' >> $outfile
#tail -n 12 $f | head -n 6 >> $outfile
#done

