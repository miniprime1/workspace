print("Tic Tac Toe v1.0")
print("Copyright (c) 2020 miniprime1")

items = [["1","2","3"],["4","5","6"],["7","8","9"]]

def validate(x):
    occupied = True
    for item in items:
        for i in item:
            if i == x:
                occupied = False
    return occupied

def takeseat(x, value):
    for idx, item in enumerate(items):
        for idy,i in enumerate(item):
            if i == x:
               items[idx][idy] = value               

def win(mark):
    return (items[0][0]+items[0][1]+items[0][2] == mark *3) or \
    (items[1][0]+items[1][1]+items[1][2] == mark *3) or \
    (items[2][0]+items[2][1]+items[2][2] == mark *3) or \
    (items[0][0]+items[1][0]+items[2][0] == mark *3) or \
    (items[0][1]+items[1][1]+items[2][1] == mark *3) or \
    (items[0][2]+items[1][2]+items[2][2] == mark *3) or \
    (items[0][0]+items[1][1]+items[2][2] == mark *3) or \
    (items[2][0]+items[1][1]+items[0][2] == mark *3)


turnkey = 0

while True:
    if win("X"):
        print("\n-------------")
        for item in items:
            for i in item: print("|", i, end=" ")
            print("|\n-------------")
        print("X is winner!")
        break
    elif win("O"):
        print("\n-------------")
        for item in items:
            for i in item: print("|", i, end=" ")
            print("|\n-------------")
        print("O is winner!")
        break

    if turnkey%2:value = "X"
    else: value = "O"

    print("\n-------------")
    for item in items:
        for i in item:
            print("|", i, end=" ")
        print("|\n-------------")
    select = input("Please select number: ")

    if validate(select):
        print("Error: Invalid Number!")
        takeseat(select, value)
        turnkey = turnkey + 1
    else:
        takeseat(select, value)
        turnkey = turnkey + 1