from math import sqrt

print("Pi Calculator v1.0")
print("Copyright (c) 2021 miniprime1")
print("[Precision: input * 100k]\n")

value, temp, answer = 0, 0, 0
precision = int(input("Enter precision: "))

try:
    print("\nCalculating pi...")
    for i in range(precision*100000):
        temp = 1 / ((i+1)**2)
        value += temp
    answer = sqrt(value*6)
    print("Done!")
except Exception as err:
    print("Error:", str(err))

print("\nResult:")
print("%.10f" % answer)