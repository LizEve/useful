#Import ggplot
library(ggplot2)

#User input:

#working dir
wd="/Users/ChatNoir/bin/Squam/R"

#file name or path of input csv file
#csvfile="RF_TL_r_test.csv"

masterD=("~/bin/Squam/data_files/mstxrm/masterD.05.11.15.txt")

#output file name or path
out="out_graph.png"

#set working directory to wherever you want your graphs to end up
setwd(wd)

#read in file, assuming csv format
data=read.table(masterD, header=TRUE)

#Data- fill in with names of columns in data file
xvals=data$Tree.Length
yvals=data$Weighted.Robinson.Foulds.Distance

#set outfile
#png(filename=out)


#Plot Template:

#add plot and trend line
p = ggplot(data, aes(xvals, yvals)) + geom_point(color="darkorchid4") + geom_smooth(method=lm, formula = y ~ x, color="cyan4", se=TRUE) 
#add title and labels # make background white
p = p + labs(x=xaxis,y=yaxis,title=title) + theme_bw()
#edit titles vjust=how far away from axis
p = p + theme(plot.title = element_text(size=30, lineheight=0.8, face="bold", vjust=1, family='Courier', color="firebrick"))
#edit labels
p = p + theme(axis.title.x = element_text(color="firebrick", vjust=-0.35,family='Courier'), axis.title.y = element_text(color="firebrick" , vjust=0.35, family='Courier'))

#Trendline:

#set trendline equation
m = lm(yvals ~ xvals) #y ~ x

#function for writing trendline
lm_eqn = function(m){
	eq <- substitute(italic(y) == a + b %.% italic(x)*","~~italic(r)^2~"="~r2, 
	         list(a = format(coef(m)[1], digits = 2), 
	              b = format(coef(m)[2], digits = 2), 
	             r2 = format(summary(m)$r.squared, digits = 3)))
	as.character(as.expression(eq));}

#call eqn_lm 
eqn=lm_eqn(m)

#add to graph. Edit where the eqn goes on graph
p=p+geom_text(aes(x = 5, y = 3, label = eqn), color="black", size=5, parse = TRUE)

#close file
#http://docs.ggplot2.org/current/ggsave.html
ggsave(filename=out, plot=p)



      



#Notes

#Equation:
#a = signif(coef(m)[1], digits = 2)
#b = signif(coef(m)[2], digits = 2)
#eqn = paste("y = ",b,"x + ",a, sep="") just equation not formatted

#summary(m) - gives details on trendline eqn
#	r2=signif(summary(m)$adj.r.squared, 5)
#rsqrd adj accounts for number of variables and observations to adjust for overfitting 
#http://stackoverflow.com/questions/2870631/what-is-the-difference-between-multiple-r-squared-and-adjusted-r-squared-in-a-si

