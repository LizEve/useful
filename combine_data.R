#Object:
#take tree len file and combine with tree dist information
#edit tree dist file to incude column for RF*2, weighted RF, and weighted MS dist 

#working dir
wd="/Users/ChatNoir/bin/Squam/data_files/mstxrm/tree_dists_mstxrm/datafiles/"


#file name or path of input tree len csv file
TL.file="TL_misstxremoved.csv"
#1-Gene 2-Tree.Length

#file name or path of input treen dist tsv file
TD.file="treedists_misstxremoved_genetrees.csv"
#1-No 2-RefTree 3-Tree 4-RefTree_taxa 5-Tree_taxa 6-Common_taxa 7-MatchingSplit 8-R.F

#set working directory 
setwd(wd)

#read in data files, skip date/time line in TL file
tree.len=read.csv(TLfile, skip=1)
tree.dist=read.csv(TDfile)

#Edit treedist
#remove columns. new headers are:
#1-Tree 2-RefTree_taxa 3-Tree_taxa 4-MatchingSplit 5-R.F
tree.dist.edit=tree.dist[,c(3,4,5,7,8)]

#create columns to add
RFxtwo = 2*tree.dist.edit[5]
RFw = RFxtwo/tree.dist.edit[3]
MSw= tree.dist.edit[4]/tree.dist.edit[3]
nummisstx = tree.dist.edit[2]-tree.dist.edit[3]

#initiate dataframe
masterD=data.frame(tree.len,tree.dist.edit)

#add new columns
masterD["RF*2"] <- RFxtwo
masterD["RFw"] <- RFw
masterD["MSw"] <- MSw
masterD["nummisstx"] <- nummisstx






#testing

test=data.frame(treelen,treedist)
test
