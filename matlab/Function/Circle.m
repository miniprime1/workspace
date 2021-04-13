function y=Circle(r)
    % Returns the plot of circle from specified radius.
    hold on
    th = 0:pi/50:2*pi;
    xunit = r * cos(th) + r;
    yunit = r * sin(th) + r;
    y = plot(xunit, yunit);
hold off