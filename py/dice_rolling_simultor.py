import random

print("Dice Rolling Simulator v1.0")
print("Copyright (c) 2020 miniprime1\n")

input("Press enter key to roll dice")
print("")

no = random.randrange(1, 6+1)

if no == 1:
    print("[-----]")
    print("[     ]")
    print("[  O  ]")
    print("[     ]")
    print("[-----]")
    print("Result: 1")
if no == 2:
    print("[-----]")
    print("[ O   ]")
    print("[     ]")
    print("[   O ]")
    print("[-----]")
    print("Result: 2")
if no == 3:
    print("[-----]")
    print("[     ]")
    print("[O O O]")
    print("[     ]")
    print("[-----]")
    print("Result: 3")
if no == 4:
    print("[-----]")
    print("[O   O]")
    print("[     ]")
    print("[O   O]")
    print("[-----]")
    print("Result: 4")
if no == 5:
    print("[-----]")
    print("[O   O]")
    print("[  O  ]")
    print("[O   O]")
    print("[-----]")
    print("Result: 5")
if no == 6:
    print("[-----]")
    print("[O O O]")
    print("[     ]")
    print("[O O O]")
    print("[-----]")
    print("Result: 6")