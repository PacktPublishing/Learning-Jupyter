#Julia Parallel Processing

addprocs(1)
srand(111)
r = remotecall(rand, 2, 3, 4)
s = @spawnat 2 1 .+ fetch(r)
fetch(s)