# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:11:59 2015

@author: ChatNoir
"""
import dendropy as dp
import os
import time

def comp_rf(file1,file2): #wrapping in function for iteration or one by one
    taxa = dp.TaxonNamespace(label="global") #set taxa same for all datasets
    f1_path=os.path.abspath(file1)
    f1_tree=dp.Tree.get_from_path(f1_path,schema='newick',taxon_namespace=taxa)
    f2_path=os.path.abspath(file2) #get path for each gene tree file
    f2_tree=dp.Tree.get_from_path(f2_path,schema='newick', taxon_namespace=taxa) #make into tree object
    rf=dp.calculate.treecompare.symmetric_difference(f1_tree,f2_tree)
    a=file1.split('.')[0] # extract gene name from file name- use this later
    b=file2.split('.')[0]
    return a,b,rf


f1=input("name of tree file:") #concat file name
f2=input("name of tree file:") #concat file name
output_file=input("output file name:")

rf_dists=comp_rf(f1, f2)

rf_dist_file=open(output_file, 'w+') ###INPUT: output file name

datetime="Current date & time of run " + time.strftime("%c")
rf_dist_file.write(datetime)
rf_dist_file.write('\n')
rf_dist_file.write(str(rf_dists))
