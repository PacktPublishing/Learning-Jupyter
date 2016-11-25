#Julia Gadfly Histogram

using Gadfly
plot(x=randn(113), Geom.histogram(bincount=10))