### spearman rank correlation and permutation test
for (i in names(ESs[,-1])){ 
  
  for (n in names(BFs[,-1])){
    res <- spearman_test(ESs[,i] ~ BFs[,n])
    print(paste(i, " ~ ", n, " P-value: ", pvalue(res)))
    out <- (paste(i, " ~ ", n, "\nP-value: ", pvalue(res), "\nRho: ", statistic(res), "\n"))
    #print(pvalue(res))
    if (is.nan(pvalue(res)) != TRUE & pvalue(res) <= 0.05 & statistic(res) < 0 ) {
        write(out, file="effectsize_bayesfactor_correlations.txt", append=TRUE)
    }
  }

}
