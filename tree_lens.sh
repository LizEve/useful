#!/bin/bash
#May 1st 2015 GGM


-----------only best trees------------
outfile='tree_lens_output'
for f in squamg_*;
do
cd $f
best_run=`tail -n 2 *run*screen.log | awk '{print $8}' | awk -F'#' '{ print $2}' | awk -F')' '{ print $1}'`
if [ ${#best_run} == 2 ]
then
best_len=`cat *screen.log | sed "1,/Treelengths:/d" | grep "^rep" | grep "^rep$best_run"`
else
best_len=`cat *screen.log | sed "1,/Treelengths:/d" | grep "^rep" | grep -e "^rep $best_run"`
fi
echo $f:$best_len
echo $f':'$best_len >> ../$outfile
cd ../
done


_____________TREE LENS_________________
outfile='tree_lens_output'
for f in squamg_*;
do
cd $f
best_run=`tail -n 2 *run*screen.log | awk '{print $8}' | awk -F'#' '{ print $2}' | awk -F')' '{ print $1}'`
if [ ${#best_run} == 2 ]
then
best_len=`cat *screen.log | sed "1,/Treelengths:/d" | grep "^rep" | grep "^rep$best_run"`
else
best_len=`cat *screen.log | sed "1,/Treelengths:/d" | grep "^rep" | grep -e "^rep $best_run"`
fi
echo $f:$best_len
echo $f':'$best_len >> ../$outfile
all_run_len=`cat *screen.log | sed "1,/Treelengths:/d" | grep "^rep"`
rm *.all_run_lens
touch $f'.all_run_lens'
echo $all_run_len >> *.all_run_lens
cd ../
done




_________________LH_______________________
touch LH_output
outfile='LH_output'
for f in squamg_*;
do
cd $f
best_run=`tail -n 2 *run*screen.log | awk '{print $8}' | awk -F'#' '{ print $2}' | awk -F')' '{ print $1}'`
best_LH=`cat *screen.log | sed "1,/Results:/d" | grep "^Replicate" | grep -e "^Replicate $best_run"`
echo $f:$best_LH
echo $f':'$best_LH >> ../$outfile
all_LHs=`cat *screen.log | sed "1,/Results:/d" | grep "^Replicate"`
rm *.LHs
touch $f'.LHs'
echo $all_LHs >> *.LHs
cd ../
done

________OTHER___________

#put all runs for all genes together
touch all_re_run_lenssss
for f in squamg_*;
do
cd $f
x=`cat *.all_run_lens`
echo $f:$x >> ../all_re_run_lenssss
cd ../
done


