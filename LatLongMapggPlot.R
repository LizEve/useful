library(ggplot2)
library(maps)
tissue<-read.csv("/Users/ChatNoir/Google Drive/LSU/P_reg/LatLongDateTypeTissues.csv")
#observations
specimens <- read.csv("/Users/ChatNoir/Google Drive/LSU/P_reg/LatLongDateType.csv")
recuero <- read.csv("/Users/ChatNoir/Google Drive/LSU/P_reg/RecueroLatLong.csv")
ripplinger <- read.csv("/Users/ChatNoir/Google Drive/LSU/P_reg/RipplingerLatLong.csv")

http://www.unomaha.edu/mahbubulmajumder/data-science/fall-2014/lectures/06-display-spatial-data/06-display-spatial-data.html#/11
us.dat <- map_data("state")
ct.dat <- map_data("county")
ggplot() + geom_polygon(aes(long,lat, group=group), fill="grey65", data=ct.dat) + 
  geom_polygon(aes(long,lat, group=group), color='white', fill=NA, data=us.dat) + 
  theme_bw() + 
  theme(axis.text = element_blank(), axis.title=element_blank()) 
