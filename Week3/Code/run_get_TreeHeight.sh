#!usr/bin/env Rscript

# function to find tree height
TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  print(paste("Tree height is:", height))
  
  return (height)
}

args <- commandArgs(trailingOnly = TRUE)

# load in the file
path <- paste0(args[1])
file <- read.csv(path)

# preallocate
storage <- vector("double", length = nrow(file))

# loop TreeHeight
for (i in 1:nrow(file)){
  storage[i] <- TreeHeight(file[i, 3], file[i, 2])
}

# bind vector to dataframe
file$Height <- storage

# output
write.csv(file, file = paste0("Results/", tools::file_path_sans_ext(basename(path)), "_treeheights.csv"))


          
          
          
          