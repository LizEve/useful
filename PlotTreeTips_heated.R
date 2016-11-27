# plot a tree with the tips colored by family
library(ape)
library(phytools)
library(geiger)

# function for making tree, pretty tree
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

setwd("/Users/ChatNoir/Projects/Squam/RevBayes/heated_emp/empTrees")

# read in the nexus file and name the outfile
genes <- c("ADNP", "AHR")

genes <- c("CAND1_0.05heated_run1", "CAND1_final_run2.trees", "GHSR_0.05heated8chains_run2", "CAND1_final_run1.trees", "GHSR_0.05heated8chains_run1", "GHSR_0.05heated_run1")

sapply(genes, makeTree_con)

sapply(genes, makeTree_mcct)




#Extra edited out bits
#next time try plottree http://blog.phytools.org/2015/04/plottreewbars-with-tip-labels.html
#make pretty color list. 
#rainbow method
#palette(rainbow(length(unique(dat2))))
#col <- palette()
#custom color palette
#col <- c("darkorchid4","mediumslateblue","blue3","firebrick3","darkgoldenrod2","darkorange3","chocolate4","chartreuse3","gray50","dodgerblue","darkgreen")
#this is a generalized way to add colors for each species. but it colors the species on a first come first serve basis
#for (i in 1:length(col)) {
#  dat3 <- gsub(pattern = unq[i],replacement = col[i], dat3)
#}


