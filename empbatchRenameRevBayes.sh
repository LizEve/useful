#!/bin/bash
mkdir empTrees
#emperical file batch rename
for j in *.nex
do
basej=`basename $j .nex`
cd $basej
mkdir ../empTrees/$basej"_empTree"
echo $basej" - emp"
cd output
cp $basej"_posterior.trees" ../../empTrees/$basej"_empTree/"$basej"_emp.t"
#if you need to standardize normalize the lenght of the files use this
#head -n 1002 cp $basej"_posterior.trees" > ../ampWorkDir/$basej"_emp.t"
cd ../../
done

#emperical change from extended to normal newick, subsample
for k in *.nex 
do
basek=`basename $k .nex`
cd ./empTrees/$basek"_empTree/"
for e in *_emp.t;
do
sed '/Iteration/d' $e > $e".tmp"
awk '{print $5}' $e".tmp" > $e
rm *.tmp
header=1
#use x if you are testing script and dont have an user input value
x=60
awk '{if (((count++)-'$header')%'$x'==0 && (count)-'$header'>0) print $0;}' $e >> $e"_sub"
#subsample trees in file
#awk '{if (((count++)-'$3')%'$2'==0 && (count)-'$3'>0) print $0;}' $e >> $e"_sub"
#move unsampled file to _old and rename subsampled file as original
mv $e $e"_full"
mv $e"_sub" $e
done
cd ../../
done


for t in *.nex 
do
baset=`basename $t .nex`
cd ./empTrees/$baset"_empTree/"
cp ../../mstx/$baset"_mstx.txt" .
cp ../../empconvertToNexus.py .
e=$baset"_emp.t"
./empconvertToNexus.py $e
#optional clean up
rm empconvertToNexus.py
cd ../../
done

