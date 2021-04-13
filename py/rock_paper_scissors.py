import random

print("Rock Paper Scissors v1.0")
print("Copyright (c) 2020 miniprime1")

print("\nYour turn!")
you = int(input("Enter input (1:Rock; 2:Paper; 3:Scissors): "))

print("\nComputer turn!")
com = random.randrange(1, 4)
print("Enter input (1:Rock; 2:Paper; 3:Scissors):", com)

print("")

if you == 1: print("Your choice: Rock")
elif you == 2: print("Your choice: Paper")
else: print("Your choice: Scissors")

if com == 1: print("Computer choice: Rock")
elif com == 2: print("Computer choice: Paper")
else: print("Computer choice: Scissors")

if com == you: print("\nIt's draw!")
elif com == 1 and you == 2: print("\nYou win!")
elif com == 2 and you == 3: print("\nYou win!")
elif com == 3 and you == 1: print("\nYou win!")
else: print("\nComputer win!")

input("\nPress enter key to exit")