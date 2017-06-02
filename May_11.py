#! /usr/bin/env python
import os
import glob
from Bio import SeqIO

mainDir = os.getcwd()

with open('Species_IDs.txt', 'w') as sp_ids:
	for in_file in glob.glob('*.fasta'):
		species = in_file.split('.')[0]
		if not os.path.exists(species):
			os.makedirs(species)
		sp_dir = os.path.join(mainDir,species)
		fasta_sequences = SeqIO.parse(open(in_file),'fasta')
		for fasta in fasta_sequences:
		    #sequence = str(fasta.seq)
			locus = str(fasta.description.split()[0])
			#taxa_id = str((fasta.description.split()[1]).split('_')[0])
			#print(taxa,locus)
			locus_empty = os.path.join(sp_dir,locus)
			open(locus_empty, 'a').close()
		#sp_ids.write(species + " - " + taxa_id + '\n')



### Not used
'''
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
new_seq = Seq(sequence)
new_seq_rec = SeqRecord(new_seq)
new_seq_rec.id = taxa_id
with open(locus) as out_file:
	SeqIO.write(new_seq_rec, out_file, "nexus")
'''