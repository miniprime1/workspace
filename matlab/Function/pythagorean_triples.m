function r = pythagorean_triples(x, y, z)
    % Print the pythagorean triples of the specified range (range1, range2, range3)
    for i = 1:x
        for j = 1:x
            for k = 1:x
                if (i^2 + j^2 == k^2)
                    fprintf("(%d, %d, %d) \n", i, j, k);
                end
            end
        end
    end
end