x <- seq(-2*pi,2*pi,0.01)

plot(x, sin(x),
  main = "Plot of Trignometric Functions",
  type = "l",
  xlim = range(-6.28, 6.28),
  ylim = range(-4, 4),
  col = "blue"
)

lines(x, cos(x), col="red")
lines(x, tan(x), col="yellow")
lines(x, cos(x)/sin(x), col="magenta")
lines(x, 1/cos(x), col="green")
lines(x, 1/sin(x), col="cyan")

legend("topright",
  c("sin(x)", "cos(x)", "tan(x)", "cot(x)", "sec(x)", "csc(x)"),
  fill = c("blue", "red", "yellow", "magenta", "green", "cyan")
)

grid(
  nx=NULL,
  ny=NULL,
  col="lightgray",
  lty = "dotted"
)
