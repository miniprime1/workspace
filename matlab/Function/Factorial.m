function y=Factorial(x)
    if (rem(x, 1)==0)
        y = 1;
        for tmp=x:-1:1
            y = y*tmp;
        end
    else
        disp("Error using Factorial")
        disp("N must be an array of real non-negative integers.")
    end
    
end