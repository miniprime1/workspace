disp("Average Calculator v1.0")
disp("Copyright (c) 2020 miniprime1")
disp(" ")
disp("Options")
disp("1. Compute average from row vector (1*n)")
disp("2. Compute average from column vector (n*1)")
disp("3. Compute average from square matrix (n*n)")
opt = input('Enter Choice: ');
dsip(" ")
if (opt == 1)
    disp("Input")
    x = input("Enter input: ");
    disp(" ")
    disp("Result")
    disp(mean(x))
elseif (opt == 2)
    disp("Input")
    x = input("Enter input: ");
    disp(" ")
    disp("Result")
    disp(mean(x))
elseif (opt == 3)
    disp("Input")
    x = input("Enter input: ");
    disp(" ")
    disp("Result")
    disp(mean(mean(x)))
else
    disp('Error: Invalid choice')
end
