print("Pythagorean Triples Generator v1.0")
print("Copyright (C) 2020 miniprime1. All rights reserved.")
print("[Form: (a, b, c)]\n")

range1 = input("Enter Range of 'a': ")
range2 = input("Enter Range of 'b': ")
range3 = input("Enter Range of 'c': ")

total = 0
true = 0
false = 0

f = open("pythagorean_triples.txt", 'w')
print("")

for i in range(1, int(range1)+1):
    for j in range(1, int(range2)+1):
        for k in range(1, int(range3)+1):
            total = total + 1;
            if i**2 + j**2 == k**2:
                print(f"({i}, {j}, {k})")
                f.write(f"({i}, {j}, {k})\n")
                true = true + 1
            else:
                false = false + 1

print("")
print(f"true={true}, false={false}, total={total}")
print(f"Total Number of Possible Combinations: {total}")
print(f"Number of Generated Pythagorean Triples: {true}  \n")
print("Result: 'pythagorean_triples.txt'")
f.close()