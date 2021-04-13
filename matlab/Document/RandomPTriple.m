x = randi([1, 1000]);
y = randi([1, 1000]);
z = randi([1, 1000]);

while (x^2 + y^2 == z^2) == false
    x = randi([1, 1000]);
    y = randi([1, 1000]);
    z = randi([1, 1000]);
end

fprintf("(%d, %d, %d) \n", x, y, z);