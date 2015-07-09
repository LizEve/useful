#!/bin/bash
outfile="all_clocklike_misstxremoved_prunedog.txt"
echo "gene delete Δ-lnL ΔAICc ΔBIC" >> $outfile
for f in *clockLH.log; 
do
gene=`echo $f | awk -F'_' '{ print $1}' `
want=`cat $f | awk -F',' '{ print $4}'`
#echo $want
#temp="$gene.temp"
echo $gene' '$want >> $outfile
#rm $temp
done


#f="athena_misstxremoved_clockLH_cat.log"
#read table sep=\s