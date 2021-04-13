disp("Fibonacci Sequence v1.0")
disp("Copyright (c) 2020 miniprime1")
disp(" ")
n = input('Enter Range: ');
disp(" ")
a = 0;
b = 1;
while a < n
    fprintf("%d, ", a)
    t = a;
    a = b;
    b = t + b;
end
disp(" ")