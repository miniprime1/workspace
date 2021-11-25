x = [-5.0:0.01:5.0];
y = gamma(x);
plot(x, y, 'r')
axis([-5 5 -5 5])
legend("gamma(x)")
title('Plot of Gamma Function')
grid on