# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:39:00 2015

@author: ChatNoir

NOT FINISHED OR EVEN CLOSE TO FINISHED
"""

import dendropy as dp
import os

def filetodict(fpath,ftype): #edited from remove_taxa_custom.py     
    dict_temp={}
    dict_real={}
    for l in open(fpath,'r'):
        line=l.strip() #strip whitespace
        if line.startswith('{'): #find dict like line
            dict_temp=ast.literal_eval(line) #literal eval or something. 
    for key in dict_temp: #now remove _ bits of taxa names
        sp_list=dict_temp[key]
        name_list=[]
        for g_s in sp_list:
            gslist=g_s.split('_')
            name=gslist[0]+" "+gslist[1]
            name_list.append(name)
            dict_real[key]=name_list
    if ftype == 'tree': #dendropy uses names *without* the _
        return dict_real 
    elif ftype == 'seq': #biopython takes names *with* the _
        return dict_temp
    else:
        print "filetype input is wrong"
        
        
def tree_prune_custom(fname,folder,outsuffix,mstxdict,outlog): #wrapping in function for iteration or one by one
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[1]
    fpath=os.path.abspath(fname) # get path to file. this doesn't work in spyder
    for key in mstxdict:
        if key == gene: #iterate through keys/genes in dictionary, when key matches the file/gene
            taxaremoved = mstxdict[key] #create list of taxa to remove
            tree=dp.Tree.get_from_path(fpath,schema='newick') #convert to dendropy tree
            tree.prune_taxa_with_labels(taxaremoved) #remove outgroups from tree
            outfile=folder+'/'+gene+outsuffix #output path constructed
            tree.write_to_path(outfile,'newick') #write out file               
            log='\n'+'\n'+fname+'\n'+str(key)+':'+str(taxaremoved) #add line in log file for what was taken out of input file
            outlog.write(log)
        else:
            None
            
            
def branch_len(gene_path, tip_taxa): #wrapping in function for iteration or one by one
    file_name=ntpath.basename(gene_path)    
    temp=file_name.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[0] #split name by .then by _        
    gene_tree=dp.Tree.get_from_path(gene_path,schema='newick') #make into tree object
    gene_tree.deroot() #deroot tree
    node = gene_tree.find_node_with_taxon_label(tip_taxa)
    x=(node.edge_length)
    return gene,x
#dictionary with list of missing taxa for each gene(key)        
mstx_file='/Users/ChatNoir/bin/Squam/data_files/missingtaxa/dict_listofmissingtaxa.txt'


