library(ape)


setwd="/Users/ChatNoir/bin/Squam/R"

#In files
dna = read.tree(file="~/bin/Squam/R/molec.tree")
bones = read.tree(file="~/bin/Squam/R/morpho.tree")
tree = read.tree(file="~/bin/Squam/R/tree.tree")
#Out files
Dout="molec_tree.pdf"
Bout="morpho_tree.pdf"
cout="tree.pdf"

dna.tree=plot(dna, type = "phylogram", edge.width = 5, edge.color="cadetblue3", tip.color="cadetblue2", label.offset=0.2, font = 1, cex=1.75)

dna.tree=plot(tree, type = "cladogram", edge.width = 15, edge.color="white", tip.color="cadetblue2", label.offset=0.2, font = 1, cex=1.75, show.tip.label=F, direction="upwards")


b=collapse.singles(bones)
bones.tree=plot(b, type = "phylogram", edge.width = 5, edge.color="cadetblue3", tip.color="cadetblue2", label.offset=0.2, font = 1, cex=1.75)







dev.print(pdf,file=outfilepdf)
dev.off()



write.tree(bones.tree, file=Bout)