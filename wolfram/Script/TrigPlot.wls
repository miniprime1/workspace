Plt = Plot[{Sin[x], Cos[x], Tan[x], Cot[x], Sec[x], Csc[x]}, {x, -2*Pi, 2*Pi}, PlotRange -> {-4, 4}, PlotLegends -> "Expressions"]
Export["trig_plot.png", Plt] (*Save as png*)