#!/bin/bash

#create nexus files with seq data, tree, and paup block for clocklike testing

for f in *.phy;
do
suffix="_clockchrk_misstxremoved.nex"
gene=`echo $f | awk -F'_' '{ print $1}' `
naked_tree=`cat $f`
temp_tree=$gene".temp"
touch $temp_tree
echo -e "\n\nbegin trees;\n" >> $temp_tree
echo -e "tree "$gene" = [&U] "$naked_tree >> $temp_tree
echo -e "\nend;" >> $temp_tree
seq=$base".nex"
outfile=$gene$suffix
cat $seq $temp_tree >> $outfile
echo -e "\n\nbegin paup;\n\noutGroup Homo_sapiens;\nRootTrees;\nlset nst=6 basefreq=empirical rates=gamma;\nclockchecker;\n\nend;" >> $outfile
rm $temp_tree
done
#rm *_clockchrk_misstxremoved.nex

