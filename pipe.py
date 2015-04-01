#!/usr/bin/env python

import os
import subprocess
from split_concat_nexus import split_nexus
from split_concat_nexus import rename

split_nexus("squam_char.nex","squamg")
#looking through file with data and char set. then making one file per gene with the prefix squam_ 

rename("squamg")
#adding .nex to file names

#lists everything in directory. points to current working directory (where the script is running from)
for f in os.listdir(os.getcwd()):
        if f.startswith("squamg_"): #add something about it not being able to end with nex already
        	filename=os.path.splitext(f)[0] #take off the .nex 
                os.makedirs(filename) #create a folder with the name of the filename minus the .nex

#write all nexus filenames starting with "squamg" to txt file        
        x = open("dataList.txt","a")
        if f.startswith("squamg"):
        	x.write(f)
        	x.write('\n')
        x.close()

#os.path.abspath(file) prints path of the file


subprocess.call("./run_jmodel.sh")

#subprocess.call("./modelSetConf.sh")
