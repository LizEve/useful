#Object:
#take tree len file and combine with tree dist information
#edit tree dist file to incude column for RF*2, weighted RF, and weighted MS dist 
masterD=0

#working dir
wd = "~/bin/Squam/data_files/mstxrm/"

#file name or path of input tree len csv file
TL.file = "tree_dists_mstxrm/datafiles/TL_prunedog_misstxremoved"
#1-Gene 2-Tree.Length

#file name or path of input treen dist tsv file
TD.file = "tree_dists_mstxrm/datafiles/treedists_misstxremoved_prunedog_genetrees.csv"
#1-No 2-RefTree 3-Tree 4-RefTree_taxa 5-Tree_taxa 6-Common_taxa 7-MatchingSplit 8-R.F

#file of clocklike scores
CL.file = "clocklikepaup_mstxrm/prunedog_misstxremoved/all_clocklike_misstxremoved_prunedog.txt"

#monophly of toxicofera
MT.file="mono_tox.txt"

#set working directory 
setwd (wd)

#read in data files, skip date/time line in TL file
tree.len=read.csv(TL.file, skip=1)
tree.dist=read.csv(TD.file)
clock.like=read.table(CL.file, header = TRUE)
mon.tox=read.table(MT.file, header = TRUE)


#Edit files

#remove columns. new headers are:
#1-Tree 2-RefTree_taxa 3-Tree_taxa 4-MatchingSplit 5-R.F
tree.dist.edit=tree.dist[,c(3,4,5,7,8)]
clock.like.edit=clock.like[,c(1,3,4,5)]
tree.len.edit=tree.len[,c(2)]

#initiate dataframe
masterD=data.frame(tree.len,tree.dist.edit,clock.like.edit,mon.tox)

#create columns to add
RFxtwo = 2*tree.dist.edit[5]
RFw = RFxtwo/((tree.dist.edit[3]-3)*2)
MSw= tree.dist.edit[4]/tree.dist.edit[3]
nummisstx = tree.dist.edit[2]-tree.dist.edit[3]
pmisstx = nummisstx/tree.dist.edit[2]
avgBL = tree.len$Tree.Length/((2*tree.dist.edit[3])-3)

#add new columns
masterD["RF*2"] <- RFxtwo
masterD["RFw"] <- RFw
masterD["MSw"] <- MSw
masterD["nummisstx"] <- nummisstx
masterD["pmisstx"] <- pmisstx
masterD["avgBL"] <- avgBL

#save to file
write.table(masterD, file="prunedog_masterD.05.20.15.txt")

