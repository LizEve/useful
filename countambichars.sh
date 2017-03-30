#Requires *gene*_misstxremoved.nex files
#Also in randomScripts.sh
out='ambiData.txt'
for f in *misstxremoved.nex;
do
q=`grep -o "?" $f | wc -l`
d=`grep -o "-" $f | wc -l`
x=$[q+d]
echo $x
gene=`echo $f | awk -F'_' '{ print $1}' `
echo -e $gene"\t"$x >> $out
done
