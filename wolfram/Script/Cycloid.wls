Plt = ParametricPlot[{t - Sin[t], 1 - Cos[t]}, {t, 0, 2Pi}]
Export["cycloid.png", Show[Plt, PlotRange -> All]] (*Save as png*)