# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:57:00 2015

@author: ChatNoir

Calculates RF distance comparing one tree to a list of others. 

PROBLEMS:
-sensitive to input file name, adjust as nessecary

"""
from __future__ import division
import dendropy as dp
import os
import time
   
def comp_rf(file_name,concat_name,tnum): #wrapping in function for iteration or one by one
    taxa = dp.TaxonNamespace(label="global") #set taxa same for all datasets
    concat_path=os.path.abspath(concat_name)
    cat_tree=dp.Tree.get_from_path(concat_path,schema='newick',taxon_namespace=taxa)
    rf="passed wrong file name" #set check in case if loop doesnt set rf dist. 
    w=(float(tnum)-3)*2
    if file_name.endswith(".phy"): #if the file ends with....phy
        gene_path=os.path.abspath(file_name) #get path for each gene tree file
        gene_tree=dp.Tree.get_from_path(gene_path,schema='newick', taxon_namespace=taxa) #make into tree object
        rf=dp.calculate.treecompare.symmetric_difference(cat_tree,gene_tree)
        wrf=rf/w
    temp=file_name.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[0] #split name by .then by _    
    return gene,wrf

#demand user input
cat_name=input("name of tree file to compare to list of files:") #concat file name
folder_with_trees=input("path to folder containing '.phy' tree files:") #folder with all .phy files
output_file=input("output file name:")
tnum=input("number of taxa:")
        
#initiate lists and things
rf_dist_file=open(output_file, 'w+')
files=[]
rf_dists={}  

   
#iterate through files and make a list of file names. 
for fn in os.listdir(folder_with_trees): 
    if fn.endswith(".phy"):        
        files.append(fn)

#calc rf dists
for n in files:
    x=comp_rf(n,cat_name,tnum)
    print n,x
    rf_dists[x[0]]=x[1]

datetime="Current date & time of run " + time.strftime("%c")
rf_dist_file.write(str(rf_dists))
rf_dist_file.write('\n')
rf_dist_file.write(datetime)
rf_dist_file.close()




"""
TESTING
 
cat_name="RAxML_bootstrap.squam_ML"
folder_with_trees="/Users/ChatNoir/bin/Squam/best_Garli_runs/best_trees"
output_file="RF_dists.txt"  


      
"""       
