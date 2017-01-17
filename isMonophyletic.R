library(ape)
library(phytools)
library(geiger)

#set working directory, gene name, and file suffix
setwd("/Users/ChatNoir/Projects/Squam/RevBayes/PP_final_empTrees/AHR_test/AHR_mike/AHR_negControl_empTree")
gene='AHR_negControl'
inFile <- paste(gene,"_mstxrm.trees", sep = "")

#read in trees
trees <- read.nexus(inFile)

#function to ask if monophyletic and print result
isMono <- function(tr,clade) {
  mon = is.monophyletic (phy = tr, tips = clade)
  mon
}

#edit to include taxa of intrest
monoClade = c("Alopoglossus_angulatum", "Pholidobolus_macbrydei", "Colobosaura_modesta", "Aspidoscelis_tigris", "Teius_teyou", "Callopistes_maculatus", "Tupinambis_teguixin")

#apply monophyly test to all trees in posterior
#True = monophyletic, False = nonmonophyletic
#If monophyletic, should be a list of TRUEs
tfmono <- c(sapply(trees, isMono, clade = monoClade))

#check if there are any trees that do not contain given clade as monophyletic
#False = Monophyletic
#True = NOT monophyletic (list includes F therefore nonmon trees)
'FALSE' %in% tfmono


#plot specific trees in treeset if needed. 
tree <- trees[[5468]]
plot.phylo(tree, show.tip.label = F, no.margin = F)
tiplabels(tree$tip.label, adj = -0.7, cex = 0.5, frame = "none")


#clades I used to test the function including a negative control
nope = c("Tupinambis_teguixin",  "Callopistes_maculatus", "Teius_teyou")
clade = c("Rhineura_floridana", "Diplometopon_zarudnyi", "Bipes_canaliculatus", "Bipes_biporus", "Amphisbaena_fuliginosa")
clade = c("Phrynosoma_platyrhinos", "Uma_scoparia", "Petrosaurus_mearnsi", "Sceloporus_variabilis", "Uta_stansburiana")

tfmono <- c(sapply(trees, isMono, clade = nope))

#check if there are any trees that do not contain given clade as monophyletic
#False = Monophyletic
#True = NOT monophyletic (list includes F therefore nonmon trees)
'FALSE' %in% tfmono