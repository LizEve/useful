import dendropy as dp
import glob

inputFile = '.T FILE TO CHECK'

bad_count = 0
tree_list = dp.TreeList.get(path=inputFile, schema="nexus")
taxa_list = []
handle = open('taxa_list.txt', 'r') ## a list of taxa expected in the monophyletic clade

for line in handle :
	taxa_list.append(line.strip())

count = 1
for tree in tree_list :
	mono_nodes = []
	mono_nodes.append(dp.Tree.mrca(tree, taxon_labels=taxa_list))
	for node in mono_nodes :
		if node != tree.seed_node :
			print tree
			print "FOUND ONE"
			print "-" * 100
			bad_count += 1

if bad_count < 1 :

	print "No trees were found with monophyletic clades."
	
else :

	print "Bad trees found!!!. Check previous messages!"