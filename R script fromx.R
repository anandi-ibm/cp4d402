print(paste0('ENV1 : ', Sys.getenv('ENV1')))
print(paste0('ENV2 : ', Sys.getenv('ENV2')))
 


#Arguments
#!/usr/bin/env Rscript
args <- commandArgs(trailingOnly = TRUE)
rnorm(n=as.numeric(args[1]), mean=as.numeric(args[2]))
