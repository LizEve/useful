path = "/Users/lcoghill/Desktop/testStats/"
file.names <- dir(path, pattern = ".csv")

for (i in 1:length(file.names)) {

  file <- read.table(file.names[i])
  plottitle <- gsub(" Test Statistic.csv", "", file.names[i])
  outname <- gsub(" ", "", plottitle)
  outname <- paste(outname, ".pdf")
  pdf(outname)
  plot(density(file$V1, from=0, to=1.0, n=248), main=plottitle, xlab="PValue")
  dev.off()
  }