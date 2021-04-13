t=[0:0.1:2*pi];
y1=sin(t);
y2=cos(t);
subplot(2,1,1);
plot(t,y1); grid on;
title('sin(t)');
subplot(2,1,2);
plot(t,y2); grid on;
title('cos(t)');