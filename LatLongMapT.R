library(rworldmap)
#tissues
tissue<-read.csv("/Users/ChatNoir/Google Drive/LSU/Thar_Be_Turtles/LatLongTissue.csv")
#observations
specimen <- read.csv("/Users/ChatNoir/Google Drive/LSU/Thar_Be_Turtles/LatLongAll.csv")
fossil <- read.csv("/Users/ChatNoir/Google Drive/LSU/Thar_Be_Turtles/LatLongFossil.csv")

tissuemap<-getMap(resolution = "low") 
plot(tissuemap, xlim = c(-100, -60), ylim = c(35,40), pch = 20) #x=long y=lat
points(specimen$decimallongitude, specimen$decimallatitude, 
       col="darkolivegreen4", cex=1.2, pch = 20) #tissue locality points
points(tissue$decimallongitude, tissue$decimallatitude, 
       col="darkorange", cex=1, pch = 20)
points(fossil$decimallongitude, fossil$decimallatitude, 
       col="lightblue", cex=0.7, pch = 20)

legend(-75,30, legend = c("Specimens","Tissues","Fossils"), 
       col=c("darkolivegreen4","darkorange","lightblue"),
       cex = 1, text.width = 10, text.font = 1,
       lty=1, lwd=3, box.lty=0, y.intersp = 1.5)

box(which = "plot", lty = "solid") # putting border around the plot



