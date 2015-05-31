# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:19:44 2015

@author: ChatNoir

help from -https://mail.python.org/pipermail/tutor/2013-February/093702.html 

put script in directory 
"""
from __future__ import division
import os


def list_missing(fname):
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[1] #split name by .then by _  
    outname=gene+"_missingtaxa.txt" #create outfile
    outF=open(outname, 'w+')  #open outfile
    qmarks='?????' #id target seq
    bps=['AT','AC','AG','AA', 'CA', 'CG', 'CT', 'CC', 'GA', 'GC', 'GG', 'GT', 'TA', 'TC', 'TG', 'TT'] #using pairs to avoid IDing first letter in Genus name
    with open(fname,'r') as inF: #open infile
        for index, line in enumerate(inF): #iterate lines in file
            if qmarks in line: #if q marks
                if any(bp in line for bp in bps): #if also bps in line, print line
                    print line
                else: #otherwise add line with only ?? to file
                    outF.write(line)
    outF.close()

folder='/Users/ChatNoir/bin/Squam/data_files/clocklikepaup'
for fn in os.listdir(folder): 
    if fn.endswith(".nex"):        
        list_missing(fn)
        
        
        