# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:24:10 2015

@author: ChatNoir
"""
import dendropy as dp
import os

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
        
 #initiate lists and things
files=[] 
rf_dists=[]   
#concat file name. 
cat_name="fake_concat_tree.phy"  

   
#iterate through files and make a list of file names. 
for fn in os.listdir('/Users/ChatNoir/bin/Squam/scripts/playground'): #folder with all .phy files
    if fn.endswith("best.phy"):
        files.append(fn)

#calc rf dists
for n in files:
    x=comp_rf(n,cat_name)
    rf_dists.append(x)
 





"""
General Dendropy Notes:
Tree and dataset are both under datamodel, but appear to be equal and separate classes
"""

"""
ATTEMPT #1 
did not work because taxonnamespace between gene tree and cat tree were not the same
going to try and create a new dataset each time 
--------
def comp_rf(file_name,concat_tree): #wrapping in function for iteration or one by one
    if file_name.endswith("best.phy"): #if the file ends with....phy
        temp=file_name.split('.')[0] #split name by .
        gene=temp.split('_')[1] #then by _
        file_path=os.path.abspath(file_name) #get path for each gene tree file
        gene_tree=dp.Tree.get_from_path(file_path, schema="newick") #make into tree object
        rf=dp.calculate.treecompare.symmetric_difference(concat_tree,gene_tree)
        return gene,rf
"""
"""
TESTING THINGS
-------
#create tree object for concatnated gene tree
cat_path="/Users/ChatNoir/bin/Squam/scripts/playground/fake_concat_tree.phy"


taxa = dp.TaxonNamespace(label="global")
#squam=dp.DataSet(taxon_namespace=taxa) #initiate set of data. ensure that each source of data the same taxa are referensed as objects

cat=dp.Tree.get_from_path(cat_path, schema='newick', taxon_namespace=taxa)
b=cat.as_string('newick')
print b

gene=dp.Tree.get_from_path("/Users/ChatNoir/bin/Squam/scripts/playground/squamg_CAND1.run00.best.phy", schema='newick', taxon_namespace=taxa)
a=gene.as_string('newick')
print a

rf=dp.calculate.treecompare.symmetric_difference(gene,cat)
print rf

"""