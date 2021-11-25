disp("Zip v1.0")
disp("Copyright (c) 2020 miniprime1")
disp(" ")
disp("Options")
disp("1. Create Zip Archive")
disp("2. Extract Zip Archive")
opt = input('Enter Choice: ');
disp(" ")

if (opt == 1)
    src = input('Enter Source Directory: ', 's');
    fnm = input('Enter Output File Name: ', 's');
    disp(" ")
    try
        zip(fnm, src)
        disp("Done!")
    catch
        disp("Failed!")
    end
    
elseif (opt == 2)
    src = input('Enter Source File: ', 's');
    odr = input('Enter Output Directory: ', 's');
    disp(" ")
    try
        unzip(src, odr)
        disp("Done!")
    catch
        disp("Failed")
    end
    
end

clear