disp("Equation Grapher v1.0")
disp("Copyright (c) 2020 miniprime1")
disp("[Variables: (x or y)]")
disp(" ")

syms x y
eq = input('Enter Equation: ');
disp(" ")

try
    ezplot(eq)
    disp("Successful!")
catch
    disp("Error!")
end

clear