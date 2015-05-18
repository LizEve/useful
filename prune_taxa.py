# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:38:27 2015

@author: ChatNoir

takes file name and folder containing files, iterates through files and spitso ut newick trees minus the outgroups
EDIT- need to change:   
    outgroups
    outfile name
    folder name
    

"""
import dendropy as dp
import os

   

def prune(fname,folder): #wrapping in function for iteration or one by one
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[1]
    fpath=os.path.abspath(fname) # get path to file
    tree=dp.Tree.get_from_path(fpath,schema='newick') #convert to dendropy tree
    outgroups=('Homo sapiens' ,'Mus musculus' ,'Alligator mississippiensis' ,'Chelydra serpentina' ,'Crocodylus porosus' ,'Dromaius novaehollandiae' ,'Gallus gallus' ,'Podocnemis expansa' , 'Tachyglossus aculeatus')   
    tree.prune_taxa_with_labels(outgroups) #remove outgroups from tree
    outfile=folder+'/'+gene+'_prunedjs.phy' #output path constructed
    tree.write_to_path(outfile,'newick') #write out file


folder="/Users/ChatNoir/bin/Squam/data_files/pruned_best_trees"
for fn in os.listdir(folder): #iterate through files in a folder
    if fn.endswith("best.phy"):
        prune(fn, folder)

   

'''
TESTING

fpath="/Users/ChatNoir/bin/Squam/data_files/best_trees_pruned/squamg_ADNP.run00.best.phy"
tree=dp.Tree.get_from_path(fpath,schema='newick')
print tree.leaf_nodes()[0].taxon
p=tree.prune_taxa_with_labels(outgroups) 
print p.leaf_nodes()[0].taxon  
folder='/Users/ChatNoir/bin/Squam/data_files/best_trees_pruned/'
outfile=folder+gene+'_prunedog.phy'
print outfile
fname='squamg_ADNP.run00.best.phy'
temp=fname.split('.')[0] # extract gene name from file name- use this later
gene=temp.split('_')[1]
o

outgroups=('Homo sapiens' ,'Mus musculus' ,'Alligator mississippiensis' ,'Chelydra serpentina' ,'Crocodylus porosus' ,'Dromaius novaehollandiae' ,'Gallus gallus' ,'Podocnemis expansa' , 'Sphenodon_punctatus', 'Tachyglossus aculeatus')   


rf=dp.calculate.treecompare.symmetric_difference(concat,cp)
print rf
dp.Tree.get_from_path('/Users/ChatNoir/bin/Squam/data_files/best_trees_pruned/concat_prunedog.phy',schema='newick',taxon_namespace=taxa)
'''