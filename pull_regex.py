#! /usr/bin/env python
import os
import glob
import re


files = glob.glob('*.nex')
pattern = re.compile('^\t*dimensions(.+)')
findDict = {}
findList = []
max = int(2164)
min = int(155)

for f in files :
	# Get first section parsed by "."
	fileName = str(f)
	fileNameIndex = fileName.find(".")
	fileNameTrunc = fileName[:fileNameIndex]
	# Open file and grab pattern match
	openFile = open(f,'r')
	for line in openFile:
		m = pattern.match(line)
		# If it matches
		if m:
			# Pull out the string from the match
			x = m.group(0)
			# Grab part you want
			y = int(x.split("=")[2].strip(";"))
			findList.append(y)
			if y == max:
				print(fileNameTrunc+" : "+str(y))
			elif y == min:
				print(fileNameTrunc+" : "+str(y))


max(findList)
min(findList)
