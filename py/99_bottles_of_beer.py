bottle = 99
print("99 Bottles of Beer v1.0\n")  
while bottle > 0:
    print("{} bottles of beer on the wall,".format(bottle))
    print("{} bottles of beer!".format(bottle))
    print("You take one down, pass it around,")
    bottle = bottle - 1
    print("{} bottles of beer on the wall!\n".format(bottle))
input("Press enter key to exit")