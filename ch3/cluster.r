# load the wheat data set from uci.edu
wheat <- read.csv("http://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt", sep="\t")
# define useful column names
colnames(wheat) <-c("area", "perimeter", "compactness", "length", "width", "asymmetry", "groove", "undefined")
# exclude incomplete cases from the data
wheat <- wheat[complete.cases(wheat),]
# calculate the clusters
fit <- kmeans(wheat, 5)
fit
