data <- read.delim('chiari_effect_sizes.tsv', header=T)

for (i in names(data)) {
 

### sets the colors for each point of interest
cols <- rep('black', nrow(data))
cols[c(125)] <- 'red'
cols[c(17)] <- 'green'
cols[c(151)] <- 'blue'
cols[c(157)] <- 'mediumorchid'

## sets the shape for each point of interest
shapes <- rep(20, nrow(data))
shapes[c(125)] <- 15
shapes[c(17)] <- 17
shapes[c(151)] <- 18
shapes[c(157)] <- 19

## sets the size for each point of interest
sizes <- rep(1, nrow(data))
sizes[c(125)] <- 2
sizes[c(17)] <- 2
sizes[c(151)] <- 2
sizes[c(157)] <- 2


pdf(file=paste(i,".pdf"))
plot(data[,i], ylab="Effect Size", xlab="Gene Index", main = i, col=cols, pch=shapes, cex=sizes)


### build legend

names <- c("my_ENSGALG00000001452.macse_DNA_gb","my_ENSGALG00000008916.macse_DNA_gb","my_ENSGALG00000011434.macse_DNA_gb","my_ENSGALG00000011905.macse_DNA_gb")

legend( x="topright", legend=c(names), col=c("red", "green", "blue", "mediumorchid"), pch=c(15,17,18,19), cex=0.80)
dev.off()

}