#!/bin/bash

echo "file	999th_1000q_lower_p	999th_1000q_upper_p	999th_1000q_two_p	99th_100q_lower_p	99th_100q_upper_p	99th_100q_two_p	3rd_4q_lower_p	3rd_4q_upper_p	3rd_4q_two_p	2nd_4q_lower_p	2nd_4q_upper_p	2nd_4q_two_p	1st_4q_lower_p	1st_4q_upper_p		1st_4q_two_p	1st_6q_lower_p	1st_6q_upper_p	1st_6q_two_p	1st_8q_lower_p	1st_8q_upper_p	1st_8q_two_p	1st_10q_lower_p	1st_10q_upper_p	1st_10q_two_p	1st_20q_lower_p	1st_20q_upper_p	1st_20q_two_p	1st_100q_lower_p	1st_100q_upper_p	1st_100q_two_p	1st_1000q_lower_p	1st_1000q_upper_p	1st_1000q_two_p	IQRange_lower	IQRange_upper	IQRange_two	meanTL_lower	meanTL_upper	meanTL_two	TLvar_lower	TLvar_upper	TLvar_two" > amp.pVal.tab		

for f in *.out
do
p999_1000low=`grep -m 1 "Lower One-tailed P-value:" $f | awk '{print $4}'`
p999_1000up=`grep -m 1 "Upper One-tailed P-value:" $f | awk '{print $4}'`
p999_1000two=`grep -m 1 "Two-tailed P-value:" $f | awk '{print $3}'`
p99_100low=`grep -m 2 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p99_100up=`grep -m 2 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p99_100two=`grep -m 2 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p3_4low=`grep -m 3 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p3_4up=`grep -m 3 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p3_4two=`grep -m 3 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p2_4low=`grep -m 4 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p2_4up=`grep -m 4 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p2_4two=`grep -m 4 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p1_4low=`grep -m 5 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_4up=`grep -m 5 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_4two=`grep -m 5 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p1_6low=`grep -m 6 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_6up=`grep -m 6 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_6two=`grep -m 6 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p1_8low=`grep -m 7 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_8up=`grep -m 7 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_8two=`grep -m 7 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p1_10low=`grep -m 8 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_10up=`grep -m 8 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_10two=`grep -m 8 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p1_20low=`grep -m 9 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_20up=`grep -m 9 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_20two=`grep -m 9 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p1_100low=`grep -m 10 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_100up=`grep -m 10 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_100two=`grep -m 10 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p1_1000low=`grep -m 11 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_1000up=`grep -m 11 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_1000two=`grep -m 11 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
IQRange_low=`grep -m 12 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
IQRange_up=`grep -m 12 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
IQRange_two=`grep -m 12 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
meanTL_low=`grep -m 13 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
meanTL_up=`grep -m 13 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
meanTL_two=`grep -m 13 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
TLvar_low=`grep -m 14 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
TLvar_up=`grep -m 14 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
TLvar_two=`grep -m 14 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
echo $f	$p999_1000low	$p999_1000up	$p999_1000two	$p99_100low	$p99_100up	$p99_100two	$p3_4low	$p3_4up	$p3_4two	$p2_4low	$p2_4up	$p2_4two	$p1_4low	$p1_4up	$p1_4two	$p1_6low	$p1_6up	$p1_6two	$p1_8low	$p1_8up	$p1_8two	$p1_10low	$p1_10up	$p1_10two	$p1_20low	$p1_20up	$p1_20two	$p1_100low	$p1_100up	$p1_100two	$p1_1000low	$p1_1000up	$p1_1000two	$IQRange_low	$IQRange_up	$IQRange_two	$meanTL_low	$meanTL_up	$meanTL_two	$TLvar_low	$TLvar_up	$TLvar_two >> amp.pVal.tab
done

