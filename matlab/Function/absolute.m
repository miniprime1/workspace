function y = absolute(x)
    if x > 0
        y = x;
    elseif x < 0;
        y = -x;
    else
        y = 0;
    end
end