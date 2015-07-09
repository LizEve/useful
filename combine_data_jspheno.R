#Object:
#take tree len file and combine with tree dist information
#edit tree dist file to incude column for RF*2, weighted RF, and weighted MS dist 
masterD=0
#working dir
wd = "~/bin/Squam/data_files/mstxrm/"

#file name or path of input tree len csv file
TL.file = "tree_dists_mstxrm/datafiles/TL_jspheno_misstxremoved"
#1-Gene 2-Tree.Length

#file name or path of input treen dist tsv file
TD.file = "tree_dists_mstxrm/datafiles/treedists_misstxremoved_jspheno_genetrees.csv"
#1-No 2-RefTree 3-Tree 4-RefTree_taxa 5-Tree_taxa 6-Common_taxa 7-MatchingSplit 8-R.F

#file of clocklike scores
CL.file = "clocklikepaup_mstxrm/jspheno_misstxremoved/all_clocklike_misstxremoved_jspheno.txt"

#spheno branch length and toxi monophyly file
BL.file="tree_dists_mstxrm/datafiles/spheno_branch.txt"
MT.file="mono_tox_js.txt"


#set working directory 
setwd (wd)

#read in data files, skip date/time line in TL file
tree.len=read.csv(TL.file)
tree.dist=read.csv(TD.file)
clock.like=read.table(CL.file, header = TRUE)
bl.spheno=read.table(BL.file, header = TRUE)
mon.tox=read.table(MT.file, header = TRUE)


#Edit files

#remove columns. new headers are:
#1-Tree 2-RefTree_taxa 3-Tree_taxa 4-MatchingSplit 5-R.F
tree.dist.edit=tree.dist[,c(3,4,5,7,8)]
clock.like.edit=clock.like[,c(1,3,4,5)]

#initiate dataframe
masterD=data.frame(tree.len,tree.dist.edit,clock.like.edit,bl.spheno,mon.tox)

#create columns to add
RFxtwo = 2*tree.dist.edit[5]
RFw = RFxtwo/((tree.dist.edit[3]-3)*2)
MSw= tree.dist.edit[4]/tree.dist.edit[3]
nummisstx = tree.dist.edit[2]-tree.dist.edit[3]
pmisstx = nummisstx/tree.dist.edit[2]

#add new columns
masterD["RF*2"] <- RFxtwo
masterD["RFw"] <- RFw
masterD["MSw"] <- MSw
masterD["nummisstx"] <- nummisstx
masterD["pmisstx"] <- pmisstx

#save to file
write.table(masterD, file="jspheno_masterD.05.20.15.txt")

