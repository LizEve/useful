
import os
import glob
import csv
from itertools import izip_longest

# Create list of all loci
loci_list=[]
with open("allloci.txt") as all_loci:
	for loci in all_loci:
		if loci.strip():
			loci_list.append(loci.strip())

# Initialize with loci as keys and empty lists as values
loci_dict= {k: [] for k in loci_list}



# Iterate through all taxa files
for file in glob.glob("*_*.txt"):
	taxa_name = os.path.splitext(file)[0]
	# Open taxa file
	with open(file) as open_file:
		# Iterate through each loci for that taxa
		for line in open_file:
			taxa_loci = line.strip()
			if taxa_loci in loci_dict:
				loci_dict[taxa_loci].append(taxa_name)


# Sort dictionary by length of lists?

# From http://stackoverflow.com/questions/23613426/write-dictionary-of-lists-to-a-csv-file
with open('text.csv','wb') as outfile:
	writer = csv.writer(outfile, delimiter = ',')
	writer.writerow(loci_dict.keys())
	writer.writerows(izip_longest(*loci_dict.values()))

