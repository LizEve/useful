#!/bin/bash
#May 19th 2015 GGM
#for each nexus gene file:
#	for each line in file:
#		if line contains 50+???
#			copy line >> GENE_missingtaxa.temp
#take temp files and parse by tab (if that is what is between the name and ???, then spit out a list of just the names, with gene name on top of list(?))

for f in *.nex
do
base=`basename $f`
cp mrc.conblock $f
cp MrConverge1b2.5.jar $f
sed -i.tmp "s/set filename=data/set filename=$base/g" $f"mrc.conblock"
done

for n in $(cat empDataDirectories)
do
cd $n
	count=1

	for f in *.t
	do
	baseT=`basename $f .nex.run$count.t`
	echo $f $baseT
	cp $f $baseT"_r"$count".t"
	((count ++))
	done

	count=1

	for g in *.p
	do
	baseP=`basename $g .nex.run$count.p`
	echo $f $baseP
	cp $g $baseP"_r"$count".p"
	((count ++))
	done
cd ../
done
