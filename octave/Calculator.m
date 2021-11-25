disp('Calculator v1.0')
disp('Copyright (C) 2020 miniprime1')
disp(' ')
disp('Options')
disp('1. Add')
disp('2. Subtract')
disp('3. Multiply')
disp('4. Divide')
opt = input('Enter choice: ');
disp(' ')
if (opt == 1)
    x = input('Enter 1st input: ');
    y = input('Enter 2nd input: ');
    disp(' ')
    disp('Result')
    fprintf("%f + %f = %f", x, y, x+y);
elseif (opt == 2)
    disp('Input')
    x = input('Enter 1st input: ');
    y = input('Enter 2nd input: ');    
    disp(' ')
    disp('Result')
    fprintf("%f - %f = %f", x, y, x-y);
elseif (opt == 3)
    x = input('Enter 1st input: ');
    y = input('Enter 2nd input: ');
    disp(' ')
    disp('Result')
    fprintf("%f * %f = %f", x, y, x*y);
elseif (opt == 4)
    x = input('Enter 1st input: ');
    y = input('Enter 2nd input: ');
    disp(' ')
    disp('Result')
    fprintf("%f / %f = %f", x, y, x/y);
else
    disp('Error: Invalid choice')
end

clear
