#!/bin/bash
#simple find num occurances of word in file
#in this case finding number of times sp names occurs in file
x=`cat weins_taxa.txt`
for l in $x
do
name=`echo $l`
num=`grep -o $l listofmissingtaxa.txt | wc -l`
echo $name':'$num >> taxa_missing.txt
done
