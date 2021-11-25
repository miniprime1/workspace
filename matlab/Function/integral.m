function y = integral(x, n)
    % Returns the integral of function y=x^n
    C = sym('C');
    if n == -1
        y = log(abs(x)) + C;
    else
        y = (x^(n+1))/(n+1) + C;
    end
end