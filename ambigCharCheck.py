#! /usr/bin/env python
import os
import glob
from Bio import SeqIO

#outFile = open('ambigCharCount.tsv', 'a')


for t in glob.glob('*.nex'):
	gene = t.split("_")[0]
	nex=open(t,'rU')
	M = 0
	R = 0
	W = 0
	S = 0
	Y = 0
	K = 0
	V = 0
	H = 0
	D = 0
	B = 0
	N = 0
	total = 0
	ambMax = 0
	for seq_record in SeqIO.parse(nex, "nexus"):
		M += seq_record.seq.count("M")
		R += seq_record.seq.count("R")
		W += seq_record.seq.count("W")
		S += seq_record.seq.count("S")
		Y += seq_record.seq.count("Y")
		K += seq_record.seq.count("K")
		V += seq_record.seq.count("V")
		H += seq_record.seq.count("H")
		D += seq_record.seq.count("D")
		B += seq_record.seq.count("B")
		N += seq_record.seq.count("N")
		total += len(seq_record.seq)
		#if y > 0:
			#print seq_record.id,y
	ambigs = sum((M,R,W,S,Y,K,V,H,D,B,N))
	percent = round((float(ambigs)/float(total))*100, 3)
	print gene,M,R,W,S,Y,K,V,H,D,B,N,ambigs,percent,"%"

