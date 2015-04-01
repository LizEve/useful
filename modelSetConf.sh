#!/bin/bash

###USAGE: You need a base directory that contains all of your nexus files
### and a template garli.conf file in order for this script to work.
### There should also be a separate subdirectory for each nexus file with the jmod file IN the subfile
### make sure there are no other nexus files in your directory

for f in *.nex; 
do
base=`basename $f .nex`
cd $base
echo $base
rm *garli.conf
cp ../garli.conf .
nex=$base".nex"
model=`tail -n 1 jmodg* | awk '{print $2}'`
echo $model 
ratematrix=`echo $model | awk -F'+' '{ print $1}'`
echo "rate matrix is $ratematrix"
modelp2=`echo $model | awk -F'+' '{ print $2}'`
echo "model part 2 is $modelp2"
modelp3=`echo $model | awk -F'+' '{ print $3}'`
echo "$modelp3"
numberModels=`grep '\[model.\]' garli.conf | wc -l`
echo "The number of models in your .conf file is $numberModels"
if [ "$numberModels" -gt 1 ]
then
echo "It looks like your starting .conf file has too many models specified."
echo "This script does not deal with partitioned data.  One model per nexus file, please."
echo "Remove additional models from your .conf file and run this script again."
exit 1
fi	
cp garli.conf $base".garli.conf"
rm garli.conf
conf=$base".garli.conf"
sed -i.tmp "s/datafname = .*/datafname = $nex/" $conf 
sed -i.tmp "s/constraintfile = .*/constraintfile = none/" $conf 
sed -i.tmp "s/ofprefix = .*/ofprefix = $base/" $conf
sed -i.tmp "s/outputphyliptree = .*/outputphyliptree = 1/" $conf
if [ "$ratematrix" == "GTR" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = 6rate/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf
elif [ "$ratematrix" == "SYM" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = 6rate/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf
elif [ "$ratematrix" == "JC" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = 1rate/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf
elif [ "$ratematrix" == "F81" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = 1rate/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf
elif [ "$ratematrix" == "K80" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = 2rate/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf
elif [ "$ratematrix" == "HKY" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = 2rate/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf
elif [ "$ratematrix" == "TrNef" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 0 0 2 0)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf
elif [ "$ratematrix" == "TrN" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 0 0 2 0)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf
elif [ "$ratematrix" == "TPM1" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 2 1 0)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf
elif [ "$ratematrix" == "TPM1uf" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 2 1 0)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf
elif [ "$ratematrix" == "TPM2" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 0 2 1 2)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf		
elif [ "$ratematrix" == "TPM2uf" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 0 2 1 2)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf
elif [ "$ratematrix" == "TPM3" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 0 1 2)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf		
elif [ "$ratematrix" == "TPM3uf" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 0 1 2)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf
elif [ "$ratematrix" == "TIM1" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 2 3 0)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf		
elif [ "$ratematrix" == "TIM1ef" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 2 3 0)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf
elif [ "$ratematrix" == "TIM2" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 0 2 3 2)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf				
elif [ "$ratematrix" == "TIM2ef" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 0 2 3 2)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf
elif [ "$ratematrix" == "TIM3" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 0 3 2)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf			
elif [ "$ratematrix" == "TIM3ef" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 0 3 2)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf	
elif [ "$ratematrix" == "TVM" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 3 1 4)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = estimate/" $conf		
elif [ "$ratematrix" == "TVMef" ]
then
	sed -i.tmp "s/ratematrix = .*/ratematrix = (0 1 2 3 1 4)/" $conf
	sed -i.tmp "s/statefrequencies = .*/statefrequencies = equal/" $conf
fi
if [ -z "$modelp2" ]
then
	echo "only one thing to change"
	sed -i.tmp "s/ratehetmodel = .*/ratehetmodel = none/" $conf
	sed -i.tmp "s/numratecats = .*/numratecats = 1/" $conf
	sed -i.tmp "s/invariantsites = .*/invariantsites = none/" $conf
elif [ "$modelp2" == "I" ]
then 
	sed -i.tmp "s/invariantsites = .*/invariantsites = estimate/" $conf
elif [ "$modelp2" == "G" ]
then
	sed -i.tmp "s/ratehetmodel = .*/ratehetmodel = gamma/" $conf
	sed -i.tmp "s/numratecats = .*/numratecats = 4/" $conf
	sed -i.tmp "s/invariantsites = .*/invariantsites = none/" $conf
fi
if [[ -z "$modelp3" ]] && [[ "$modelp2" == "I" ]]
then
	sed -i.tmp "s/ratehetmodel = .*/ratehetmodel = none/" $conf
	sed -i.tmp "s/numratecats = .*/numratecats = 1/" $conf
elif [[ "$modelp3" == "G" ]]
then 
	sed -i.tmp "s/ratehetmodel = .*/ratehetmodel = gamma/" $conf
	sed -i.tmp "s/numratecats = .*/numratecats = 4/" $conf
fi
sed -n '34,40 p' $conf
echo ""
echo ""
rm *.tmp
cd ../
done

