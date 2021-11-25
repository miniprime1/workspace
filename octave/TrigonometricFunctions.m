t=linspace(-2*pi, 2*pi, 10000);
ysin = sin(t);
ycos = cos(t);
ytan = tan(t);
ycot = cot(t);
ysec = sec(t);
ycsc = csc(t);
plot(t, ysin, t, ycos, t, ytan, t, ycot, t, ysec, t, ycsc)
axis([-2*pi 2*pi -4 4])
legend('sin(t)', 'cos(t)', 'tan(t)', 'cot(t)', 'sec(t)', 'csc(t)')
title('Plot of Trigonometric Fuctions')