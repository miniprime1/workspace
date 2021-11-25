figure('NumberTitle','off')
t = 0:pi/256:2*pi;
x = 16*sin(t).^3;
y = 13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t);
patch(x,y,[1,0,0])
axis equal
axis off
set(gcf, 'Position', get(0,'Screensize')); 
title('혜준이는 시우를 좋아해요!', 'FontSize', 28);