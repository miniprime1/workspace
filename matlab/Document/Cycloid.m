% Calculate & Plot Cycloid
a = 1;
t = linspace(0, 2*pi, 1000);
x = a * (t - sin(t));
y = a * (1 - cos(t));
cycloid = plot(x, y, "b--", "LineWidth", 1);
hold on
grid on

% Calculate & Plot Circle
xc = linspace(-1, 1, 1000);
ycp = 1 + sqrt(a^2 - xc.^2);
ycm = 1 - sqrt(a^2 - xc.^2);
cip = plot(xc, ycp, "k", "LineWidth", 1);
cim = plot(xc, ycm, "k", "LineWidth", 1);
cim.Annotation.LegendInformation.IconDisplayStyle = 'off';

% Draw Point
plot(0, 0, "b.", "MarkerSize", 20);

% Draw X and Y axis
xax = plot([0, 0], [-100, 100], "k", "LineWidth", 0.5);
yax = plot([-100, 100], [0, 0], "k", "LineWidth", 0.5);
xax.Annotation.LegendInformation.IconDisplayStyle = 'off';
yax.Annotation.LegendInformation.IconDisplayStyle = 'off';

% Prettier Plot
axis([-1-1 2*pi+1 0-1 2*a+1])
pbaspect([2*pi+1+2 2*a+2 2*pi]);
legend('Cycloid', 'Circle', 'Point')