#!/bin/bash


#for lines in file, extract directory, extract part from directory, if that part matches a line in one file, add it to file. 
for f in $(cat empDataList)
do dirN=`dirname $f`
gene=`echo $dirN | awk -F'/' '{print $5}'`

if grep -Fxq $gene short.txt
then
echo $f >> empDataListS
fi

if grep -Fxq $gene long.txt
then
echo $f >> empDataListL
fi

done




# squamg_GENE.nex > GENE.nex
for f in *.nex; 
do
gene=`echo $f | awk -F'_' '{ print $2}' |  awk -F'.' '{ print $1}' ` 
echo $gene
touch $gene'.nex'
cp $f $gene'.nex'
done

#collect jmodg files
mkdir jmodg_files
for f in squamg_*
do 
cd $f
cp jmodg_squamg* ../jmodg_files
cd ../
done

###Folder= file of jmod output files named jmodg_squamg_GENE
#add GTR+G for concat file seperate
rm 'jmod_table.txt'
touch 'jmod_table.txt'
out='jmod_table.txt'
for f in jmodg_*; 
do
gene=`echo $f | awk -F'_' '{ print $3}'` 
nfname=$gene'.nex'
model=`tail -n 1 jmodg_squamg_$gene | awk '{print $2}'`
echo -e $nfname'\t'$model >> $out
done

# iterate check files for a keyword and output all lines and file name
for f in *.log; 
do
gene=`echo $f | awk -F'_' '{ print $1}' `
echo $gene
x=`cat $f | grep "lnL"`
echo $x
done

for f in *clockLH.log; 
do
gene=`echo $f | awk -F'_' '{ print $1}' `
echo $gene
x=`cat $f`
echo $x
done


for f in *_graph.png;
do 
gene=`echo $f | awk -F'_' '{ print $1}'` 
newf=$gene'_prunedog.05.15.15.png'
mv $f $newf 
done

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


#remove folders correlating to .nex files
for f in *.nex; 
do
gene=`echo $f | awk -F'.' '{ print $1}' `
echo $gene
rm -rf $gene
done