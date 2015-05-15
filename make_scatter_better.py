# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:40:33 2015

@author: ChatNoir
"""

import numpy as np
import matplotlib.pyplot as plt

bigd={'ADNP': [209, 4.995], 'PNN': [205, 6.387], 'MSH6': [204, 6.492], 'MLL3': [282, 9.602], 'BDNF': [173, 4.387], 'SLC30A1': [174, 6.834], 'GPR37': [227, 4.945], 'NGFB': [157, 6.328], 'ZEB2_ZFHX1B': [181, 3.334], 'CILP': [213, 12.131], 'CAND1': [183, 2.758], 'PRLR': [282, 10.453], 'BACH1': [292, 6.273], 'FSTL5': [212, 3.899], 'MKL1': [189, 7.375], 'BHLHB2': [265, 5.138], 'UBN1': [289, 10.055], 'FSHR': [176, 7.702], 'SLC8A1': [144, 4.547], 'R35': [177, 9.469], 'SLC8A3': [189, 5.54], 'CARD4': [146, 8.643], 'TRAF6': [161, 6.347], 'CXCR4': [185, 7.4], 'ZFP36L1': [216, 5.301], 'DLL1': [263, 6.114], 'SINCAIP': [218, 5.859], 'RAG1': [210, 5.058], 'INHIBA': [255, 5.605], 'GHSR': [285, 6.479], 'VCPIP1': [212, 4.645], 'BMP2': [219, 6.251], 'HLCS': [199, 7.883], 'ECEL': [259, 16.538], 'AKAP9': [248, 6.927], 'LRRN1': [241, 4.081], 'AHR': [260, 7.703], 'PTGER4': [266, 6.987], 'GALR1': [226, 6.61], 'NKTR': [265, 11.308], 'ENC1': [185, 3.872], 'NTF_3': [190, 6.954], 'LZTSS1': [298, 5.765], 'PTPN': [261, 8.114]}

x_val = [bigd[x][0] for x in bigd]
y_val = [bigd[x][1] for x in bigd]
dkeys=bigd.keys()




data = bigd
print data
labels = dkeys
#plt.subplots_adjust(bottom = 0.1)
plt.scatter(x_val, y_val, marker = 'o')
for label, x, y in zip(labels, x_val, y_val):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom', 
        bbox = dict(boxstyle = 'round,pad=0.3', fc = 'teal', ec='teal', alpha = 0.1),
        arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=0'))

plt.show()


"""
Help- 
http://matplotlib.org/api/text_api.html#matplotlib.text.Annotation
http://matplotlib.org/users/annotations_guide.html
bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5)
arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'