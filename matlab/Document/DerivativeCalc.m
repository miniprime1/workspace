disp("Derivative Calculator v1.0")
disp(" ")

syms x h f(x) df(x)

f(x) = input('Enter function: ');
df(x) = limit((f(x+h)-f(x))/h, h, 0);

disp(" ")
fprintf("f(x) = %s\n", f(x));
fprintf("f'(x) = %s\n", df(x));