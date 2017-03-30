#! /usr/bin/env python

import dendropy 
import os

def rf_unweighted(tree1_path,tree2_path): 
	taxa = dendropy.TaxonNamespace() #set taxa same for all 
	tree1=dendropy.Tree.get_from_path(tree1_path,schema='nexus',taxon_namespace=taxa)
	tree2=dendropy.Tree.get_from_path(tree2_path,schema='nexus',taxon_namespace=taxa)
	tree1.encode_bipartitions()
	tree2.encode_bipartitions()
	dist=dendropy.calculate.treecompare.symmetric_difference(tree1,tree2)
	return dist

def euclid_dist(tree1_path,tree2_path): 
	taxa = dendropy.TaxonNamespace() #set taxa same for all 
	tree1=dendropy.Tree.get_from_path(tree1_path,schema='nexus',taxon_namespace=taxa)
	tree2=dendropy.Tree.get_from_path(tree2_path,schema='nexus',taxon_namespace=taxa)
	tree1.encode_bipartitions()
	tree2.encode_bipartitions()
	dist=dendropy.calculate.treecompare.euclidean_distance(tree1,tree2)
	return dist

def rf_weighted(tree1_path,tree2_path): 
	taxa = dendropy.TaxonNamespace() #set taxa same for all 
	tree1=dendropy.Tree.get_from_path(tree1_path,schema='nexus',taxon_namespace=taxa)
	tree2=dendropy.Tree.get_from_path(tree2_path,schema='nexus',taxon_namespace=taxa)
	tree1.encode_bipartitions()
	tree2.encode_bipartitions()
	dist=dendropy.calculate.treecompare.weighted_robinson_foulds_distance(tree1,tree2)
	return dist



