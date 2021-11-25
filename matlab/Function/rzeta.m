function z = rzeta(s)
    % Returns the Riemann zeta function value of a specified number.
    z = 0;
    for n = [1:10000000]
        z = z + 1/n^s;
    end
end