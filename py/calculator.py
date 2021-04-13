print("Calculator, version 1.0")
print("Copyright (C) 2020 miniprime1")
print("")

print("Options")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice: ")
 
print()
if choice == "1":
    x = float(input("Enter 1st input: "))
    y = float(input("Enter 2nd input: "))
    print("")
    print("Result")
    print(x, "+", y, "=", x + y)
elif choice == "2":
    x = float(input("Enter 1st input: "))
    y = float(input("Enter 2nd input: "))
    print("")
    print("Result")
    print(x, "-", y, "=", x - y)
elif choice == "3":
    x = float(input("Enter 1st input: "))
    y = float(input("Enter 2nd input: "))
    print("")
    print("Result")
    print(x, "*", y, "=", x * y)
elif choice == "4":
    x = float(input("Enter 1st input: "))
    y = float(input("Enter 2nd input: "))
    print("")
    print("Result")
    print(x, "/", y, "=", x / y)
else:
    print("Error: Invalid Choice")
