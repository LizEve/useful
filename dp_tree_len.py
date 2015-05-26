# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:08:05 2015

@author: ChatNoir

Tree length

adjust grabbing the gene name depending on how your files are labeled. 

user input- file with folder of .phy files. 
"""

from __future__ import division
import dendropy as dp
import os
import time


def get_treelen(fname): #wrapping in function for iteration or one by one
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[0]
    fpath=os.path.abspath(fname) # get path to file
    tree=dp.Tree.get_from_path(fpath,schema='newick') #convert to dendropy tree
    TL=round(dp.datamodel.treemodel.Tree.length(tree), 3) #get tree len and round to 3 decimals
    return gene,TL

#demand user input
folder_with_trees=input("path to folder containing '.phy' tree files:") #folder with all .phy files
out_file_path=input("output file name with path:")
        
#initiate lists and things
TL_file=open(out_file_path, 'w+')
files=[]
TL_dists={}  

   
#iterate through files and make a list of file names. 
for fn in os.listdir(folder_with_trees): 
    if fn.endswith(".phy"):        
        files.append(fn)

#calc TL dists
for n in files:
    x=get_treelen(n)
    print n,x
    TL_dists[x[0]]=x[1]

datetime="Current date & time of run " + time.strftime("%c")
TL_file.write(str(TL_dists))
TL_file.write('\n')
TL_file.write(datetime)
TL_file.close()



"""
TESTING-
*confirmed same tree len
fpath='/Users/ChatNoir/bin/Squam/data_files/pruned_best_trees/squamg_ADNP.run00.best.phy'
tree=dp.Tree.get_from_path(fpath,schema='newick') #convert to dendropy tree
dp.datamodel.treemodel.Tree.length(tree)


fpath='/Users/ChatNoir/bin/Squam/data_files/pruned_best_trees/squamg_AHR.run00.best.phy'
tree=dp.Tree.get_from_path(fpath,schema='newick') #convert to dendropy tree
TL=round(dp.datamodel.treemodel.Tree.length(tree), 3)
print TL
"""