
#creates qsub for each gene
for f in *.nex; 
do
base=`basename $f .nex`
gene=`echo $base | awk -F'_' '{ print $2}'` #split file name by _ and take the second part
cd $base
echo $base
cp ../qsub_garli_squam_20_genename 'qsub_garli_squam_20_'$gene #copy qsub file into folder
qsub='qsub_garli_squam_20_'$gene # replace genename with appropriate gene name
sed -i.tmp "s/genename/$gene/g" $qsub
rm *.tmp
cd ../
done

#to run qsub files 
for f in squamg_*;
do
base=`basename $f .nex`
cd $base
qsub qsub_garli_squam_20_*
cd ../
done

#to remove qsub files
for f in *.nex; 
do
base=`basename $f .nex`
cd $base
echo $base
rm qsub*
cd ../
done


