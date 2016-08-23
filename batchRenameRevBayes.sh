#!/bin/bash

##Usage:
## run in folder containing gene.nex and gene/ and convertToNexus.py
## This script is currently setup to assume there are four replicate runs for each emperical run.
## burninSamples should be the number of printed lines that are burning in your simulated run. 
## the emperical run will already have burnin removed.
## the resulting files should have the following format
##  <basename>_<treefile#>_<rep#>.t, 
##  <basename>_emp_<rep#>.t  

#if [ $1 == "help" ]
#then
#	echo "usage: batchRenameRevBayes.sh subsamplingRateSim subsamplingRateEmp burninSamples+1forheader"
#fi
 
#if [ $1 != "help" ]
#then

# for sim data. doing sim data renaming and subsampling first. 
# emperical data may have a different number of generations than sim. therefore needs a differents subsamplign rate. 
# move into output file for each gene
for f in *.nex 
do
basef=`basename $f .nex`
cd ./$basef
mkdir ampWorkDir
cd ./output
echo $basef" - sim"
#rename files and put them into ampWorkDir folder
for f in posterior_predictive_sim_*;
do 
#pull out simulation number
num=`echo $f | awk -F '_' '{print $4}'`
#echo $num
#pull from run folder and rename as gene_number.t
#cp $f/$basef"_posterior.trees" ../ampWorkDir/$basef"_"$num".t"
#if your runs didnt all finish and you need to standardize the lenght of the files use this
head -n 1002 $f/$basef"_posterior.trees" > ../ampWorkDir/$basef"_"$num".t"
done
#move back into base folder
cd ../../
done

# sim, move into ampWorkDir for each gene and print out only column with newick string
for g in *.nex 
do
baseg=`basename $g .nex`
cd ./$baseg/ampWorkDir
touch to_nexus.txt
for t in *.t;
do
sed '/Iteration/d' $t > $t".tmp"
awk '{print $5}' $t".tmp" > $t
rm *.tmp
done
echo $baseg" sim - newick"


# subsample sim files and convert to nexus
for t in *.t;
do
#header=151
#use x if you are testing script and dont have an user input value
#x=8
#awk '{if (((count++)-'$header')%'$x'==0 && (count)-'$header'>0) print $0;}' $t >> $t"_sub"
#subsample trees in file
awk '{if (((count++)-'$3')%'$1'==0 && (count)-'$3'>0) print $0;}' $t >> $t"_sub"
#move unsampled file to _full and rename subsampled file as original
mv $t $t"_full"
mv $t"_sub" $t
# make a list of files that need to be converted to nexus
echo $t >> 'to_nexus.txt'
done
echo $basef" sim - subsampled"
#convert to nexus
cp ../../convertToNexus.py .
for a in $(cat "to_nexus.txt");
do
./convertToNexus.py $a
done
rm "to_nexus.txt"
cd ../../
done

#emperical file batch rename
for j in *.nex
do
basej=`basename $j .nex`
cd $basej
echo $basej" - emp"
cd output
#cp $basej"_posterior.trees" ../ampWorkDir/$basej"_emp.t"
#if you need to standardize normalize the lenght of the files use this
head -n 1002 cp $basej"_posterior.trees" > ../ampWorkDir/$basej"_emp.t"
cd ../../
done

#emperical change from extended to normal newick and subsample
for k in *.nex 
do
basek=`basename $k .nex`
cd ./$basek/ampWorkDir
for e in *_emp.t;
do
sed '/Iteration/d' $e > $e".tmp"
awk '{print $5}' $e".tmp" > $e
rm *.tmp
#header=151
#use x if you are testing script and dont have an user input value
#x=30
#awk '{if (((count++)-'$header')%'$x'==0 && (count)-'$header'>0) print $0;}' $e >> $e"_sub"
#subsample trees in file
awk '{if (((count++)-'$3')%'$2'==0 && (count)-'$3'>0) print $0;}' $e >> $e"_sub"
#move unsampled file to _old and rename subsampled file as original
mv $e $e"_full"
mv $e"_sub" $e
./convertToNexus.py $e
#optional clean up
rm convertToNexus.py
mkdir temp
mv *_r1.t temp
rm *.t 
rm *_full
mv temp/* .
rm -rf temp/

cd ../../
done
echo $basek" emp- newick"
done
#fi

#for t in *.t; do; mv $t"_old" $t; done

