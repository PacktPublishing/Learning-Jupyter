#Julia Winston Plotting

using Winston
# fix the random seed so we have reproducible results
srand(111)
# generate a plot
pl = plot(cumsum(rand(100) .- 0.5), "g", cumsum(rand(100) .- 0.5), "b")
# display the plot
display(pl)