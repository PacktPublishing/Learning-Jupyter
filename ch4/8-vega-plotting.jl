#Julia Vega Plotting

#Pkg.add("Vega")
#Pkg.add("Compat")
#Pkg.add("Patchwork")
using Vega
using Compat
using Patchwork
Patchwork.load_js_runtime()
stock = ["chairs", "tables", "desks", "rugs", "lamps"];
quantity = [15, 10, 10, 5, 20];
piechart(x = stock, y = quantity)