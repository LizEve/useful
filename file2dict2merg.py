# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:44:36 2015

@author: ChatNoir

Assumptions:
two files each with ONLY one line that is formatted like a dictionary with keys and values and {}

"""

import time
import os
import ast

"""
takes 2 dictionaries, checks for any keys that are unique, then combines values for each key as a list
output=one dictionary with a list for each key. key:[dic1value,dic2value]
"""
def merg_dicts(dic1,dic2):
    dic3={}
    for key in dic1:
        if key not in dic2:
            print "you are missing values for",key,"in the second dictionary"
        if key in dic2:
            val=[dic1[key],dic2[key]]
            #print val
            dic3[key]=val
    for key in dic2:
        if key not in dic1:
            print "you are missing",key,"in the first dictionary"
    return dic3

"""
takes a file with a dictionary in it, starting with {
outputs a dictionary object in python
"""
def filetodict(fname):     
    fpath=os.path.abspath(fname)
    dict1={}
    for line in open(fpath,'r'):
        if line.startswith('{'):
            dict1=ast.literal_eval(line)
        return dict1    

#demand user input
f1=input("name of file containing dictionary:") 
f2=input("name of file containing dictionary:") 
output_file=input("output file name:")

#convert files to dictionaries
dict1=filetodict(f1)
print "Dictionary 1: "+f1+'='+str(dict1)
dict2=filetodict(f2)
print "Dictionary 2: "+f2+'='+str(dict2)

#merge
bigd=merg_dicts(dict1,dict2)
datetime="Current date & time of run " + time.strftime("%c")


#write info to file
outfile=open(output_file, 'w+')
outfile.write(str(bigd))
outfile.write('\n')
outfile.write(datetime)
outfile.write('\n')
info='Merged dictionaries from '+f1+" and "+f2
outfile.write(info)
outfile.close()


'''
RF={'ADNP': 209, 'MSH6': 204, 'MLL3': 282, 'BDNF': 173, 'SLC30A1': 174, 'GPR37': 227, 'NGFB': 157, 'CILP': 213, 'CAND1': 183, 'PRLR': 282, 'BACH1': 292, 'FSTL5': 212, 'MKL1': 189, 'BHLHB2': 265, 'UBN1': 289, 'CXCR4': 185, 'SLC8A1': 144, 'R35': 177, 'SLC8A3': 189, 'CARD4': 146, 'TRAF6': 161, 'FSHR': 176, 'ZFP36L1': 216, 'DLL1': 263, 'SINCAIP': 218, 'RAG1': 210, 'INHIBA': 255, 'GHSR': 285, 'ZEB2': 181, 'VCPIP1': 212, 'BMP2': 219, 'HLCS': 199, 'ECEL': 259, 'AKAP9': 248, 'LRRN1': 241, 'AHR': 260, 'PTGER4': 266, 'GALR1': 226, 'NKTR': 265, 'ENC1': 185, 'PNN': 205, 'LZTSS1': 298, 'PTPN': 261, 'NTF': 190}
TL={'ADNP': 4.995, 'PNN': 6.387, 'MSH6': 6.492, 'MLL3': 9.602, 'BDNF': 4.387, 'SLC30A1': 6.834, 'GPR37': 4.945, 'NGFB': 6.328, 'ZEB2_ZFHX1B': 3.334, 'CILP': 12.131, 'CAND1': 2.758, 'PRLR': 10.453, 'BACH1': 6.273, 'FSTL5': 3.899, 'MKL1': 7.375, 'BHLHB2': 5.138, 'UBN1': 10.055, 'CXCR4': 7.4, 'SLC8A1': 4.547, 'R35': 9.469, 'SLC8A3': 5.54, 'CARD4': 8.643, 'TRAF6': 6.347, 'FSHR': 7.702, 'ZFP36L1': 5.301, 'DLL1': 6.114, 'SINCAIP': 5.859, 'RAG1': 5.058, 'INHIBA': 5.605, 'GHSR': 6.479, 'VCPIP1': 4.645, 'BMP2': 6.251, 'HLCS': 7.883, 'ECEL': 16.538, 'AKAP9': 6.927, 'LRRN1': 4.081, 'AHR': 7.703, 'PTGER4': 6.987, 'GALR1': 6.61, 'NKTR': 11.308, 'ENC1': 3.872, 'NTF_3': 6.954, 'LZTSS1': 5.765, 'PTPN': 8.114}
x=merg_dicts(RF,TL)
print x
'''       
"""
TESTING
dic1={'A': 4.995, 'B': 6.387, 'C': 6.492, 'D': 9.602, 'E': 4.387, 'F': 6.834}
dic2={'A': 209, 'F': 204, 'E': 282, 'B': 173, 'C': 174, 'D': 227, 'NGFB': 157}
x=merg_dicts(dic1,dic2)
print x
"""
