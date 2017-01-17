#! /usr/bin/env python
import os
import glob
from Bio import SeqIO
from Bio import Seq
from Bio import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

#outFile = open('ambigCharCount.tsv', 'a')


for t in glob.glob('*_misstxremoved.nex'):
	gene = t.split("_")[0]
	print gene
	nex=open(t,'rU')
	seqList=[]
	outfile=gene+"_masked.nex"    
	outnex=open(outfile,'w')
	print outfile
	for seq_record in SeqIO.parse(nex, "nexus"):
		# turn seq into string
		ambig_str = str(seq_record.seq)
		
		# search and replace for ambig chars
		mask_str = ambig_str.replace("M","?")
		mask_str = mask_str.replace("R","?")
		mask_str = mask_str.replace("W","?")
		mask_str = mask_str.replace("S","?")
		mask_str = mask_str.replace("Y","?")
		mask_str = mask_str.replace("K","?")
		mask_str = mask_str.replace("V","?")
		mask_str = mask_str.replace("H","?")
		mask_str = mask_str.replace("D","?")
		mask_str = mask_str.replace("B","?")
		mask_str = mask_str.replace("N","?")

		mask_seq = Seq(mask_str, IUPAC.unambiguous_dna)
		# replace seq with masked seq
		seq_record.seq = mask_seq
		# add to list 
		seqList.append(seq_record)
	SeqIO.write(seqList,outnex,"nexus")





