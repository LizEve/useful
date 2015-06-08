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
 
           
def nexus_prune_custom(fname,folder,outsuffix,taxaremoved):
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[0]
    nexpath=os.path.abspath(fname) # get path to file. this doesn't work in spyder
    seqList=[]
    outfile=folder+'/'+gene+outsuffix    
    outnex=open(outfile,'w')
    nex=open(nexpath,'rU')
    for seq_record in SeqIO.parse(nex, "nexus"):
        if seq_record.name not in taxaremoved:
            seqList.append(seq_record)            
    SeqIO.write(seqList,outnex,"nexus")
    outnex.close()
    nex.close()

#USEAGE
jspheno=('Homo_sapiens' ,'Mus_musculus' ,'Alligator_mississippiensis' ,'Chelydra_serpentina' ,'Crocodylus_porosus' ,'Dromaius_novaehollandiae' ,'Gallus_gallus' ,'Podocnemis_expansa' , 'Tachyglossus_aculeatus')   
#prunedog=('Sphenodon punctatus', 'Homo sapiens' ,'Mus musculus' ,'Alligator mississippiensis' ,'Chelydra serpentina' ,'Crocodylus porosus' ,'Dromaius novaehollandiae' ,'Gallus gallus' ,'Podocnemis expansa' , 'Tachyglossus aculeatus')


        
#check file type      
#ftype=input("If tree files(.phy) type 'tree' if sequence files (.nex) type 'seq' :")
#ftype='tree'
#ftype='seq'

#set paths 
folder='/Users/ChatNoir/bin/Squam/data_files/removemissdata_seqs/jspheno_misstxremoved/'

#set other variables
datetime="Current date & time of run " + time.strftime("%c")


for fn in os.listdir(folder): #iterate through files in a folder
    if fn.endswith(".nex"):
        outsuffix='_misstxremoved_jspheno.nex'
        nexus_prune_custom(fn,folder,outsuffix,jspheno)              
    else:
        None
    
"""
TESTING
#TEST
nexpath="/Users/ChatNoir/bin/Squam/data_files/removemissdata_seqs/jspheno_misstxremoved/ADNP_misstxremoved.nex"
taxaremoved=('Homo_sapiens' ,'Mus musculus' ,'Alligator mississippiensis' ,'Chelydra serpentina' ,'Crocodylus porosus' ,'Dromaius novaehollandiae' ,'Gallus gallus' ,'Podocnemis expansa' , 'Tachyglossus aculeatus')   
outfile="/Users/ChatNoir/bin/Squam/data_files/removemissdata_seqs/jspheno_misstxremoved/ADNP_misstxremoved_jspheno.nex"

seqList=[]
outnex=open(outfile,'w')
nex=open(nexpath,'rU')
for seq_record in SeqIO.parse(nex, "nexus"):
    if seq_record.name not in taxaremoved:
        seqList.append(seq_record)            
SeqIO.write(seqList,outnex,"nexus")
outnex.close()
nex.close()
"""