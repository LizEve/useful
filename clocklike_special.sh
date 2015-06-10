#!/bin/bash

#create nexus files with seq data, tree, and paup block for clocklike testing
#edits files missing outgroup

for f in *.phy;
do
suffix="_clockchrk_misstxremoved.nex"
gene=`echo $f | awk -F'_' '{ print $1}' `
base=`echo $f | awk -F'.' '{ print $1}' `
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
#rm *_clockchrk_*

rm GALR1_clockchrk_*
rm SINCAIP_clockchrk_*

f=SINCAIP_misstxremoved.phy
suffix="_clockchrk_misstxremoved.nex"
base=`echo $f | awk -F'.' '{ print $1}' `
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
echo -e "\n\nbegin paup;\n\noutGroup Tachyglossus_aculeatus;\nRootTrees;\nlset nst=6 basefreq=empirical rates=gamma;\nclockchecker;\n\nend;" >> $outfile
rm $temp_tree



f=GALR1_misstxremoved.phy 
gene=`echo $f | awk -F'_' '{ print $1}' `
naked_tree=`cat $f`
temp_tree=$gene".temp"
touch $temp_tree
echo -e "\n\nbegin trees;\n" >> $temp_tree
echo -e "tree "$gene" = [&U] "$naked_tree >> $temp_tree
echo -e "\nend;" >> $temp_tree
seq=$base".nex"
outfile1=$gene"_CS"$suffix
outfile2=$gene"_DN"$suffix
outfile3=$gene"_GG"$suffix
cat $seq $temp_tree >> $outfile1
cat $seq $temp_tree >> $outfile2
cat $seq $temp_tree >> $outfile3
echo -e "\n\nbegin paup;\n\noutGroup Chelydra_serpentina;\nRootTrees;\nlset nst=6 basefreq=empirical rates=gamma;\nclockchecker;\n\nend;" >> $outfile1
echo -e "\n\nbegin paup;\n\noutGroup Dromaius_novaehollandiae;\nRootTrees;\nlset nst=6 basefreq=empirical rates=gamma;\nclockchecker;\n\nend;" >> $outfile2
echo -e "\n\nbegin paup;\n\noutGroup Gallus_gallus;\nRootTrees;\nlset nst=6 basefreq=empirical rates=gamma;\nclockchecker;\n\nend;" >> $outfile3
rm $temp_tree


