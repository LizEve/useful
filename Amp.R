library(ggplot2)
library(RColorBrewer)

setwd("/Users/ChatNoir/Projects/Squam/RevBayes/Amp_Results/AmpOut")

data<- read.delim("Aug26_effect_sizes.tsv", header=T)

genes=data$gene
one1000=data$X1.th.1000.quantile.Effect.Size
one100=data$X1.th.100.quantile.Effect.Size
one20=data$X1.th.20.quantile.Effect.Size
one10=data$X1.th.10.quantile.Effect.Size
one8=data$X1.th.8.quantile.Effect.Size
one6=data$X1.th.6.quantile.Effect.Size
one4=data$X1.th.4.quantile.Effect.Size
two4=data$X2.th.4.quantile.Effect.Size
three4=data$X3.th.4.quantile.Effect.Size
nine9100=data$X99.th.100.quantile.Effect.Siz
nine991000=data$X999.th.1000.quantile.Effect.Size
nine99910000=data$X9999.th.10000.quantile.Effect.Size
interQuart=data$Interquartile.Range.Effect.Size
meanTree=data$Mean.Treelength.Effect.Size
varTree=data$Treelength.Variance.Effect.Size

#don't include gene or entropy based column
numStats=length(names(data))-2
numGenes=length(genes)
df <- data.frame(x=rep(genes,numStats), 
                 y=c(one1000,one100,one20,one10,one8,one6,one4,two4,three4,nine9100,nine991000,nine99910000,interQuart,meanTree,varTree), 
                 Statistic=c(rep("1st 1000th quantile",numGenes),rep("1st 100th quantile",numGenes),rep("1st 20th quantile",numGenes),rep("1st 10th quantile",numGenes),rep("1st 8th quantile",numGenes),rep("1st 6th quantile",numGenes),rep("1st 4th quantile",numGenes),rep("2nd 4th quantile",numGenes),rep("3rd 4th quantile",numGenes),rep("99th 100th quantile",numGenes),rep("999th 1000th quantile",numGenes),rep("9999th 10000th quantile",numGenes),rep("Interquartile Range",numGenes),rep("Mean Treelength",numGenes),rep("Treelength Variance",numGenes)))

#colorRampPalette(brewer.pal(n_palette, "palette_name"))(n_plot),
ESgraph = ggplot(df, aes(x=x, y=y, color=Statistic)) + 
  geom_point() + 
  xlab("Gene") +
  ylab("Effect Size") +
  theme(axis.title.x = element_text(color="Black", size=16, vjust=-0.35, family='Helvetica'), 
        axis.title.y = element_text(color="Black", size=16, vjust=0.35, family='Helvetica'))

ESgraph

ggsave(filename="Rplot.tiff", plot=ESgraph, scale=1)


FAILURES:
colorCount=numStats
a <- colorRampPalette(brewer.pal(9,"Blues"))(15)
b <- c("#F7FBFF", "#E8F1FA", "#DAE8F5", "#CCDFF1", "#BAD6EB", "#A3CCE3", "#88BEDC", "#6BAED6", "#539ECC", "#3D8DC3", "#2A7AB9", "#1967AD", "#0B559F", "#084287", "#08306B")
scale_fill_manual(values = b)