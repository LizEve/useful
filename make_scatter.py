# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:55:20 2015

@author: ChatNoir
"""
from __future__ import division
import matplotlib.pyplot as plt
import os
import ast
import numpy as np



def filetodict(fname):     
    fpath=os.path.abspath(fname)
    dict1={}
    for line in open(fpath,'r'):
        if line.startswith('{'):
            dict1=ast.literal_eval(line)
        return dict1    



#user input
#xax=input('x axis label:')
#yax=input('y axis label:')
xax='Tree Len'
yax='RF weighted'
title=input('title of graph:')
infile=input('file containing dictionary. ex:{"key":[x,y]}:')
outfilename=input('output file name:')

#direct output
fpath=os.path.abspath(infile)
outpath=os.path.dirname(fpath)
outfile=outpath+'/'+outfilename

#import dictionary of paired values
bigd=filetodict(infile)

xv = [bigd[x][0] for x in bigd]
yv = [bigd[x][1] for x in bigd]
print xv
print yv
x_val = np.array(xv)
y_val = np.array(yv)

plt.scatter(x_val,y_val,color='teal',s=10, edgecolor='none')
plt.xlabel(xax)
plt.ylabel(yax)
plt.title(title)


# determine best fit line (stolen from stackoverflow)
par = np.polyfit(x_val, y_val, 1, full=True)
slope=par[0][0]
intercept=par[0][1]
xl = [min(x_val), max(x_val)]
yl = [slope*xx + intercept  for xx in xl]
plt.plot(xl, yl, '-r')

# coefficient of determination, plot text (stolen from stackoverflow)
variance = np.var(y_val)
residuals = np.var([(slope*xx + intercept - yy)  for xx,yy in zip(x_val,y_val)])
Rsqr = np.round(1-residuals/variance, decimals=2)
plt.text(.9*max(x_val)+.1*min(x_val),.9*max(y_val)+.1*min(y_val),'$R^2 = %0.2f$'% Rsqr, fontsize=15,bbox=dict(facecolor='blue', alpha=0.1))

#y=mx+b eqn
mm, bb = np.polyfit(x_val, y_val, 1)
m=str(round(mm,3))
b=str(round(bb,3))
eqn= 'y = '+m+'x + '+b
print eqn
plt.text(.9*max(x_val)+.1*min(x_val),.8*max(y_val)+.1*min(y_val),eqn, fontsize=12, bbox=dict(facecolor='blue', alpha=0.1))


plt.plot(xl, yl, '-r')
plt.savefig(outfile)
plt.show()


#add data labels

"""
dkeys=bigd.keys()
data = bigd
labels = dkeys
#plt.subplots_adjust(bottom = 0.1)
for label, x, y in zip(labels, x_val, y_val):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom', 
        bbox = dict(boxstyle = 'round,pad=0.3', fc = 'teal', ec='teal', alpha = 0.5),
        arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=0'))
"""
"""
fc= face color
ec=edge color 
alpha = transperency of dots
xytext= how far away txt is
testcords= where box goes
"""




"""
::RESOURCES::
_____Labeling Points______
http://matplotlib.org/api/text_api.html#matplotlib.text.Annotation
http://matplotlib.org/users/annotations_guide.html
bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5)
arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'

______Trend line_______
http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html
http://stackoverflow.com/questions/22239691/code-for-line-of-best-fit-of-a-scatter-plot-in-python

::TESTING::
bigd={'ADNP': [209, 4.995], 'PNN': [205, 6.387], 'MSH6': [204, 6.492], 'MLL3': [282, 9.602], 'BDNF': [173, 4.387], 'SLC30A1': [174, 6.834], 'GPR37': [227, 4.945], 'NGFB': [157, 6.328], 'ZEB2_ZFHX1B': [181, 3.334], 'CILP': [213, 12.131], 'CAND1': [183, 2.758], 'PRLR': [282, 10.453], 'BACH1': [292, 6.273], 'FSTL5': [212, 3.899], 'MKL1': [189, 7.375], 'BHLHB2': [265, 5.138], 'UBN1': [289, 10.055], 'FSHR': [176, 7.702], 'SLC8A1': [144, 4.547], 'R35': [177, 9.469], 'SLC8A3': [189, 5.54], 'CARD4': [146, 8.643], 'TRAF6': [161, 6.347], 'CXCR4': [185, 7.4], 'ZFP36L1': [216, 5.301], 'DLL1': [263, 6.114], 'SINCAIP': [218, 5.859], 'RAG1': [210, 5.058], 'INHIBA': [255, 5.605], 'GHSR': [285, 6.479], 'VCPIP1': [212, 4.645], 'BMP2': [219, 6.251], 'HLCS': [199, 7.883], 'ECEL': [259, 16.538], 'AKAP9': [248, 6.927], 'LRRN1': [241, 4.081], 'AHR': [260, 7.703], 'PTGER4': [266, 6.987], 'GALR1': [226, 6.61], 'NKTR': [265, 11.308], 'ENC1': [185, 3.872], 'NTF_3': [190, 6.954], 'LZTSS1': [298, 5.765], 'PTPN': [261, 8.114]}


bigd=0
x_val=0
y_val=0


bigd={'ADNP': [1.1, 100], 'PNN': [2.2, 200], 'MSH6': [3.3, 300], 'MLL3': [4.4, 400], 'BDNF': [5.5, 500]}

x_val = [bigd[x][0] for x in bigd]
y_val = [bigd[x][1] for x in bigd]

print x_val[0]
print y_val


Stuff I didn't use----------

# error bounds
yerr = [abs(slope*xx + intercept - yy)  for xx,yy in zip(x_val,y_val)]
par = np.polyfit(x_val, yerr, 2, full=True)

yerrUpper = [(xx*slope+intercept)+(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(x_val,y_val)]
yerrLower = [(xx*slope+intercept)-(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(x_val,y_val)]

plt.plot(x_val, yerrLower, '--r')
plt.plot(x_val, yerrUpper, '--r')


fig = plt.figure()
ax1 = fig.add_subplot(121)

## the data
N=1000
x = np.random.randn(N)
y = np.random.randn(N)

## left panel
plt.scatter(x,y,color='blue',s=5,edgecolor='none')
ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square

"""
