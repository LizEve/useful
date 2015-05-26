# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:21:03 2015

@author: ChatNoir

take multiple newick tree files and create a nexus block. trees arent identifieyable by gene

"""
from __future__ import division
import dendropy as dp
import os

folder_with_trees=input("path to folder containing '.phy' tree files:") #folder with all .phy files
of=input("output file name:")

#initiate dendropy tree file
taxa = dp.TaxonNamespace(label="global") #set taxa same for all datasets
treelist=dp.TreeList(taxon_namespace=taxa) #initiate tree list

#iterate through files
for fn in os.listdir(folder_with_trees): 
    if fn.endswith(".phy"):        
        fpath=os.path.abspath(fn)
        tree=dp.Tree.get_from_path(fpath,schema='newick')
        treelist.append(tree)
 
#direct output
treelist.write_to_path(of,schema='nexus')




"""   

folder_with_trees='/Users/ChatNoir/bin/Squam/data_files/pruned_best_trees'
     
f1path='/Users/ChatNoir/bin/Squam/data_files/pruned_best_trees/squamg_ADNP.run00.best.phy'
f2path='/Users/ChatNoir/bin/Squam/data_files/pruned_best_trees/squamg_ADNP.run00.best.phy'

tree1=dp.Tree.get_from_path(f1path,schema='newick')
tree2=dp.Tree.get_from_path(f2path,schema='newick')


taxa = dp.TaxonNamespace(label="global") #set taxa same for all datasets
treelist=dp.TreeList(taxon_namespace=taxa) #initiate tree list
treelist.append(tree1)
treelist.append(tree2)
for tree in treelist:
    print(tree.as_string('newick'))
 """