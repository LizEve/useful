#!/bin/bash
#removing a file from multiple folders
#this is finding all files that end with .nex use the basename to find folders with the basename
#then move into that folder and remove the file "1"
for f in squam*; 
do
base=`basename $f squam_`
echo $base
cd $base
rm squam*
cd ../
done



for f in squam*.nex; 
do
base=`basename $f .nex`
cd $base
echo $base
rm *.conf
cd ../
done
