print("System of Linear Equation Solver v1.0")
print("Math: {ax+by=c, dx+ey=f}\n")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
e = float(input("Enter a: "))
f = float(input("Enter f: "))

print("\n", end="")

if a*e-b*d==0:
    if (a/d)==(b/e) and (a/d)!=(c/f) and (b/e)!=(c/f):
        print("Result: There is no solution.")
    elif (a/d)==(b/e)==(c/f):
        print("Result: There is contless solution.")
else:
    x = (e*f-b*c)/(a*e-b*d)
    y = (a*f-c*d)/(a*e-b*d)
    print(f"Result: x={x}, y={y}")