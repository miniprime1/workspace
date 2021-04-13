x=[0:0.0001:1];
sqrt=x.^(1/2);
cbrt=x.^(1/3);
qdrt=x.^(1/4);
plot(x, sqrt, x, cbrt, x, qdrt);
axis([0 1 0 1]);
legend("Square Root", "Cube Root", "Fourth Root");
title("Plot of Nth Root");
subtitle("x = [0, 1]");
