import random
print("Human Verifiacation v1.0\n")
code = random.randrange(100000, 1000000)
print("Verification Code:", code)
i = input("Enter Verification Code: ")
if int(i) == code: print("\nHuman Verification Successful!")
else: print("\nHuman Verification Falied!")
input("\nPress enter key to exit")