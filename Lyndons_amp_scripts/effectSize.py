import numpy as np
import glob


files = glob.glob("amp-results/*.out")

genes = []
genes.append("gene")
for f in files :
    genes.append(f.split("/")[-1])

allResults = []
allResults.append(genes)
testStatistics = ["Posterior Predictive 1-th 10000-quantile Test Statistics:",
"Posterior Predictive 1-th 1000-quantile Test Statistics:",
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
            
            if parsing :
                if line != "\n" :
                    localStats.append(line.strip())
            tracker += 1
        allStats.append(localStats)




    ## calculate the effect size of each value
    ## in this case it's just (empirical - median) / standard deviation

    tracker = 0
    for stat in allStats :
        values = stat[1:]
        values = [float(x) for x in values]
        median = np.median(values)
        sd = np.std(values)
        if sd == 0 :
            effectSize = 0.0
        else :
            effectSize = (float(empValues[tracker]) - median) / sd

        allResults[tracker+1].append(str(abs(effectSize)))
        tracker += 1


allRows = []

for n in range(0, len(allResults[0])) :
    row = "\t".join([item[n] for item in allResults])
    allRows.append(row)

outHandle = open('chiari_effect_sizes.tsv', 'a')

for r in allRows :
    outHandle.write(r + "\n")

outHandle.close()