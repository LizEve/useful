# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:08:55 2015

@author: ChatNoir

Not finished. couldn't figure it out. Used R instead, but not in a loop. 
"""

#import dendropy as dp
import os
from Bio import Phylo

fpath="/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/concat_raxml_nbl.phy"

tree = Phylo.read(fpath, 'newick')
print tree

iguania=["Brookesia_brygooi","Chamaeleo_calyptratus","Uromastyx_aegyptus","Leiolepis_belliana","Hydrosaurus_sp","Physignathus_cocincinus","Chelosania_brunnea","Moloch_horridus","Hypsilurus_boydi","Physignathus_leseuri","Pogona_vitticeps","Chlamydosaurus_kingii","Rankinia_adelaidensis","Ctenophorus_isolepis","Calotes_emma","Acanthosaura_lepidogaster","Draco_blanfordii","Trapelus_agilis","Agama_agama","Phrynocephalus_mystaceus","Crotaphytus_collaris","Gambelia_wislizenii","Basiliscus_basiliscus","Corytophanes_cristatus","Dipsosaurus_dorsalis","Sauromalus_obesus","Brachylophus_fasciatus","Morunasaurus_annularis","Enyalioides_laticeps","Stenocercus_guentheri","Tropiduris_plica","Uranoscodon_superciliosus","Urostrophus_vautieri","Leiosaurus_catamarcensis","Pristidactylus_torquatus","Oplurus_cyclurus","Chalarodon_madagascariensis","Anolis_carolinensis","Uta_stansburiana","Sceloporus_variabilis","Petrosaurus_mearnsi","Uma_scoparia","Phrynosoma_platyrhinos","Polychrus_marmoratus","Phymaturus_palluma","Liolaemus_bellii","Liolaemus_elongatus","Leiocephalus_barahonensis"]

test=("Crotaphytus_collaris","Gambelia_wislizenii")











"""
tree_str=open(fpath, "r+")
t=tree_str.read()
for x in t:
    print x

tree=dp.Tree.get_from_path(fpath,schema='newick')
labs=["Brookesia_brygooi","Chamaeleo_calyptratus","Uromastyx_aegyptus","Leiolepis_belliana","Hydrosaurus_sp","Physignathus_cocincinus","Chelosania_brunnea","Moloch_horridus","Hypsilurus_boydi","Physignathus_leseuri","Pogona_vitticeps","Chlamydosaurus_kingii","Rankinia_adelaidensis","Ctenophorus_isolepis","Calotes_emma","Acanthosaura_lepidogaster","Draco_blanfordii","Trapelus_agilis","Agama_agama","Phrynocephalus_mystaceus","Crotaphytus_collaris","Gambelia_wislizenii","Basiliscus_basiliscus","Corytophanes_cristatus","Dipsosaurus_dorsalis","Sauromalus_obesus","Brachylophus_fasciatus","Morunasaurus_annularis","Enyalioides_laticeps","Stenocercus_guentheri","Tropiduris_plica","Uranoscodon_superciliosus","Urostrophus_vautieri","Leiosaurus_catamarcensis","Pristidactylus_torquatus","Oplurus_cyclurus","Chalarodon_madagascariensis","Anolis_carolinensis","Uta_stansburiana","Sceloporus_variabilis","Petrosaurus_mearnsi","Uma_scoparia","Phrynosoma_platyrhinos","Polychrus_marmoratus","Phymaturus_palluma","Liolaemus_bellii","Liolaemus_elongatus","Leiocephalus_barahonensis"]
cd_split = mytrees.taxon_set.get_taxa_bitmask(labels=labels) 


def iter_prune(fname,folder,taxaremoved): #wrapping in function for iteration or one by one
    temp=fname.split('.')[0] # extract gene name from file name- use this later
    gene=temp.split('_')[0]
    fpath=os.path.abspath(fname) # get path to file
    tree=dp.Tree.get_from_path(fpath,schema='newick')
    
    
this did not work. no idea why
tree = Phylo.read(fpath, 'newick')
print tree

iguania=["Brookesia_brygooi","Chamaeleo_calyptratus","Uromastyx_aegyptus","Leiolepis_belliana","Hydrosaurus_sp","Physignathus_cocincinus","Chelosania_brunnea","Moloch_horridus","Hypsilurus_boydi","Physignathus_leseuri","Pogona_vitticeps","Chlamydosaurus_kingii","Rankinia_adelaidensis","Ctenophorus_isolepis","Calotes_emma","Acanthosaura_lepidogaster","Draco_blanfordii","Trapelus_agilis","Agama_agama","Phrynocephalus_mystaceus","Crotaphytus_collaris","Gambelia_wislizenii","Basiliscus_basiliscus","Corytophanes_cristatus","Dipsosaurus_dorsalis","Sauromalus_obesus","Brachylophus_fasciatus","Morunasaurus_annularis","Enyalioides_laticeps","Stenocercus_guentheri","Tropiduris_plica","Uranoscodon_superciliosus","Urostrophus_vautieri","Leiosaurus_catamarcensis","Pristidactylus_torquatus","Oplurus_cyclurus","Chalarodon_madagascariensis","Anolis_carolinensis","Uta_stansburiana","Sceloporus_variabilis","Petrosaurus_mearnsi","Uma_scoparia","Phrynosoma_platyrhinos","Polychrus_marmoratus","Phymaturus_palluma","Liolaemus_bellii","Liolaemus_elongatus","Leiocephalus_barahonensis"]
("Crotaphytus_collaris","Gambelia_wislizenii")
test=("Crotaphytus_collaris","Gambelia_wislizenii")
tree.is_monophyletic("Crotaphytus_collaris","Gambelia_wislizenii")




    
    """