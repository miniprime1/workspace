x=[-5:0.1:5];
y1 = sin(x);
y2 = cos(x);
plot(x, y1, 'b', x, y2, 'r')
xlabel('x')
ylabel('y')
title('Practice Graph (Sine/Cosine)')
axis([-4 4 -2 2])
legend("Graph 1", "Graph 2")
grid on