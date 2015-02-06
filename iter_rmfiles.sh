#!/bin/bash
#removing a file from multiple folders
#this is finding all files that end with .nex use the basename to find folders with the basename
#then move into that folder and remove the file "1"
for f in *.nex; 
do
base=`basename $f .nex`
cd $base
rm 1
cd ../
done
