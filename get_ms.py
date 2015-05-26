# -*- coding: utf-8 -*-
"""
Created on Sat May 23 20:19:44 2015

@author: ChatNoir
"""
from __future__ import division
import ast
import time

#IMPORT MS DICTIONARY
MSfp='/Users/ChatNoir/bin/Squam/data_files/matching_dist/MSdists/MS_prunedog_full.txt'
msdict={}        
     
with open(MSfp,'r') as f: #open file
    next(f) #skip the first line
    for line in f: #for the rest of the lines
        gene=line.split('\t')[0] #split by tabs, pick out gene name
        g=gene.strip() #strip whitespace from name
        ms=line.split('\t')[3] #pick out matching distance
        fms=float(ms) #float the number
        msdict[g]=fms #add gene as key and ms as number
print len(msdict.keys())     #double check number of keys in dict. should be 44
print msdict     
#IMPORT TL DICTIONARY
TL="~/bin/Squam/data_files/TLs_ofsorts/TL_prunedog.txt"   
 
def filetodict(fpath):     
    dict1={}
    for line in open(fpath,'r'):
        if line.startswith('{'):
            dict1=ast.literal_eval(line)
        return dict1         
treelen=filetodict(TL)

print len(treelen.keys())
     
#MERGE AND OUTPUT     
output_file="/Users/ChatNoir/bin/Squam/data_files/matching_dist/prunedog_MSTL.txt"

def merg_dicts(dic1,dic2):
    dic3={}
    for key in dic1:
        if key not in dic2:
            print "you are missing values for",key,"in the second dictionary"
        if key in dic2:
            val=[dic1[key],dic2[key]]
            #print vals
            dic3[key]=val
    for key in dic2:
        if key not in dic1:
            print "you are missing",key,"in the first dictionary"
    return dic3


bigd=merg_dicts(treelen,msdict)
datetime="Current date & time of run " + time.strftime("%c")



outfile=open(output_file, 'w+')
outfile.write(str(bigd))
outfile.write('\n')
outfile.write(datetime)
outfile.close()



"""

TESTING


for l in open(fp,'r'):
    line=l.strip()
    tree=line.split('\t')[0]
    ms=line.split('\t')[3]
    fms=float(ms)
    print fms
    msdict[tree]=fms
    print msdict
output_file='/Users/ChatNoir/bin/Squam/data_files/matching_dist/temp_MS_full.txt'
outfile=open(output_file, 'w+')
outfile.write(str(msdict))
outfile.close()

tmpfp='/Users/ChatNoir/bin/Squam/data_files/matching_dist/temp_MS_full.txt'


def filetodict(fpath):     
    dict1={}
    for line in open(fpath,'r'):
        if line.startswith('{'):
            dict1=ast.literal_eval(line)
        return dict1   
        
filetodict(tmpfp)
"""