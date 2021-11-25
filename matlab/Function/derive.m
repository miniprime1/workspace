function y = derive(f, a)
    h = 1.0 * 10^-6;
    x1 = a-h;
    x2 = a+h;
    y1 = f(x1);
    y2 = f(x2);
    y = (y2-y1)/(x2-x1);
end