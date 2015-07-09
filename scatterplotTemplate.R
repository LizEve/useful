#Import ggplot
library(ggplot2)


#Trendline:
#set trendline equation

#function for writing trendline
lm_eqn = function(xvals,yvals){
	m = lm(yvals ~ xvals) #y ~ x
	eq <- substitute(italic(y) == a + b %.% italic(x)*","~~italic(r)^2~"="~r2, 
	         list(a = format(coef(m)[1], digits = 2), 
	              b = format(coef(m)[2], digits = 2), 
	             r2 = format(summary(m)$r.squared, digits = 3)))
	as.character(as.expression(eq));}



#Plot Template:

my.plot <- function(data, xvals, yvals, title, xaxis, yaxis){
	
	#add plot and trend line
	p = ggplot(data, aes(xvals, yvals)) + geom_point(color="darkorchid4") + 	geom_smooth(method=lm, formula = y ~ x, color="cyan4", se=TRUE) 
	#add title and labels # make background white
	p = p + labs(x=xaxis,y=yaxis,title=title) + theme_bw()
	#edit titles vjust=how far away from axis
	p = p + theme(plot.title = element_text(size=20, lineheight=0.8, face="bold", vjust=1, family='Courier', color="firebrick"))
	#edit labels
	p = p + theme(axis.title.x = element_text(color="firebrick", size=14, vjust=-0.35,family='Courier'), axis.title.y = element_text(color="firebrick" , size=14, vjust=0.35, family='Courier'))
	#add trendline to graph. Edit where the eqn goes on graph
	p=p+geom_text(aes(x = 14, y = 1.2, label = eqn), color="black", size=4.5, parse = TRUE)
	#set tick marks #which.min(xvals)
	#p=p+scale_y_continuous(breaks=0:1.25)+scale_x_continuous(breaks=0:20)
}


#User input:

#set working directory to wherever you want your graphs to end up
wd="/Users/ChatNoir/bin/Squam/data_files/mstxrm"
setwd(wd)

#file name or path of input file
masterD=read.table("~/bin/Squam/data_files/mstxrm/masterD.05.12.15.txt", header=T)
data=data.frame(masterD)
#colnames(data)

#Data- fill in with names of columns in data file
xvals=data$Tree.Length
yvals=data$RFw
xaxis="Tree Length"
yaxis="Weighted Robinson-Foulds value"
title="Tree length vs RF distance to reference tree"

#output file name or path
out="RFwTL_graph.png"
png(filename=out)

#call eqn_lm 
eqn=lm_eqn(xvals,yvals)

graph=my.plot(data, xvals, yvals, title, xaxis, yaxis)
graph
#close file
#http://docs.ggplot2.org/current/ggsave.html
ggsave(filename=out, plot=graph, scale=1.2)



