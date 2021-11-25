ver = version;
info = sprintf("MATLAB, version %s", ver);
disp(info)
disp("Copyright (c) 1984-2020 The MathWorks, Inc.")
disp(" ")

while true
    i = input('>> ', 's');
    
    if (i == "exit")
        break
    end
    
    try
        eval(i)
    catch
        except = sprintf("'%s' is an unrecognized function or variable.", i);
        disp(except)
    end
end

clear