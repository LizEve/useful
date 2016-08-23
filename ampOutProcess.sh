#!/bin/bash

echo "file	9999th_10000q_lower_p	9999th_10000q_upper_p	9999th_10000q_two_p	999th_1000q_lower_p	999th_1000q_upper_p	999th_1000q_two_p	99th_100q_lower_p	99th_100q_upper_p	99th_100q_two_p	3rd_4q_lower_p	3rd_4q_upper_p	3rd_4q_two_p	2nd_4q_lower_p	2nd_4q_upper_p	2nd_4q_two_p	1st_4q_lower_p	1st_4q_upper_p		1st_4q_two_p	entropy_lower	entropy_upper	entropy_two	IQRange_lower	IQRange_upper	IQRange_two	meanTL_lower	meanTL_upper	meanTL_two	TLvar_lower	TLvar_upper	TLvar_two" > amp.pVal.tab		

for f in *.out
do
p9999_10000low=`grep -m 1 "Lower One-tailed P-value:" $f | awk '{print $4}'`
p9999_10000up=`grep -m 1 "Upper One-tailed P-value:" $f | awk '{print $4}'`
p9999_10000two=`grep -m 1 "Two-tailed P-value:" $f | awk '{print $3}'`
p999_1000low=`grep -m 2 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p999_1000up=`grep -m 2 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p999_1000two=`grep -m 2 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p99_100low=`grep -m 3 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p99_100up=`grep -m 3 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p99_100two=`grep -m 3 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p3_4low=`grep -m 4 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p3_4up=`grep -m 4 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p3_4two=`grep -m 4 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p2_4low=`grep -m 5 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p2_4up=`grep -m 5 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p2_4two=`grep -m 5 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
p1_4low=`grep -m 6 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_4up=`grep -m 6 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
p1_4two=`grep -m 6 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
entropy_low=`grep -m 7 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
entropy_up=`grep -m 7 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
entropy_two=`grep -m 7 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
IQRange_low=`grep -m 8 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
IQRange_up=`grep -m 8 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
IQRange_two=`grep -m 8 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
meanTL_low=`grep -m 9 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
meanTL_up=`grep -m 9 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
meanTL_two=`grep -m 9 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
TLvar_low=`grep -m 10 "Lower One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
TLvar_up=`grep -m 10 "Upper One-tailed P-value:" $f | tail -n 1 | awk '{print $4}'`
TLvar_two=`grep -m 10 "Two-tailed P-value:" $f | tail -n 1 | awk '{print $3}'`
echo $f	$p9999_10000low	$p9999_10000up	$p9999_10000two	$p999_1000low	$p999_1000up	$p999_1000two	$p99_100low	$p99_100up	$p99_100two	$p3_4low	$p3_4up	$p3_4two	$p2_4low	$p2_4up	$p2_4two	$p1_4low	$p1_4up	$p1_4two	$entropy_low	$entropy_up	$entropy_two	$IQRange_low	$IQRange_up	$IQRange_two	$meanTL_low	$meanTL_up	$meanTL_two	$TLvar_low	$TLvar_up	$TLvar_two >> amp.pVal.tab
done

