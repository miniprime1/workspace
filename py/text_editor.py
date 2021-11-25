import sys

print("Text Editor, version 1.0")
print("Copyright (c) 2020 miniprime1\n")

print("Options")
print("1. Write Mode (w)")
print("2. Read Mode (r)")
print("3. Append Mode (a)")
print("4. Exit")
option = input("Your choice: ")

if option == "1":
    path = input("\nEnter path of file to save: ")
    f = open(path, 'w')
    print("")
    print("[ Enter text to write (To exit, type \"EXIT\"): ]")
    print("=" * 50)
    while True:
        before_data = input()
        if before_data == 'EXIT': break
        data = before_data + "\n"
        f.write(data)
    print("=" * 50)
    f.close

elif option == "2":
    path = input("\nEnter path of file to open: ")
    f = open(path, 'r')
    print("")
    print("=" * 50)
    data = f.read()
    print(data)
    print("=" * 50)
    f.close

elif option == "3":
    path = input("\nEnter path of file to open: ")
    f = open(path, 'a')
    print("")
    print("[ Enter text to append (To exit, type \"EXIT\"): ]")
    print("=" * 50)
    while True:
        before_data = input()
        if before_data == 'EXIT': break
        data = before_data + "\n"
        f.write(data)
    print("=" * 50)
    f.close

elif option == "4":
    sys.exit()

else:
    print("\nError: invalid choice")