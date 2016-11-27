# plot a tree with the tips colored by family
library(ape)
library(phytools)
library(geiger)

# function for making tree, pretty tree
makeTree <- function(gene) {
  inFile <- paste(gene,"_conSumt0.5.t", sep = "")
  tr <- read.nexus(inFile)
  outFile <- paste(gene,"_conSumt0.5.pdf", sep = "")
  
  # get tips for said tree
  tips <- tr$tip.label
  
  # search tips for your desired root-taxa
  roots <- c(grep(pattern="Alligator_mississippiensis",tips, value = TRUE),
             grep(pattern="Chelydra_serpentina",tips, value = TRUE),
             grep(pattern="Crocodylus_porosus",tips, value = TRUE),
             grep(pattern="Dromaius_novaehollandiae",tips, value = TRUE),
             grep(pattern="Gallus_gallus",tips, value = TRUE),
             grep(pattern="Mus_musculus",tips, value = TRUE),
             grep(pattern="Podocnemis_expansa",tips, value = TRUE),
             grep(pattern="Sphenodon_punctatus",tips, value = TRUE),
             grep(pattern="Tachyglossus_aculeatus",tips, value = TRUE),
             grep(pattern="Homo_sapiens",tips, value = TRUE))
  roots <- as.character(roots)
  
  # get node number for desired root
  root.node <- getMRCA(tr, roots)
  
  # root the tree
  tr.rooted <- root(tr,node=root.node)
  
  # read in your family data - this should be a tab-delimited text file:
  # taxon1  family1
  # taxon2  family2
  # etc
  # obviously, make sure your tip names and taxon names are spelled the same and stuff
  dat <- read.delim(file = "families.tsv", row.names = 1, header = F, stringsAsFactors = F,
                    col.names = c("taxon", "family"))
  
  # combine tree file and list of names, sort them
  comb <- treedata(tr.rooted,dat,sort = T,warnings = F)
  sort(comb$data)
  
  # make new lists and tree that are properly matched to each other
  # double check that all is well 
  dat2 <- comb$data
  tr2 <- comb$phy
  name.check(tr2,dat2)
  
  #make list of unique family names
  unq <- unique(dat2[,1])
  
  # make a new data list replacing family names with colors
  dat3 <- dat2
  
  # replace specific familes with specific colors
  dat3 <- gsub(pattern = "Serpentes" ,replacement = "darkorchid4", dat3)
  dat3 <- gsub(pattern = "Scolecophidia" ,replacement = "mediumslateblue", dat3)
  dat3 <- gsub(pattern = "Teioidea" ,replacement = "blue3", dat3)
  dat3 <- gsub(pattern = "Amphisbaenia" ,replacement = "firebrick3", dat3)
  dat3 <- gsub(pattern = "Lacertoidea" ,replacement = "darkgoldenrod2", dat3)
  dat3 <- gsub(pattern = "Anguimorpha" ,replacement = "darkorange3", dat3)
  dat3 <- gsub(pattern = "Dibamidae" ,replacement = "chocolate4", dat3)
  dat3 <- gsub(pattern = "Gekkota" ,replacement = "chartreuse3", dat3)
  dat3 <- gsub(pattern = "Outgroup" ,replacement = "gray50", dat3)
  dat3 <- gsub(pattern = "Scincoidea" ,replacement = "dodgerblue", dat3)
  dat3 <- gsub(pattern = "Iguania" ,replacement = "darkgreen", dat3)
  
  col <- unique(dat3[,1])
  
  # open pdf file
  pdf(outFile, height = 9, width = 7)
  
  # plot the tree with the tips labeled with taxon names
  
  plot.phylo(tr2,  show.tip.label = F, no.margin = F)
  
  # cex controls the size of the text, label.offset controls how far from the tip the name is
  
  # now add dots to the tips, colored by family name
  
  tiplabels(tr2$tip.label, adj = -0.7, cex = 0.05, frame= "rect", bg=dat3)
  #tiplabels(tr2$tip.label, cex = 0.2, pie = to.matrix(family.dat2, piecol=family.dat3)
  
  # plot legend
  #legend(x=35, text.col = col, legend = unq, cex = 1, text.width = 30, text.font = 2)
  
  # plot title
  title(gene)
  
  #close pdf 
  dev.off()
  
}

makeTree_con <- function(gene) {
  inFile <- paste(gene,"_conSumt0.5.t", sep = "")
  tr <- read.nexus(inFile)
  outFile <- paste(gene,"_conSumt0.5.pdf", sep = "")
  
  # get tips for said tree
  tips <- tr$tip.label
  
  # search tips for your desired root-taxa
  roots <- c(grep(pattern="Alligator_mississippiensis",tips, value = TRUE),
             grep(pattern="Chelydra_serpentina",tips, value = TRUE),
             grep(pattern="Crocodylus_porosus",tips, value = TRUE),
             grep(pattern="Dromaius_novaehollandiae",tips, value = TRUE),
             grep(pattern="Gallus_gallus",tips, value = TRUE),
             grep(pattern="Mus_musculus",tips, value = TRUE),
             grep(pattern="Podocnemis_expansa",tips, value = TRUE),
             grep(pattern="Sphenodon_punctatus",tips, value = TRUE),
             grep(pattern="Tachyglossus_aculeatus",tips, value = TRUE),
             grep(pattern="Homo_sapiens",tips, value = TRUE))
  roots <- as.character(roots)
  
  # get node number for desired root
  root.node <- getMRCA(tr, roots)
  
  # root the tree
  tr.rooted <- root(tr,node=root.node)
  
  # read in your family data - this should be a tab-delimited text file:
  # taxon1  family1
  # taxon2  family2
  # etc
  # obviously, make sure your tip names and taxon names are spelled the same and stuff
  dat <- read.delim(file = "families.tsv", row.names = 1, header = F, stringsAsFactors = F,
                    col.names = c("taxon", "family"))
  
  # combine tree file and list of names, sort them
  comb <- treedata(tr.rooted,dat,sort = T,warnings = F)
  sort(comb$data)
  
  # make new lists and tree that are properly matched to each other
  # double check that all is well 
  dat2 <- comb$data
  tr2 <- comb$phy
  name.check(tr2,dat2)
  
  #make list of unique family names
  unq <- unique(dat2[,1])
  
  # make a new data list replacing family names with colors
  dat3 <- dat2
  
  # replace specific familes with specific colors
  dat3 <- gsub(pattern = "Serpentes" ,replacement = "darkorchid4", dat3)
  dat3 <- gsub(pattern = "Scolecophidia" ,replacement = "mediumslateblue", dat3)
  dat3 <- gsub(pattern = "Teioidea" ,replacement = "blue3", dat3)
  dat3 <- gsub(pattern = "Amphisbaenia" ,replacement = "firebrick3", dat3)
  dat3 <- gsub(pattern = "Lacertoidea" ,replacement = "darkgoldenrod2", dat3)
  dat3 <- gsub(pattern = "Anguimorpha" ,replacement = "darkorange3", dat3)
  dat3 <- gsub(pattern = "Dibamidae" ,replacement = "chocolate4", dat3)
  dat3 <- gsub(pattern = "Gekkota" ,replacement = "chartreuse3", dat3)
  dat3 <- gsub(pattern = "Outgroup" ,replacement = "gray50", dat3)
  dat3 <- gsub(pattern = "Scincoidea" ,replacement = "dodgerblue", dat3)
  dat3 <- gsub(pattern = "Iguania" ,replacement = "darkgreen", dat3)
  
  col <- unique(dat3[,1])
  
  # open pdf file
  pdf(outFile, height = 9, width = 7)
  
  # plot the tree with the tips labeled with taxon names
  
  plot.phylo(tr2,  show.tip.label = F, no.margin = F)
  
  # cex controls the size of the text, label.offset controls how far from the tip the name is
  
  # now add dots to the tips, colored by family name
  
  tiplabels(tr2$tip.label, adj = -0.7, cex = 0.05, frame= "rect", bg=dat3)
  #tiplabels(tr2$tip.label, cex = 0.2, pie = to.matrix(family.dat2, piecol=family.dat3)
  
  # plot legend
  # legend(x=35, text.col = col, legend = unq, cex = 1, text.width = 30, text.font = 2)
  
  # plot title
  title(gene)
  
  #close pdf 
  dev.off()
  
}

makeTree_mcct <- function(gene) {
  inFile <- paste(gene,"_mcctSumt0.5.t", sep = "")
  tr <- read.nexus(inFile)
  outFile <- paste(gene,"_mcctSumt0.5.pdf", sep = "")
  
  # get tips for said tree
  tips <- tr$tip.label
  
  # search tips for your desired root-taxa
  roots <- c(grep(pattern="Alligator_mississippiensis",tips, value = TRUE),
             grep(pattern="Chelydra_serpentina",tips, value = TRUE),
             grep(pattern="Crocodylus_porosus",tips, value = TRUE),
             grep(pattern="Dromaius_novaehollandiae",tips, value = TRUE),
             grep(pattern="Gallus_gallus",tips, value = TRUE),
             grep(pattern="Mus_musculus",tips, value = TRUE),
             grep(pattern="Podocnemis_expansa",tips, value = TRUE),
             grep(pattern="Sphenodon_punctatus",tips, value = TRUE),
             grep(pattern="Tachyglossus_aculeatus",tips, value = TRUE),
             grep(pattern="Homo_sapiens",tips, value = TRUE))
  roots <- as.character(roots)
  
  # get node number for desired root
  root.node <- getMRCA(tr, roots)
  
  # root the tree
  tr.rooted <- root(tr,node=root.node)
  
  # read in your family data - this should be a tab-delimited text file:
  # taxon1  family1
  # taxon2  family2
  # etc
  # obviously, make sure your tip names and taxon names are spelled the same and stuff
  dat <- read.delim(file = "families.tsv", row.names = 1, header = F, stringsAsFactors = F,
                    col.names = c("taxon", "family"))
  
  # combine tree file and list of names, sort them
  comb <- treedata(tr.rooted,dat,sort = T,warnings = F)
  sort(comb$data)
  
  # make new lists and tree that are properly matched to each other
  # double check that all is well 
  dat2 <- comb$data
  tr2 <- comb$phy
  name.check(tr2,dat2)
  
  #make list of unique family names
  unq <- unique(dat2[,1])
  
  # make a new data list replacing family names with colors
  dat3 <- dat2
  
  # replace specific familes with specific colors
  dat3 <- gsub(pattern = "Serpentes" ,replacement = "darkorchid4", dat3)
  dat3 <- gsub(pattern = "Scolecophidia" ,replacement = "mediumslateblue", dat3)
  dat3 <- gsub(pattern = "Teioidea" ,replacement = "blue3", dat3)
  dat3 <- gsub(pattern = "Amphisbaenia" ,replacement = "firebrick3", dat3)
  dat3 <- gsub(pattern = "Lacertoidea" ,replacement = "darkgoldenrod2", dat3)
  dat3 <- gsub(pattern = "Anguimorpha" ,replacement = "darkorange3", dat3)
  dat3 <- gsub(pattern = "Dibamidae" ,replacement = "chocolate4", dat3)
  dat3 <- gsub(pattern = "Gekkota" ,replacement = "chartreuse3", dat3)
  dat3 <- gsub(pattern = "Outgroup" ,replacement = "gray50", dat3)
  dat3 <- gsub(pattern = "Scincoidea" ,replacement = "dodgerblue", dat3)
  dat3 <- gsub(pattern = "Iguania" ,replacement = "darkgreen", dat3)
  
  col <- unique(dat3[,1])
  
  # open pdf file
  pdf(outFile, height = 9, width = 7)
  
  # plot the tree with the tips labeled with taxon names
  
  plot.phylo(tr2,  show.tip.label = F, no.margin = F)
  
  # cex controls the size of the text, label.offset controls how far from the tip the name is
  
  # now add dots to the tips, colored by family name
  
  tiplabels(tr2$tip.label, adj = -0.7, cex = 0.05, frame= "rect", bg=dat3)
  #tiplabels(tr2$tip.label, cex = 0.2, pie = to.matrix(family.dat2, piecol=family.dat3)
  
  # plot legend
  # legend(x=35, text.col = col, legend = unq, cex = 1, text.width = 30, text.font = 2)
  
  # plot title
  title(gene)
  
  #close pdf 
  dev.off()
  
}


############################################################################################################################################
  
setwd("/Users/ChatNoir/Projects/Squam/RevBayes/PP_final_empTrees/empTrees")

# read in the nexus file and name the outfile
genes <- c("LRRN1")

genes <- c("ADNP", "AHR", "AKAP9", "BACH1", "BDNF", "BHLHB2", "BMP2", "CAND1")
genes <- c("CARD4", "CILP", "CXCR4", "DLL1", "ECEL", "ENC1", "FSHR", "FSTL5")
genes <- c("GALR1", "GHSR", "GPR37", "HLCS")
genes <- c("INHIBA", "LRRN1", "LZTSS1", "MKL1")
genes <- c("MLL3", "MSH6", "NGFB", "NKTR", "NTF", "PNN", "PRLR", "PTGER4", "PTPN")
genes <- c("R35", "RAG1", "SINCAIP", "SLC30A1", "SLC8A1", "SLC8A3", "TRAF6", "UBN1")
genes <- c("VCPIP1", "ZEB2", "ZFP36L1")

sapply(genes, makeTree)


############################################################################################################################################
setwd("/Users/ChatNoir/Projects/Squam/RevBayes/PP_final_empTrees/empTrees")

gene <- c("ADNP")

# read in your family data - this should be a tab-delimited text file:
# taxon1  family1
dat <- read.delim(file = "families.tsv", row.names = 1, header = F, stringsAsFactors = F,
                  col.names = c("taxon", "family"))

### FIRST TREE
inFileA <- paste(gene,"_mcct.t", sep = "")
trA <- read.nexus(inFileA)
# get tips for said tree
tipsA <- trA$tip.label
# search tips for your desired root-taxa
rootsA <- c(grep(pattern="Alligator_mississippiensis",tipsA, value = TRUE),
            grep(pattern="Chelydra_serpentina",tipsA, value = TRUE),
            grep(pattern="Crocodylus_porosus",tipsA, value = TRUE),
            grep(pattern="Dromaius_novaehollandiae",tipsA, value = TRUE),
            grep(pattern="Gallus_gallus",tipsA, value = TRUE),
            grep(pattern="Mus_musculus",tipsA, value = TRUE),
            grep(pattern="Podocnemis_expansa",tipsA, value = TRUE),
            grep(pattern="Sphenodon_punctatus",tipsA, value = TRUE),
            grep(pattern="Tachyglossus_aculeatus",tipsA, value = TRUE),
            grep(pattern="Homo_sapiens",tipsA, value = TRUE))
rootsA <- as.character(rootsA)
# get node number for desired root
root.node <- getMRCA(trA, rootsA)
# root the tree
trA.rooted <- root(trA,node=root.node)
# combine tree file and list of names, sort them
combA <- treedata(trA.rooted,dat,sort = T,warnings = F)
sort(combA$data)
# make new lists and tree that are properly matched to each other
# double check that all is well 
dat2A <- combA$data
tr2A <- combA$phy
name.check(tr2A,dat2A)
#make list of unique family names
unqA <- unique(dat2A[,1])
# make a new data list replacing family names with colors
dat3A <- dat2A
# replace specific familes with specific colors
dat3A <- gsub(pattern = "Serpentes" ,replacement = "darkorchid4", dat3A)
dat3A <- gsub(pattern = "Scolecophidia" ,replacement = "mediumslateblue", dat3A)
dat3A <- gsub(pattern = "Teioidea" ,replacement = "blue3", dat3A)
dat3A <- gsub(pattern = "Amphisbaenia" ,replacement = "firebrick3", dat3A)
dat3A <- gsub(pattern = "Lacertoidea" ,replacement = "darkgoldenrod2", dat3A)
dat3A <- gsub(pattern = "Anguimorpha" ,replacement = "darkorange3", dat3A)
dat3A <- gsub(pattern = "Dibamidae" ,replacement = "chocolate4", dat3A)
dat3A <- gsub(pattern = "Gekkota" ,replacement = "chartreuse3", dat3A)
dat3A <- gsub(pattern = "Outgroup" ,replacement = "gray50", dat3A)
dat3A <- gsub(pattern = "Scincoidea" ,replacement = "dodgerblue", dat3A)
dat3A <- gsub(pattern = "Iguania" ,replacement = "darkgreen", dat3A)
colA <- unique(dat3A[,1])



# open pdf file
#pdf(outFile, height = 9, width = 7)
layout(matrix(1:1))
# plot the tree with the tips labeled with taxon names
plot.phylo(tr2A,  show.tip.label = F, no.margin = F)
tiplabels(tr2A$tip.label, adj = -0.7, cex = 0.05, frame= "rect", bg=dat3A)

# plot legend
#legend(x=35, text.col = col, legend = unqA, cex = 1, text.width = 30, text.font = 2)

# plot title
title(gene)

#close pdf 
#dev.off()
  
############################################################################################################################################

  
  

