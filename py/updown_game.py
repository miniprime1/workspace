import random

print("Up/Down Game v1.0")
print("Copyright (c) 2020 miniprime1\n")

print("Difficult")
print("1. Easy (1~10)")
print("2. Normal (1~100)")
print("3. Hard (1~1000)")
print("4. Extreme (1~10000)")
print("5. Custom (?~?)")
opt = input("Your choice: ")

if int(opt) == 1: 
    ans = random.randrange(1, 11)
    print("\nDifficult: Easy (1~10)")
elif int(opt) == 2: 
    ans = random.randrange(1, 101)
    print("\nDifficult: Normal (1~100)")
elif int(opt) == 3: 
    ans = random.randrange(1, 1001)
    print("\nDifficult: Hard (1~1000)")
elif int(opt) == 4: 
    ans = random.randrange(1, 10001)
    print("\nDifficult: Extreme (1~10000)")
elif int(opt) == 5:
    x = input("\nEnter 1st input: ")
    y = input("Enter 2nd input: ")
    print("\nDifficult: Custom (" + x + "~" + y + ")")
    ans = random.randrange(int(x), int(y) + 1)
else: 
    ans = random.randrange(1, 1000001)
    print("\nDifficult: Error (1~1000000)")

while True:
    you = int(input("\nEnter number: "))
    if you > ans: print("Down!")
    if you < ans: print("Up!")
    if you == ans: break

print("Answer!")

input("\nPress enter key to exit")