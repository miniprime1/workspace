disp("Excel Reader v1.0")
disp(" ")
path = input("Enter path of file to open: ", 's');
data = xlsread(path);
disp(" ")
disp("Result = ")
disp(data)