# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:19:44 2015

@author: ChatNoir
"""
from __future__ import division
import dendropy as dp
import os
import time
import re

taxa = dp.TaxonNamespace(label="global")
dna1 = dp.DnaCharacterMatrix.get_from_path("/Users/ChatNoir/bin/Squam/best_Garli_runs/nexus_files/squamg_ADNP.nex", "nexus", taxon_namespace=taxa)


fpath=os.path.abspath(taxa.txt) #import taxa names to make a dict with gene numbers
fpath='/Users/ChatNoir/bin/Squam/data_files/weins_taxa.txt'
tlist=[]
for line in open(fpath,'r'):
    tlist.append(line.strip())
print tlist

alist=[]
for x in range(171):
    seq=str(dna1[x])
    alist.append(seq)
print len(alist)
print alist
x=str(dna1(('Homo_sapiens'))) #want to iterate through all taxa 0-170 or whatever. if dna1[x]=regex match of ?* then output key:N else output key:Y
x=dna1[1]
print x[1]
y='ACTGCCATGATTGGGCACACAAATGTAGTGGTTCCCCGATCCAAACCCTTGATGCTAATTGCTCCCAAACCTCAAGACAAGAAGAGCATGGGACTCCCACCAAGGATCGGTTCCCTTGCTTCTGGAAATGTCCGGTCTTTACCATCACAGCAGATGGTGAATCGACTCTCAATACCAAAGCCTAACTTAAATTCTACAGGAGTCAACATGATGTCCAGTGTTCATCTGCAGCAGAACAACTATGGAGTCAAATCTGTAGGCCAGGGTTACAGTGTTGGTCAGTCAATG---AGACTGGGTCTAGGTGGCAACGCACCAGTTTCCATTCCTCAACAATCTCAGTCTGTAAAGCAGTTACTTCCAAGTGGAAACGGAAGGTCTTATGGG---CTTGGGTCAGAGCAGAGGTCCCAGGCACCAGCAAGATACTCCCTGCAGTCTGCTAATGCCTCTTCTCTCTCATCGGGCCAGTTAAAGTCTCCTTCCCTCTCTCAGTCACAGGCATCCA---GAGTGTTAGGTCAGTCCAGTTCCAAACCTGCTGCAGCT---GCCACA------------GGCCCTCCCCCAGGTAACACTTCCTCAACTCAAAAGTGGAAAATATGTACAATCTGTAATGAGCTTTTTCCTGAAAATGTCTATAGTGTGCACTTCGAAAAAGAACATAAAGCTGAGAAAGTCCCAGCAGTAGCCAACTACATTATGAAAATACACAATTTTACTAGCAAATGCCTCTACTGTAATCGCTATTTACCCACAGATACTCTGCTCAACCATATGTTAATTCAT'
x==y


a='??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????'
b='--------AGGGCACACCAATGTAGTCGTCCCAAGATCCAAACCTTTGATGCTGATTGCTCCAAAACCACAGGATAAAAAGCCCATGGGACTTCCTCAGAGAATGGGCCCCTTGTCTCCTGGAAGTGTCCGGTCTCTTTCATCGCAGCAAATGATGAATCGACTGAATATACCAAAGCCTACTTTAAAT'

miss=re.compile('[?]*') #set regex 
x=miss.match(b).group() #search string #return line containing regex
x=miss.match(b)
print x.span()
if x.span()[1]==0:
    print "sequence exists"
else:
    print "only ???"
    
########GETTING REAL#########  

#file with taxa names
tlist=[]
tpath='/Users/ChatNoir/bin/Squam/data_files/weins_taxa.txt'
for line in open(fpath,'r'):
        tlist.append(line.strip()) 
#missing data dictionary
mdata={}

def missingtaxa(tlist,concat_name): #wrapping in function for iteration or one by one
    
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[1]
    hastaxa=[]
    missingtaxa=[]
    
    #initiate dendropy matrix    
    f_path=os.path.abspath(fname) #get path for nexus file
    taxa = dp.TaxonNamespace(label="global") #set taxa same for all datasets
    nexus=dp.DnaCharacterMatrix.get_from_path(f_path,schema='nexus', taxon_namespace=taxa) #turn file into dp object
   
    #find missing data    
    for x in range(171): #iterate through all taxa in file 
        seq=str(nexus[x]) #turn seq into string to manipulate
        qmarks=re.compile('[?]*') #set regex 
        x=qmarks.match(seq)#search string does regex miss
            if x.span()[1]==0: # If there IS data: (.span returns the index where .match starts and ends matching. so if it stops matching at 0. then it doesnt match at all. so there IS data there.)
                
    # for each gene, list taxa that are included. save each gene as a list of taxa
            #combine all genes in a matrix
                
    
    
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
rf_dist_file.write(str(rf_dists))
rf_dist_file.write('\n')
rf_dist_file.write(datetime)
rf_dist_file.close()


with open('/Users/ChatNoir/bin/Squam/best_Garli_runs/nexus_files/squamg_ADNP.nex', 'r') as f:
    regex = "\?" 
    for line in f:
        match = re.search(regex, line)
        if match in line:
            print line




"""

TESTING

PROOF- indexing of nexus files
taxa = dp.TaxonNamespace(label="global")
dna1 = dp.DnaCharacterMatrix.get_from_path("/Users/ChatNoir/bin/Squam/best_Garli_runs/nexus_files/squamg_ADNP.nex", "nexus", taxon_namespace=taxa)
x=str(dna1[0])
y='ACTGCCATGATTGGGCACACAAATGTAGTGGTTCCCCGATCCAAACCCTTGATGCTAATTGCTCCCAAACCTCAAGACAAGAAGAGCATGGGACTCCCACCAAGGATCGGTTCCCTTGCTTCTGGAAATGTCCGGTCTTTACCATCACAGCAGATGGTGAATCGACTCTCAATACCAAAGCCTAACTTAAATTCTACAGGAGTCAACATGATGTCCAGTGTTCATCTGCAGCAGAACAACTATGGAGTCAAATCTGTAGGCCAGGGTTACAGTGTTGGTCAGTCAATG---AGACTGGGTCTAGGTGGCAACGCACCAGTTTCCATTCCTCAACAATCTCAGTCTGTAAAGCAGTTACTTCCAAGTGGAAACGGAAGGTCTTATGGG---CTTGGGTCAGAGCAGAGGTCCCAGGCACCAGCAAGATACTCCCTGCAGTCTGCTAATGCCTCTTCTCTCTCATCGGGCCAGTTAAAGTCTCCTTCCCTCTCTCAGTCACAGGCATCCA---GAGTGTTAGGTCAGTCCAGTTCCAAACCTGCTGCAGCT---GCCACA------------GGCCCTCCCCCAGGTAACACTTCCTCAACTCAAAAGTGGAAAATATGTACAATCTGTAATGAGCTTTTTCCTGAAAATGTCTATAGTGTGCACTTCGAAAAAGAACATAAAGCTGAGAAAGTCCCAGCAGTAGCCAACTACATTATGAAAATACACAATTTTACTAGCAAATGCCTCTACTGTAATCGCTATTTACCCACAGATACTCTGCTCAACCATATGTTAATTCAT'
x==y
TRUE

PROOF- re search. a=dna seq or '????'
miss=re.compile('[?]*') #set regex 
x=miss.search(a) #search string
y=x.group() #return line containing regex
print y[0]

_______________ATTEMPT #1_______________
with open('/Users/ChatNoir/bin/Squam/best_Garli_runs/nexus_files/squamg_ADNP.nex', 'r') as f:
    for line in nblock(8):
        next(f)
    for line in f:
    taxa=[r.split()[0] for r in f]
print taxa    
    #THIS PRINTS all names without the _



with open('/Users/ChatNoir/bin/Squam/best_Garli_runs/nexus_files/squamg_ADNP.nex', 'r') as f:
    regex = "([A-Z][a-z]+)_([a-z][a-z]+\\-?[a-z]+) " 
    for line in f:
        match = re.search(regex, line)
        print match
    
    data=[line.split("\s+",1)[0] for line in f]
    print data
    for line in nblock(8):
        next(f)
    for line in f:
    taxa=[r.split()[0] for r in f]
    data=[r.split()[1] for r in f]
print data
print taxa

infile=open('/Users/ChatNoir/bin/Squam/best_Garli_runs/nexus_files/squamg_ADNP.nex', 'r')
for line in infile:
    print 
data=infile.read()
start=data.find('matrix')
end=data.find(';\nend;')
algn=data[start:end]
for line in algn:
    print line
    
    
 ------------some more notes-------------
taxa = dp.TaxonNamespace(label="global")
dna1 = dp.DnaCharacterMatrix.get_from_path("/Users/ChatNoir/bin/Squam/best_Garli_runs/nexus_files/squamg_ADNP.nex", "nexus", taxon_namespace=taxa)


fpath=os.path.abspath(taxa.txt) #import taxa names to make a dict with gene numbers
fpath='/Users/ChatNoir/bin/Squam/data_files/weins_taxa.txt'
tlist=[]
for line in open(fpath,'r'):
    tlist.append(line.strip())
print tlist

alist=[]
for x in range(171):
    seq=str(dna1[x])
    alist.append(seq)
print len(alist)
print alist
x=str(dna1(('Homo_sapiens'))) #want to iterate through all taxa 0-170 or whatever. if dna1[x]=regex match of ?* then output key:N else output key:Y
x=dna1[1]
print x[1]
y='ACTGCCATGATTGGGCACACAAATGTAGTGGTTCCCCGATCCAAACCCTTGATGCTAATTGCTCCCAAACCTCAAGACAAGAAGAGCATGGGACTCCCACCAAGGATCGGTTCCCTTGCTTCTGGAAATGTCCGGTCTTTACCATCACAGCAGATGGTGAATCGACTCTCAATACCAAAGCCTAACTTAAATTCTACAGGAGTCAACATGATGTCCAGTGTTCATCTGCAGCAGAACAACTATGGAGTCAAATCTGTAGGCCAGGGTTACAGTGTTGGTCAGTCAATG---AGACTGGGTCTAGGTGGCAACGCACCAGTTTCCATTCCTCAACAATCTCAGTCTGTAAAGCAGTTACTTCCAAGTGGAAACGGAAGGTCTTATGGG---CTTGGGTCAGAGCAGAGGTCCCAGGCACCAGCAAGATACTCCCTGCAGTCTGCTAATGCCTCTTCTCTCTCATCGGGCCAGTTAAAGTCTCCTTCCCTCTCTCAGTCACAGGCATCCA---GAGTGTTAGGTCAGTCCAGTTCCAAACCTGCTGCAGCT---GCCACA------------GGCCCTCCCCCAGGTAACACTTCCTCAACTCAAAAGTGGAAAATATGTACAATCTGTAATGAGCTTTTTCCTGAAAATGTCTATAGTGTGCACTTCGAAAAAGAACATAAAGCTGAGAAAGTCCCAGCAGTAGCCAACTACATTATGAAAATACACAATTTTACTAGCAAATGCCTCTACTGTAATCGCTATTTACCCACAGATACTCTGCTCAACCATATGTTAATTCAT'
x==y


a='??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????'
b='--------AGGGCACACCAATGTAGTCGTCCCAAGATCCAAACCTTTGATGCTGATTGCTCCAAAACCACAGGATAAAAAGCCCATGGGACTTCCTCAGAGAATGGGCCCCTTGTCTCCTGGAAGTGTCCGGTCTCTTTCATCGCAGCAAATGATGAATCGACTGAATATACCAAAGCCTACTTTAAAT'

miss=re.compile('[?]*') #set regex 
x=miss.match(b).group() #search string #return line containing regex
x=miss.match(b)
print x.span()
if x.span()[1]==0:
    print "sequence exists"
else:
    print "only ???"   
"""