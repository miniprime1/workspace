Plt = Plot[{Sqrt[Abs[x]] + Sqrt[6-Power[x,2]], Sqrt[Abs[x]] - Sqrt[6-Power[x,2]]}, {x, -Sqrt[6], Sqrt[6]}, PlotStyle -> Red]
Export["heart.png", Show[Plt, PlotRange -> All]] (*Save as png*)