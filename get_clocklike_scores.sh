#!/bin/bash
#created a CSV files from paup output. 


for f in *.log; 
do
suffix="_misstxremoved_clockLH.log"
gene=`echo $f | awk -F'_' '{ print $1}' `
base=`echo $f | awk -F'.' '{ print $1}' `
outfile=$gene$suffix
cat $f | grep 'criterion' | awk '{print $4","$5","$6","$7}' >> $outfile
#get columns 4,5,6,7 from line with "criterion" and add commas inbetween
cat $f | grep 'lnL' | awk '{print $4","$5","$6","$7}' >> $outfile
cat $f | grep 'AICc' | awk '{print $1","$2","$3","$4}' >> $outfile
cat $f | grep 'BIC'| awk '{print $1","$2","$3","$4}' >> $outfile
done
#rm *clockLH.log

#cp ~/bin/Squam/scripts/get_clocklike_scores.sh .






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
##tail -n 12 $f | head -n 6 >> $outfile
#done

