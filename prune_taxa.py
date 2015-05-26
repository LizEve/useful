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

   

def iter_prune(fname,folder,taxaremoved): #wrapping in function for iteration or one by one
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[0]
    fpath=os.path.abspath(fname) # get path to file
    tree=dp.Tree.get_from_path(fpath,schema='newick') #convert to dendropy tree
    tree.prune_taxa_with_labels(taxaremoved) #remove outgroups from tree
    outfile=folder+'/'+gene+'_jspheno_141.phy' #output path constructed
    tree.write_to_path(outfile,'newick') #write out file

#example taxa removed
outgroups_nospheno=('Homo sapiens' ,'Mus musculus' ,'Alligator mississippiensis' ,'Chelydra serpentina' ,'Crocodylus porosus' ,'Dromaius novaehollandiae' ,'Gallus gallus' ,'Podocnemis expansa' , 'Tachyglossus aculeatus')   
not_in_reeder=('Alopoglossus angulatum', 'Lamprophis fuliginosus', 'Trimorphodon biscutatus', 'Sonora semiannulata', 'Imantodes cenchoa', 'Heterodon platyrhinos', 'Chelosania brunnea', 'Moloch horridus', 'Hypsilurus boydi', 'Physignathus leseuri', 'Chlamydosaurus kingii', 'Rankinia adelaidensis', 'Ctenophorus isolepis', 'Acanthosaura lepidogaster', 'Draco blanfordii', 'Trapelus agilis', 'Phrynocephalus mystaceus', 'Liolaemus elongatus', 'Ophisaurus ventralis', 'Eumeces schneideri', 'Plestiodon skiltonianus')
prunedog=('Sphenodon punctatus', 'Homo sapiens' ,'Mus musculus' ,'Alligator mississippiensis' ,'Chelydra serpentina' ,'Crocodylus porosus' ,'Dromaius novaehollandiae' ,'Gallus gallus' ,'Podocnemis expansa' , 'Tachyglossus aculeatus')

#useage
folder="/Users/ChatNoir/bin/Squam/data_files/taxa150/genes_150"
for fn in os.listdir(folder): #iterate through files in a folder
    if fn.endswith("_prunedjs.phy"):
        iter_prune(fn, folder, not_in_reeder)

#single usage, edit as needed
def single_prune(fpath,taxaremoved,opath):
    tree=dp.Tree.get_from_path(fpath,schema='newick')  #convert to dendropy tree
    tree.prune_taxa_with_labels(taxaremoved) #removes list of taxa from tree
    tree.write_to_path(opath,'newick') #write out file

#useage
filepath='/Users/ChatNoir/bin/Squam/data_files/pruned_best_trees/prunedog/mount_raxml_nbl.phy'
outpath='/Users/ChatNoir/bin/Squam/data_files/taxa150/prunedog_raxml_nbl.phy'
single_prune(filepath,prunedog,outpath)



'''
TESTING

fpath="//Users/ChatNoir/bin/Squam/data_files/pruned_best_trees/squamg_ADNP.run00.best.phy"
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