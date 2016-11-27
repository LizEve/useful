library(rworldmap)
#tissues
tissue<-read.csv("/Users/ChatNoir/Google Drive/LSU/P_reg/LatLongDateTypeTissues.csv")
#observations
specimens <- read.csv("/Users/ChatNoir/Google Drive/LSU/P_reg/LatLongDateType.csv")
recuero <- read.csv("/Users/ChatNoir/Google Drive/LSU/P_reg/RecueroLatLong.csv")
ripplinger <- read.csv("/Users/ChatNoir/Google Drive/LSU/P_reg/RipplingerLatLong.csv")
tissuemap<-getMap(resolution = "low") 
plot(tissuemap, xlim = c(-136, -110), ylim = c(23,57), pch = 20) #larger map
plot(tissuemap, xlim = c(-138, -110), ylim = c(24,51), pch = 20) #focused map
points(specimens$decimallongitude, specimens$decimallatitude, col="darkolivegreen4", cex=1, pch = 20) #tissue locality points
points(tissue$decimallongitude, tissue$decimallatitude, col="darkorange", cex=1.2, pch = 20)
points(recuero$decimallongitude, recuero$decimallatitude, col="blue1", cex=1, pch = 20)
points(ripplinger$decimallongitude, ripplinger$decimallatitude, col="deeppink4", cex=1, pch = 20)
box(which = "plot", lty = "solid") # putting border around the plot



