print("Fibonacci Sequence v1.0")
print("Copyright (c) 2020 miniprime1\n")
n = float(input("Enter limit: "))
print("")
a, b = 0, 1
while a < n:
    print(a, end=', ')
    a, b = b, a+b
print("")
input("\nPress enter key to exit")