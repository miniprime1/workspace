function x = eulergamma()
    syms n k
    x = limit(symsum(1/k, k, 1, n) - log(n), n, inf);
end