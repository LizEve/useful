# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:40:05 2015

@author: ChatNoir
"""

from Bio import Phylo

rt='/Users/ChatNoir/bin/Squam/data_files/taxa150/reeder_jspheno_150_raxml_nbl.phy'
mt='/Users/ChatNoir/bin/Squam/data_files/taxa150/mount_jspheno_150_raxml_nbl.phy'

RE = Phylo.read(rt, "newick")
MO = Phylo.read(mt, "newick")

