x <- seq(-4, 4, 0.01)
plot(x, exp(x), main="Plot of Exponential Function", type="l", col="blue", xlim=range(-4, 4), ylim=range(0, 5))
legend("topright", c("exp(x)"), fill=c("blue"))
grid(nx=NULL, ny=NULL, col="lightgray", lty="dotted")
