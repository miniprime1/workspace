print("RGB2HEX v1.0")
print("\nRGB")
r = int(input("Enter R: "))
g = int(input("Enter G: "))
b = int(input("Enter B: "))
if (r > 255) | (g > 255) | (b > 255): print("\nError: Please enter valid input: Values for R, G and B should be from 0 to 255 only\n")
result = "#" + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]
print("\nHEX")
print(result)