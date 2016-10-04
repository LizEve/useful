import numpy as np
import glob
import csv

files = glob.glob("*.out")

genes = []
genes.append("gene")
for f in files :
    genes.append(f.split(".")[0])

allResults = []
allResults.append(genes)
testStatistics = ["Posterior Predictive 1-th 1000-quantile Test Statistics:",
"Posterior Predictive 1-th 100-quantile Test Statistics:",
"Posterior Predictive 1-th 20-quantile Test Statistics:",
"Posterior Predictive 1-th 10-quantile Test Statistics:",
"Posterior Predictive 1-th 8-quantile Test Statistics:",
"Posterior Predictive 1-th 6-quantile Test Statistics:",
"Posterior Predictive 1-th 4-quantile Test Statistics:",
"Posterior Predictive 2-th 4-quantile Test Statistics:",
"Posterior Predictive 3-th 4-quantile Test Statistics:",
"Posterior Predictive 99-th 100-quantile Test Statistics:",
"Posterior Predictive 999-th 1000-quantile Test Statistics:",
"Posterior Predictive 9999-th 10000-quantile Test Statistics:",
"Posterior Predictive Entropy-based Test Statistics:",
"Posterior Predictive Interquartile Range Test Statistics:",
"Posterior Predictive Mean Treelength Test Statistics:",
"Posterior Predictive Treelength Variance Test Statistics:"]

for t in testStatistics :
    temp = []
    temp.append(t.replace("Posterior Predictive ", "").replace(" Test Statistics:", " Effect Size"))
    allResults.append(temp)


# reads through lines, adds non empty lines to test stat 

for f in files :
    flist = open(f).readlines()
    allStats = []
    empValues = []
    for test in testStatistics :
        tracker = 0
        localStats = []
        parsing = False
        start = test
        stop = test.replace("Posterior Predictive", "Empirical").replace("Statistics", "Statistic")
        for line in flist : 
            if start in line :
                parsing = True
            elif stop in line :
                parsing = False
                empValue = flist[tracker + 2]
                empValues.append(empValue.strip())
                localStats.append(empValue.strip())
                #print f
                #qprint empValue
            if parsing :
                if line != "\n" :
                    localStats.append(line.strip())
            tracker += 1
        #print localStats
        #print empValues
        allStats.append(localStats)

        #print f 
        #print empValue
        #print empValues
        #print localStats
        r = len(allStats[0])
        rows=[]
        for j in range(r):
            rowj=str(j)
            for stat in allStats:
                rowj=rowj+','
                rowj=rowj+str(stat[j].strip(":"))
            rows.append(rowj)
        fname = f.split(".")[0]
        outName = fname+'_ampStats.csv'
        #outName='testOut_ampStats.csv'
        s = len(rows)
        with open(outName, 'wb') as out:
            for i in range(s):
                out.write(rows[i])
                out.write("\n")   


    tracker = 0
    for stat in allStats :
        values = stat[1:-1]
        values = [float(x) for x in values]
        median = np.median(values)
        sd = np.std(values)
        if sd == 0 :
            effectSize = 0.0
        else :
            effectSize = (float(empValues[tracker]) - median) / sd
        allResults[tracker+1].append(str(abs(effectSize)))
        #print "values "+str(fname)+" :"+str(values)
        #print "median "+str(fname)+" "+str(median)
        #print "sd "+str(fname)+" "+str(sd)
        #print "emp "+str(fname)+" "+str(empValues[tracker])
        #print "effectSize "+str(fname)+" "+str(effectSize)
        tracker += 1



allRows = []

for n in range(0, len(allResults[0])) :
    row = "\t".join([item[n] for item in allResults])
    allRows.append(row)

outHandle = open('Aug25_effect_sizes.tsv', 'a')

for r in allRows :
    outHandle.write(r + "\n")

outHandle.close()
