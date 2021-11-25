t=[-2*pi:0.0001:2*pi];
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
subtitle('t = [-2*pi, 2*pi]')