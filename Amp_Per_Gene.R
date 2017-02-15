library(ggplot2)
library(RColorBrewer)

setwd("/Users/ChatNoir/Projects/Squam/RevBayes/FinalAmp/ampOut")
graphStats <- function(x,data) {
  # pull out column name and reformat into title
  # list stored in a list, so you have to double index to get into the string with [[1]], then you get the piece you want
  colName=colnames(data[x])
  stat=strsplit(colName,".",fixed=T)[[1]][3][5:6] 
  statName = paste(stat, collapse = " ")
  #title=paste(gene,"-",statName)
  pp = data[1:96,x]
  # get emp value
  emp = data[97,x]
  # get max and min data values
  maxpp = max(data[,x])
  minpp = min(data[,x])
  # calculate number of bins for histogram
  s=((maxpp-minpp)/20)
  bins = c(seq(minpp,maxpp,s))
  name=colnames(data[x])
  # list stored in a list, so you have to double index to get into the string with [[1]]
  # then you get the piece you want
  preTitle=strsplit(name,".",fixed=T)[[1]][3:6]
  title=paste(preTitle, collapse = " ")
  # set size of plot, bottom, left, top, right
  par(mar=c(1.5,1.5,1,1.5))
  # set axis lables. location of lables, tick mark lables, tick marks
  par(mgp=c(3,0.15,0))
  hist(pp, col="MediumPurple3", main=title, xlab=NA, ylab=NA, tck = -.02,
       breaks=bins, cex.axis=0.7, cex.main=0.9, yaxt='n')
  abline(v=emp,col="orange", lwd=3)
}
readData <- function(geneAmpStats) {
    #read in data
    d <- read.table(geneAmpStats, header=TRUE, sep=",")
    # get gene name
    g <- strsplit(geneAmpStats,"_",fixed=T)[[1]][1]
    #name output graph file
    fname <- paste(paste("Stats", g, sep="_"),"pdf", sep=".")
    # open pdf file
    pdf(file=fname)
    # set outer margins
    # bottom, left, top, right
    par(oma=c(2,2,3,2))
    # set number of rows and columns
    par(mfrow=c(5,3))
    # numbers to iterate through, represent columns in dataset. 
    nums=seq(2,15,1)
    for (n in nums){graphStats(n,d)}
    #add title and outer lables for axes
    mtext(g, outer = TRUE, cex = 1.5, line=0)
    mtext(text="Summary Statistic Value",side=1,line=0,outer=TRUE)
    mtext(text="Frequency",side=2,line=0,outer=TRUE)
    dev.off()
  }
  
files <- list.files(pattern = "csv")

for (f in files){readData(f)}

#Graphing deets
#open file
#pdf(file='XXX.pdf')
#parses graphing space into 3 rows and 1 column
#par(mfrow=c(3,1))
#dev.off()
############################################################################################################################################

setwd("/Users/ChatNoir/Projects/Squam/RevBayes/Amp_Results/AmpOut")

genes <- c("ADNP", "AHR", "AKAP9", "BACH1", "BDNF", "BHLHB2", "BMP2", "CAND1")
genes <- c("CARD4", "CILP", "CXCR4", "DLL1", "ECEL", "ENC1", "FSHR", "FSTL5")
genes <- c("GALR1", "GHSR", "GPR37", "HLCS")
genes <- c("INHIBA", "LRRN1", "LZTSS1", "MKL1")
genes <- c("MLL3", "MSH6", "NGFB", "NKTR", "NTF", "PNN", "PRLR", "PTGER4", "PTPN")
genes <- c("R35", "RAG1", "SINCAIP", "SLC30A1", "SLC8A1", "SLC8A3", "TRAF6", "UBN1")
genes <- c("VCPIP1", "ZEB2", "ZFP36L1")

sapply(genes, makeTree)