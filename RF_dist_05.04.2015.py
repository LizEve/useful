# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:46:40 2015

@author: ChatNoir
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:24:10 2015

@author: ChatNoir

Calculates RF distance comparing one tree to a list of others. 

NEED: change folder containing tree files
change file name for comparison tree
"""
import dendropy as dp
import os
import time

"""
*input* 
file_name=.phy file with newick string
concat_name= file name of the concat tree
*output*
gene name of input file
rf distance
**notes**
this works. need to input gene name first. concat name second
probably want to put all of this in a list or something to graph. 
"""    
def comp_rf(file_name,concat_name): #wrapping in function for iteration or one by one
    taxa = dp.TaxonNamespace(label="global") #set taxa same for all datasets
    concat_path=os.path.abspath(concat_name)
    cat_tree=dp.Tree.get_from_path(concat_path,schema='newick',taxon_namespace=taxa)
    rf="passed wrong file name" #set check in case if loop doesnt set rf dist. 
    if file_name.endswith("best.phy"): #if the file ends with....phy
        gene_path=os.path.abspath(file_name) #get path for each gene tree file
        gene_tree=dp.Tree.get_from_path(gene_path,schema='newick', taxon_namespace=taxa) #make into tree object
        rf=dp.calculate.treecompare.symmetric_difference(cat_tree,gene_tree)
    temp=file_name.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[1] #split name by .then by _    
    return gene,rf

#demand user input
cat_name=input("name of tree file to compare to list of files:") #concat file name
folder_with_trees=input("path to folder containing 'best.phy' tree files:") #folder with all .phy files
output_file=input("output file name:")
"""     
cat_name="RAxML_bootstrap.squam_ML"
folder_with_trees="/Users/ChatNoir/bin/Squam/best_Garli_runs/best_trees"
output_file="RF_dists.txt"        
 """       
        
#initiate lists and things
rf_dist_file=open(output_file, 'w+')
files=[]
rf_dists={}  


   
#iterate through files and make a list of file names. 
for fn in os.listdir(folder_with_trees): 
    if fn.endswith("best.phy"):        
        files.append(fn)

#calc rf dists
for n in files:
    x=comp_rf(n,cat_name)
    print n,x
    rf_dists[x[0]]=x[1]

datetime="Current date & time of run " + time.strftime("%c")
rf_dist_file.write(datetime)
rf_dist_file.write('\n')
rf_dist_file.write(str('RF_dict='))
rf_dist_file.write(str(rf_dists))

