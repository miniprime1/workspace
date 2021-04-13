disp("Text Editor v1.0")
disp("Copyright (c) 2020 miniprime1")
disp(" ")
disp("Options")
disp("1. Write Mode (w)")
disp("1. Read Mode (r)")
disp("3. Append Mode (a)")
option = input("Enter choice: ");
disp(" ")

if (option == 1)
    path = input("Enter path of file to save: ", 's');
    fp = fopen(path, 'w');
    disp(" ")
    disp('[ Enter text to write (To exit, type "EXIT"): ]')
    disp("==================================================")
    while (true)
        data = input("", 's');
        if (data == "EXIT") 
            break 
        end
        fprintf(fp, "%s\n", data);
    end
    disp("==================================================")
    fclose(fp);

elseif (option == 2)
    path = input("Enter path of file to read: ", 's');d
    fp = fopen(path, 'r');
    disp(" ")
    disp("==================================================")
    fprintf("%s\n", fileread(path));
    disp("==================================================")
    fclose(fp);
    
elseif (option == 3)
    path = input("Enter path of file to open/save: ", 's');d
    fp = fopen(path, 'a+');
    disp(" ")
    disp('[ Enter text to write (To exit, type "EXIT"): ]')
    disp("==================================================")
    fprintf("%s\n", fileread(path));
    while (true)
        data = input("", 's');
        if (data == "EXIT") 
            break 
        end
        fprintf(fp, "%s\n", data);
    end
    disp("==================================================")
    fclose(fp);
    
end

clear option
clear path
clear data