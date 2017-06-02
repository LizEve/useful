
import sys
import os
from tempfile import mkstemp
from shutil import move, copyfile
# Testing on cluster. didnt work. 
def edit_file(inputFileEditPath,change):
	# Add comment blocks that number each tree with the indices used by TreeScaper. Pulled from AffinityCommunities.py
	inputFileEdit = open(inputFileEditPath, 'r')
	lineNum = 1
	# make a temp file
	fh, absPath = mkstemp()
	tempFile = open(absPath,'w')
	for line in inputFileEdit:
		if line.find('_taco') != -1:
			tempFile.write(line.replace('_taco','_'+str(change)))
		else:
			tempFile.write(line)
	# close temp file
	tempFile.close()
	os.close(fh)
	inputFileEdit.close()
	# Remove original file
	os.remove(inputFileEditPath)
	# Move new file
	move(absPath, inputFileEditPath)
	return lineNum

