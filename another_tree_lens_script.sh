#!/bin/bash

output=`touch tree_lens_output`
for f in squamg_*;
do
cd $f
echo $f
best_run=`tail -n 2 *run*screen.log | awk '{print $8}' | awk -F'#' '{ print $2}' | awk -F')' '{ print $1}'`
echo $best_run
if [ ${#best_run} == 2 ]
then
best_len=`cat *screen.log | sed "1,/^\s*TL/d" | grep "^rep" | grep "^rep$best_run"`
else
best_len=`cat *screen.log | sed "1,/^\s*TL/d" | grep "^rep" | grep -e "^rep $best_run"`
fi
echo $best_len
echo $f':'$best_len >> ../$output
all_run_len=`cat *screen.log | sed "1,/^\s*TL/d" | grep "^rep"`
rm *.all_run_lens
touch $f'.all_run_lens'
echo $all_run_len >> *.all_run_lens
cd ../
done

_____________last version______________

#!/bin/bash

output=`touch tree_lens_output`
for f in squamg_*;
do
cd $f
echo $f
best_run=`tail -n 2 *run*screen.log | awk '{print $8}' | awk -F'#' '{ print $2}' | awk -F')' '{ print $1}'`
echo 'best run is $best_run'
if [ "$best_run" == "10" ]
then
best_len=`cat *screen.log | sed "1,/^\s*TL/d" | grep "^rep" | grep "^rep$best_run"`
else
best_len=`cat *screen.log | sed "1,/^\s*TL/d" | grep "^rep" | grep -e "^rep $best_run"`
fi
echo 'length $best_len'
echo $f':'$best_len >> ../$output
all_run_len=`cat *screen.log | sed "1,/^\s*TL/d" | grep "^rep"`
rm *.all_run_lens
touch $f'.all_run_lens'
echo $f^$all_run_len >> *.all_run_lens
cd ../
done


