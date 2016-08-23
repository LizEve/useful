mkdir compare
mkdir comp
cd output/
basef="AHR"
for f in posterior_predictive_sim_*;
do 
#pull out simulation number
num=`echo $f | awk -F '_' '{print $4}'`
#echo $num
#pull from run folder and rename as gene_number.t
#cp $f/$basef"_posterior.trees" ../ampWorkDir/$basef"_"$num".t"
#if your runs didnt all finish and you need to standardize the lenght of the files use this
head -n 2100 $f/$basef"_posterior.trees" > ../compare/$basef"_"$num".t"
done


/Users/ChatNoir/Projects/Squam/RevBayes/rbcluster_download/CXCR4

cd CXCR4
mkdir sim_compare
basef="CXCR4"
cd output/CXCR4_post_sims
for f in posterior_predictive_sim_*;
do 
#pull out simulation number
num=`echo $f | awk -F '_' '{print $4}'`
cd $f
for x in *.nex;
do
cp $x ../../../sim_compare/$basef"_"$num"_"$x
done
cd ../
done
cd ../../



for f in *.t;
do
diff -qs $f ../comp/CXCR4_1.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_10.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_100.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_101.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_102.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_103.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_104.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_105.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_106.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_107.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_108.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_109.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_11.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_110.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_111.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_112.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_113.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_114.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_115.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_116.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_117.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_118.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_119.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_12.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_120.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_121.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_122.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_123.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_124.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_125.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_126.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_127.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_128.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_129.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_13.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_130.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_131.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_132.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_133.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_134.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_135.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_136.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_137.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_138.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_139.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_14.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_140.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_141.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_142.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_143.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_144.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_15.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_16.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_17.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_18.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_19.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_2.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_20.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_21.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_22.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_23.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_24.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_25.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_26.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_27.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_28.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_29.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_3.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_30.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_31.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_32.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_33.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_34.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_35.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_36.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_37.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_38.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_39.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_4.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_40.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_41.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_42.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_43.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_44.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_45.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_46.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_47.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_48.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_49.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_5.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_50.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_51.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_52.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_53.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_54.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_55.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_56.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_57.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_58.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_59.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_6.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_60.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_61.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_62.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_63.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_64.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_65.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_66.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_67.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_68.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_69.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_7.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_70.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_71.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_72.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_73.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_74.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_75.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_76.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_77.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_78.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_79.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_8.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_80.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_81.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_82.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_83.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_84.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_85.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_86.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_87.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_88.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_89.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_9.t | grep identical >> CXCR4_comp.txt 
diff -qs $f ../comp/CXCR4_90.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_91.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_92.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_93.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_94.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_95.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_96.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_97.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_98.t | grep identical >> CXCR4_comp.txt
diff -qs $f ../comp/CXCR4_99.t | grep identical >> CXCR4_comp.txt
done