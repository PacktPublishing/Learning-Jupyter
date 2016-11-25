# make sure lattice package is installed
# in a standalone R script you would have a command to download the lattice library – this is not needed in Jupyter
library("lattice")
# use the automobile data from ics.edu
mydata <- read.table("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
# define more meaningful column names for the display
colnames(mydata) <- c("mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model.year", "origin", "car.name")
# 3-D plot with number of cylinders on x axis, weight of the vehicle on the y axis and miles per gallon on the z axis.
cloud(mpg~cylinders*weight, data=mydata)
