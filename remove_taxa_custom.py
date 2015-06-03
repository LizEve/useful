# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:34:26 2015

@author: ChatNoir
"""

import dendropy as dp
import os
import ast
import time
from Bio import SeqIO

def filetodict(fpath,ftype): #edited from fil2dict2merg.py     
    dict_temp={}
    dict_real={}
    for l in open(fpath,'r'):
        line=l.strip() #strip whitespace
        if line.startswith('{'): #find dict like line
            dict_temp=ast.literal_eval(line) #literal eval or something. 
    for key in dict_temp: #now remove _ bits of taxa names
        sp_list=dict_temp[key]
        name_list=[]
        for g_s in sp_list:
            gslist=g_s.split('_')
            name=gslist[0]+" "+gslist[1]
            name_list.append(name)
            dict_real[key]=name_list
    if ftype == 'tree': #dendropy uses names without the _
        return dict_real 
    elif ftype == 'seq': #biopython takes names *with* the _
        return dict_temp
    else:
        print "filetype input is wrong"
        
        
def tree_prune_custom(fname,folder,outsuffix,mstxdict,outlog): #wrapping in function for iteration or one by one
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[1]
    fpath=os.path.abspath(fname) # get path to file. this doesn't work in spyder
    for key in mstxdict:
        if key == gene: #iterate through keys/genes in dictionary, when key matches the file/gene
            taxaremoved = mstxdict[key] #create list of taxa to remove
            tree=dp.Tree.get_from_path(fpath,schema='newick') #convert to dendropy tree
            tree.prune_taxa_with_labels(taxaremoved) #remove outgroups from tree
            outfile=folder+'/'+gene+outsuffix #output path constructed
            tree.write_to_path(outfile,'newick') #write out file               
            log='\n'+'\n'+fname+'\n'+str(key)+':'+str(taxaremoved) #add line in log file for what was taken out of input file
            outlog.write(log)
        else:
            None
            
def nexus_prune_custom(fname,folder,outsuffix,mstxdict,outlog):
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[1]
    nexpath=os.path.abspath(fname) # get path to file. this doesn't work in spyder
    for key in mstxdict:
        if key == gene: #iterate through keys/genes in dictionary, when key matches the file/gene
            seqList=[]
            taxaremoved = mstxdict[key]
            outfile=folder+'/'+gene+outsuffix    
            outnex=open(outfile,'w')
            nex=open(nexpath,'rU')
            for seq_record in SeqIO.parse(nex, "nexus"):
                if seq_record.name not in taxaremoved:
                    seqList.append(seq_record)            
            SeqIO.write(seqList,outnex,"nexus")
            outnex.close()
            nex.close()
            log='\n'+'\n'+fname+'\n'+str(key)+':'+str(taxaremoved) #add line in log file for what was taken out of input file
            outlog.write(log)
        else:
            None
#USEAGE
        
#check file type      
#ftype=input("If tree files(.phy) type 'tree' if sequence files (.nex) type 'seq' :")
#ftype='tree'
#ftype='seq'

#set paths 
mstx='/Users/ChatNoir/bin/Squam/data_files/missingtaxa/dict_listofmissingtaxa.txt'
folder='/Users/ChatNoir/bin/Squam/data_files/removemissdata_seqs'

#set other variables
datetime="Current date & time of run " + time.strftime("%c")

#open log folder write date
outlog=open('remove_taxa_custom.log', 'a') #open this before iterating? or for each run?
outlog.write(datetime)

for fn in os.listdir(folder): #iterate through files in a folder
    if fn.endswith(".phy"):
        ftype="tree"
        mstxdict=filetodict(mstx,ftype) #create dictionary GENE:[list of taxa with no data for this gene]
        outsuffix='_misstxremoved.phy'
        tree_prune_custom(fn,folder,outsuffix,mstxdict,outlog)         
              
    elif fn.endswith(".nex"):
        ftype="seq"
        mstxdict_=filetodict(mstx,ftype) #create dictionary GENE:[list of taxa with no data for this gene]
        outsuffix='_misstxremoved.nex'
        nexus_prune_custom(fn,folder,outsuffix,mstxdict_,outlog)              
    else:
        x="\n"+"not edited: "+fn
        outlog.write(x)
    
outlog.close()

