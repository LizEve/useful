rm(list=ls())

#import mrbayes log files
setwd("/Users/ChatNoir/Projects/Squam/pp_all_genes")
# skip first line in .p files
mbRun1 <- read.delim("LZTSS1/LZTSS1.nex.run1.p", stringsAsFactors=F, skip = 1)
mbRun2 <- read.delim("LZTSS1/LZTSS1.nex.run2.p", stringsAsFactors=F, skip = 1)
mbRun3 <- read.delim("LZTSS1/LZTSS1.nex.run3.p", stringsAsFactors=F, skip = 1)
mbRun4 <- read.delim("LZTSS1/LZTSS1.nex.run4.p", stringsAsFactors=F, skip = 1)
#check names
names(mbRun1)
#plot all three rates
plot(mbRun1$Gen,mbRun1$alpha.1.,type="l",col="darkgreen", ylim=c(0.3,8.5))
par(new=TRUE)
plot(mbRun1$Gen,mbRun1$alpha.2.,type="l",col="darkblue", ylim=c(0.3,8.5))
par(new=TRUE)
plot(mbRun1$Gen,mbRun1$alpha.3.,type="l",col="darkred", ylim=c(0.3,8.5))

#move to revbays .var files
setwd("/Users/ChatNoir/Projects/Squam/RevBayes\ 2/LZTSS1/output_0329")

rbRun1 <- read.delim("LZTSS1_posterior_run_1.var",stringsAsFactors=F)
rbRun2 <- read.delim("LZTSS1_posterior_run_2.var", stringsAsFactors=F)
rbComb <- read.delim("LZTSS1_posterior.var", stringsAsFactors=F)
#check names and list all up until the total number of columns in the file
str(rbComb, list.len = ncol(rbComb))

#compare across codon positions
plot(rbRun1$Iteration ,rbRun1$alpha.1.,type="l",col="darkgreen", ylim=c(0.3,8.5))
par(new=TRUE)
plot(rbRun1$Iteration ,rbRun1$alpha.2.,type="l",col="darkblue", ylim=c(0.3,8.5))
par(new=TRUE)
plot(rbRun1$Iteration ,rbRun1$alpha.3.,type="l",col="darkred", ylim=c(0.3,8.5))

#compare across runs
plot(rbComb$Iteration ,rbComb$alpha.2.,type="l",col="darkgreen", ylim=c(0.25,2))
par(new=TRUE)
plot(rbRun1$Iteration ,rbRun1$alpha.2.,type="l",col="darkblue", ylim=c(0.25,2))
par(new=TRUE)
plot(rbRun2$Iteration ,rbRun2$alpha.2.,type="l",col="darkred", ylim=c(0.25,2))
