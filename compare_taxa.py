# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:14:24 2015

@author: ChatNoir


Working through comparison of taxa between tree from reeder and tree i made from weins concat data

"""
from __future__ import division
import dendropy as dp
import os
import string


rt='/Users/ChatNoir/bin/Squam/data_files/concat_trees/reeder_raxml_nbl.phy'
mt='/Users/ChatNoir/bin/Squam/data_files/concat_trees/mount_raxml_nbl.phy'
rtt='/Users/ChatNoir/bin/Squam/data_files/concat_trees/Reeder_ML_tree.tre'

def newick_to_dict(fpath):
    dump='();' #characters to remove
    taxalist=[] #list to store taxa names in
    for line in open(fpath,'r'):#for each line in the file
        clean=line.strip() #remove space like characters
        rmshit=clean.translate(string.maketrans("","", ), dump) #replace bad chars with nothing
        listable=rmshit.split(',') #split by remaining commas
        taxalist.extend(listable) #add each element in listable to taxalist
    return taxalist

RE=newick_to_dict(rt)
MO=newick_to_dict(mt)
print MO
print RE

taxa1=[]
taxa2=[]
notinMO=[]
notinRE=[]
taxdic={}
for x in RE:
    if x not in MO:
        notinMO.append(x)
        taxdic[x]='not in mount tree'
    if x in MO:
        taxa1.append(x)
for x in MO:
    if x not in RE:
        notinRE.append(x)
        taxdic[x]='not in reeder tree'
    if x in RE:
        taxa2.append(x)
        
        
print len(taxa1) #150
print len(taxa2) #150
print len(notinMO) #0
print len(notinRE) #21
print len(RE) #150
print len(MO) #171

print notinMO
print notinRE


"""
-----------------------------------------
parse by genus and by species to check for overlap, misspelling and synonyms
"""
REg=[]
MOg=[]
for x in notinRE:
    genus=x.split('_')[0]
    REg.append(genus)
print REg

for x in notinMO:
    genus=x.split('_')[0]
    MOg.append(genus)
print MOg

for x in MOg:
     if x in REg:
         print x
         
for x in REg:
     if x in MOg:
         print x


"""
-----------------------------------------
prune outgroups
"""

fold="/Users/ChatNoir/bin/Squam/data_files/concat_trees"

def prune(fpath,folder,outname): #wrapping in function for iteration or one by one
    tree=dp.Tree.get_from_path(fpath,schema='newick') #convert to dendropy tree
    outgroups=('Homo sapiens' ,'Mus musculus' ,'Alligator mississippiensis' ,'Chelydra serpentina' ,'Crocodylus porosus' ,'Dromaius novaehollandiae' ,'Gallus gallus' ,'Podocnemis expansa' , 'Tachyglossus aculeatus')   
    tree.prune_taxa_with_labels(outgroups) #remove outgroups from tree
    outfile=folder+'/'+outname #output path constructed
    tree.write_to_path(outfile,'newick') #write out file

prune(rt,fold,'reeder_jspheno_raxml_nbl.phy')

prune(rt,fold,'mount_jspheno_raxml_nbl.phy')

RE=newick_to_dict(rt)
MO=newick_to_dict(mt)
REE=newick_to_dict(rtt)
print REE
print MO

taxa1=[]
taxa2=[]
noMO=[]
noRE=[]
for x in RE:
    if x not in MO:
        noMO.append(x)
    if x in MO:
        taxa1.append(x)
for x in MO:
    if x not in RE:
        noRE.append(x)
    if x in RE:
        taxa2.append(x)
        
        
print len(taxa1) #132
print len(taxa2) #132
print len(noMO) #18
print len(noRE) #39
print len(RE) #150
print len(MO) #170


"""
-----------------------------------------
Comparing RF dist
"""


jrt='/Users/ChatNoir/bin/Squam/data_files/concat_trees/reeder_jspheno_raxml_nbl.phy'
jmt='/Users/ChatNoir/bin/Squam/data_files/concat_trees/mount_jspheno_raxml_nbl.phy'

taxa = dp.TaxonNamespace(label="global") #set taxa same for all datasets

REt=dp.Tree.get_from_path(jrt,schema='newick', taxon_namespace=taxa)
MOt=dp.Tree.get_from_path(jmt,schema='newick', taxon_namespace=taxa)    
    
rf=dp.calculate.treecompare.symmetric_difference(REt, MOt)
print rf    #240
 
maxRF=(float(171)-3)*2 #336



"""
TESTING

Tried to compare taxa using dendropy and bipython, couldn't figure out how. 

import dendropy as dp

rt='/Users/ChatNoir/bin/Squam/data_files/concat_trees/reeder_raxml_nbl.phy'
mt='/Users/ChatNoir/bin/Squam/data_files/concat_trees/mount_raxml_nbl.phy'

ds = dendropy.DataSet()
ds.attach_taxon_set()
RE=dp.Tree.get_from_path(rt,schema='newick')
MO=dp.Tree.get_from_path(mt,schema='newick')
ds=dp.DataSet(RE,MO)


print (RE.description(3))
print RE.as_string(schema='nexus')

rf=dp.calculate.treecompare.symmetric_difference(RE, MO)
print rf



from Bio import Phylo

rt='/Users/ChatNoir/bin/Squam/data_files/concat_trees/reeder_raxml_nbl.phy'
mt='/Users/ChatNoir/bin/Squam/data_files/concat_trees/mount_raxml_nbl.phy'

RE = Phylo.read(rt, "newick")
MO = Phylo.read(mt, "newick")

RE.get_terminals()


"""