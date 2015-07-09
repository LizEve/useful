# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:38:22 2015

@author: ChatNoir
get tree
deroot tree- this enables the calculation from the tip of sphenodon to the first node of the squamate tree. 
"""

from __future__ import division
import dendropy as dp
import os
import ntpath


#USER INPUT:

folder_with_trees="/Users/ChatNoir/bin/Squam/data_files/mstxrm/tree_dists_mstxrm/jspheno_misstxremoved"
outfile=open("/Users/ChatNoir/bin/Squam/data_files/mstxrm/tree_dists_mstxrm/jspheno_misstxremoved/spheno_branch.txt", 'w+')
tip_taxa=('Sphenodon punctatus')
literal_string=('Sphenodon_punctatus')

def branch_len(gene_path, tip_taxa): #wrapping in function for iteration or one by one
    file_name=ntpath.basename(gene_path)    
    temp=file_name.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[0] #split name by .then by _        
    gene_tree=dp.Tree.get_from_path(gene_path,schema='newick') #make into tree object
    gene_tree.deroot() #deroot tree
    node = gene_tree.find_node_with_taxon_label(tip_taxa)
    x=(node.edge_length)
    return gene,x
    
    
for fn in os.listdir(folder_with_trees): 
    if fn.endswith(".phy"):
        if literal_string in open(fn).read():        
            fpath=os.path.abspath(fn)
            info=branch_len(fpath, tip_taxa)
            gene=info[0]
            blen=info[1]
            out=gene+"\t"+str(blen)
            outfile.write(out)
            outfile.write('\n')
        else:
            print tip_taxa+" is not in "+fn
outfile.close()


"""
gene_path="/Users/ChatNoir/bin/Squam/data_files/mstxrm/tree_dists_mstxrm/jspheno_misstxremoved/AHR_misstxremoved_jspheno.phy"
if tip_taxa in open(gene_path).read():
    y=tip_taxa.strip("_")
    print y
gene_tree=dp.Tree.get_from_path(gene_path,schema='newick')
gene_tree.deroot() #deroot tree
node = gene_tree.find_node_with_taxon_label(tip_taxa)
x=(node.edge_length)
print x
y=tip_taxa.strip("_")
print y
x=branch_len(gene_path,tip_taxa)
print x
"""