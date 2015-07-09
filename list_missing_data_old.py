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

def get_taxa(fname):
    taxalist=[]
    gene=fname.split('_')[0] #get gene name
    with open(fname, 'r') as F: #open file
        for line in F:
            t=line.split('?') #split by ??
            tx=t[0]
            taxa=tx.strip()
            taxalist.append(taxa) #add to list
        return gene,taxalist


folder='/Users/ChatNoir/bin/Squam/data_files/clocklikepaup'
for fn in os.listdir(folder): 
    if fn.endswith(".nex"):        
        list_missing(fn)
        
OF=open('listofmissingtaxa.txt', 'w+')
for fn in os.listdir(folder): 
    if fn.endswith("missingtaxa.txt"):
        x=get_taxa(fn)
        lineforfile=str(x[0])+': '+str(x[1])
        OF.write(lineforfile)
        OF.write('\n')
OF.close()
        
        
     
