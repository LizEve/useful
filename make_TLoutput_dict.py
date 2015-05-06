# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:15:25 2015

@author: ChatNoir
"""
class FiletoDict(object):
    def __init__(self,path,dic=None,):
        self.dic=None
        self.path=path
        self.f=None
        
    def print_file(self):
        self.f=open(self.path,'r')
        contents=self.f.read()
        return contents  
        self.f.close()
        
    def make_dic(self):
        self.f=open(self.path,'r')
        self.dic={} #create a dictionary that will hold each gene name as a key, and a list of values as the values. 
        for line in self.f: #for each line in the file
            clean=line.strip() #clean the lines from weird space characters
            (key,val)=clean.split(":") #split the clean lines into key and string of values
            mylist=val.split(',') #split the string of values by ','
            val_list=[]    
            for num in mylist: 
                num=float(num) #change each value to a float instead of a string
                val_list.append(num) #add to a list
            self.dic[str(key)]=val_list #create dict
        return self.dic
        self.f.close()

tree_lens=FiletoDict(path='/Users/ChatNoir/bin/Squam/best_Garli_runs/best_trees/best_tree_lens_20run.txt')
TL=tree_lens.make_dic()
print TL
