# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:08:41 2015

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

def merg_dicts(dic1,dic2):
    dic3={}
    for key in dic1:
        if key not in dic2:
            dic3[key]=dic1[key]
        if key in dic2:
            d3=[] #create new list so original lists don't get changed
            d3.extend(dic1[key]) #add values from dict1 and dict2 to new list
            d3.extend(dic2[key])
            dic3[key]=d3 #add key and now concatenated value to new dict
    return dic3 #tested len(dic3.keys())=45 so all good. (44 + gene)    
            
len(merg_dicts(TL,TLrr)) 

LHs=FiletoDict(path='/Users/ChatNoir/bin/Squam/data_files/tree_lens_3.23.15/20Garli_LHs.txt')
tree_lens=FiletoDict(path='/Users/ChatNoir/bin/Squam/data_files/tree_lens_3.23.15/20Garli_tree_lens.txt')
LHsrr=FiletoDict(path='/Users/ChatNoir/bin/Squam/data_files/tree_lens_3.23.15/20Garli_LHs_rr.txt')
tree_lensrr=FiletoDict(path='/Users/ChatNoir/bin/Squam/data_files/tree_lens_3.23.15/20Garli_tree_lens_rr.txt')

LH,TL,LHrr,TLrr=0,0,0,0

LH=LHs.make_dic()
TL=tree_lens.make_dic()
LHrr=LHsrr.make_dic()
TLrr=tree_lensrr.make_dic()
print LH

d1=LH['AHR']
TL['AHR']
d2=LHrr['AHR']
TLrr['AHR']
print d2
print d1
d3=d1.extend(d2)
print d1
print d3
d1=[]
d2=[]
d3=[]

dic1=LH
dic2=LHrr
dic3={}
for key in dic1:
    if key not in dic2:
        dic3[key]=dic1[key]
    if key in dic2:
        d3=[] #create new list so original lists don't get changed
        d3.extend(dic1[key]) #add values from dict1 and dict2 to new list
        d3.extend(dic2[key])
        dic3[key]=d3 #add key and now concatenated value to new dict
    print dic3.keys() #tested len(dic3.keys())=45 so all good. (44 + gene)        
        

print dic3.keys()       
        
    look up in first one
    if it is there, concat values. :
        
        proof of princicple. how to address if molec results are reliable. 
        
        
"""
FML none of this worked. 
    
#copied from http://stackoverflow.com/questions/16458340/python-equivalent-of-zip-for-dictionaries
#takes n dictionaries and zips together values with common keys
def zip_dicts(da,db):
    for i in set(da).intersection(db):
        print i
        #if key in set(dics[0]).intersection(*dics[1:]):
         #   return key 
            
def OG_zip_dicts(*dics):
    for i in set(dics[0]).intersection(*dics[1:]):
        yield (i,) + tuple(d[i] for d in dics)  
    a=list(OG_zip_dicts(*dics))
    return a

da = {'a': 1, 'b': 2, 'c': 3, 'd': 7}
db = {'a': 4, 'b': 5, 'c': 6}
cd=da.copy()
cd.update(db)
print cd
c=dict(da,**db)

z = dict(da.items() + db.items())
print z
for i in set(da).intersection(db):
    print i,da[i],db[i]

dc=set(da) & set(db)
print dc


OG_zip_dicts(da, db)
zip_dicts(da,db)
list(OG_zip_dicts(da, db))
print p
"""       
 