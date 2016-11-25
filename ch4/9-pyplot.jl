#Julia PyPlot Plotting

#Pkg.add("PyPlot")
using PyPlot
precipitation = [0,0,0,0,0,0,0,0,0,0,0.12,0.01,0,0,0,0.37,0,0,0,0,0.01,0,0,0,0.01,0.01,0,0.17,0.01,0.11,0.31]
date = collect(1:31)
fig = figure(1, figsize=(4, 4))
plot(date, precipitation, ".")
title("Boston Precipitation")
xlabel("May 2013")
ylabel("Precipitation")