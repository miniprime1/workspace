disp("Pythagorean Triples Generator v1.0")
disp("Copyright (C) 2020 miniprime1. All rights reserved.")
disp("[Form: (a, b, c)]")
disp(" ")
range1 = input("Enter Range of 'a': ");
range2 = input("Enter Range of 'b': ");
range3 = input("Enter Range of 'c': ");
total = 0;
true = 0;
false = 0;
f = fopen("pythagorean_triples.txt", 'w');
disp(" ")
for i = 1:range1
    for j = 1:range2
        for k = 1:range3
            total = total + 1;
            if (i^2 + j^2 == k^2)
                fprintf("(%d, %d, %d) \n", i, j, k);
                fprintf(f, "(%d, %d, %d)\n",i,j,k);
                true = true + 1;
            else 
                false = false + 1;
            end
        end
    end
end
disp(" ")
fprintf("true=%d, false=%d, total=%d \n", true, false, total);
fprintf("Total Number of Possible Combinations: %d \n", total);
fprintf("Number of Generated Pythagorean Triples: %d \n\n", true);
disp("Result: 'pythagorean_triples.txt'")