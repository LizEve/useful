# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:56:38 2015

@author: ChatNoir

Working through comparison of taxa between tree from reeder and tree i made from weins concat data

"""
from __future__ import division
import dendropy as dp
import os
import string


rt='/Users/ChatNoir/bin/Squam/data_files/taxa150/reeder_raxml_nbl.phy'
mt='/Users/ChatNoir/bin/Squam/data_files/taxa150/mount_150_raxml_nbl.phy'

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
print len(MO) #150
print len(RE) #150



"""
-----------------------------------------
Comparing RF dist
"""


taxa = dp.TaxonNamespace(label="global") #set taxa same for all datasets

REt=dp.Tree.get_from_path(rt,schema='newick', taxon_namespace=taxa)
MOt=dp.Tree.get_from_path(mt,schema='newick', taxon_namespace=taxa)    
    
rf=dp.calculate.treecompare.symmetric_difference(REt, MOt)
print rf    #24
 
maxRF=(float(150)-3)*2 
print maxRF #294

#weighted
print (rf/maxRF)
#0.0816326530612


"""
-----------------------------------------
prune outgroups
"""

def single_prune(fpath,taxaremoved,opath):
    tree=dp.Tree.get_from_path(fpath,schema='newick')  #convert to dendropy tree
    tree.prune_taxa_with_labels(taxaremoved) #removes list of taxa from tree
    tree.write_to_path(opath,'newick') #write out file

outgroups_nospheno=('Homo sapiens' ,'Mus musculus' ,'Alligator mississippiensis' ,'Chelydra serpentina' ,'Crocodylus porosus' ,'Dromaius novaehollandiae' ,'Gallus gallus' ,'Podocnemis expansa' , 'Tachyglossus aculeatus')   
filepath='/Users/ChatNoir/bin/Squam/data_files/taxa150/reeder_150_raxml_nbl.phy'
outpath='/Users/ChatNoir/bin/Squam/data_files/taxa150/reeder_jspheno_150_raxml_nbl.phy'

single_prune(filepath,outgroups_nospheno,outpath)


"""
-----------------------------------------
check # taxa
"""

rtnog='/Users/ChatNoir/bin/Squam/data_files/taxa150/reeder_jspheno_150_raxml_nbl.phy'
mtnog='/Users/ChatNoir/bin/Squam/data_files/taxa150/mount_jspheno_150_raxml_nbl.phy'

REnog=newick_to_dict(rtnog)
MOnog=newick_to_dict(mtnog)
print len(MOnog) #141
print len(REnog) #141

"""
-----------------------------------------
Comparing RF dist
"""


taxa = dp.TaxonNamespace(label="global") #set taxa same for all datasets

REtnog=dp.Tree.get_from_path(rtnog,schema='newick', taxon_namespace=taxa)
MOtnog=dp.Tree.get_from_path(mtnog,schema='newick', taxon_namespace=taxa)    
    
rfnog=dp.calculate.treecompare.symmetric_difference(REtnog, MOtnog)
print rf    #24
 
maxRFnog=(float(141)-3)*2 
print maxRFnog #276

#weighted
print (rfnog/maxRFnog)
#0.0869565217391