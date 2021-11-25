import math
import numpy as np

def solve(a, b, c, d):
    if (a == 0 and b == 0):
        return np.array([(-d * 1.0) / c])

    elif (a == 0):
        D = c * c - 4.0 * b * d
        if D >= 0:
            D = math.sqrt(D)
            x1 = (-c + D) / (2.0 * b)
            x2 = (-c - D) / (2.0 * b)
        else:
            D = math.sqrt(-D)
            x1 = (-c + D * 1j) / (2.0 * b)
            x2 = (-c - D * 1j) / (2.0 * b)
            
        return np.array([x1, x2])               

    f = ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0                         
    g = (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a **2.0)) + (27.0 * d / a)) / 27.0                      
    h = ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)                          

    if f == 0 and g == 0 and h == 0:            
        if (d / a) >= 0:
            x = (d / (1.0 * a)) ** (1 / 3.0) * -1
        else:
            x = (-d / (1.0 * a)) ** (1 / 3.0)
        return np.array([x, x, x])             

    elif h <= 0:                     
        i = math.sqrt(((g ** 2.0) / 4.0) - h)   
        j = i ** (1 / 3.0)                      
        k = math.acos(-(g / (2 * i)))           
        L = j * -1                              
        M = math.cos(k / 3.0)                   
        N = math.sqrt(3) * math.sin(k / 3.0)    
        P = (b / (3.0 * a)) * -1                
        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P
        return np.array([x1, x2, x3])           

    elif h > 0:                                 
        R = -(g / 2.0) + math.sqrt(h)           
        if R >= 0:
            S = R ** (1 / 3.0)                  
        else:
            S = (-R) ** (1 / 3.0) * -1          
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))                
        else:
            U = ((-T) ** (1 / 3.0)) * -1        
        x1 = (S + U) - (b / (3.0 * a))
        x2 = -(S + U) / 2 - (b / (3.0 * a)) + (S - U) * math.sqrt(3) * 0.5j
        x3 = -(S + U) / 2 - (b / (3.0 * a)) - (S - U) * math.sqrt(3) * 0.5j
        return np.array([x1, x2, x3])

print("Cubic Equation Solver v1.0")
print("Copyright (c) 2021 miniprime1. All rights reserved.")
print("[Equation: ax^3 + bx^2 + cx + d= 0]\n")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))

try:
    print("\nSolving Equation...")
    x1, x2, x3 = solve(a, b, c, d)
    print("Done!\n")

    print("Equation:\n" + str(a) + "x^3 + " + str(b) + "x^2 + " + str(c) + "x + " + str(d) + " = 0" + "\n")

    print("Result:")
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
    print("x3 = " + str(x3))

    
except Exception as err:
    print("Error:", str(err))

# from numpy import sqrt, cbrt
# x1 = - (b / 3*a) \
#      - ( (1 / 3*a) * cbrt( 1/2 * ( 2*(b**3) - 9*a*b*c + 27*(a**2)*d + sqrt( (2*(b**3) - 9*a*b*c + 27*(a**2)*d)**2 - 4*(((b**2)-3*a*c)**3)) ) ) ) \
#      - ( (1 / 3*a) * cbrt( 1/2 * ( 2*(b**3) - 9*a*b*c + 27*(a**2)*d - sqrt( (2*(b**3) - 9*a*b*c + 27*(a**2)*d)**2 - 4*(((b**2)-3*a*c)**3)) ) ) )
# x2 = - (b / 3*a) \
#      + ( ( 1+1j*sqrt(3)/(6*a) ) * cbrt( 1/2 * ( 2*(b**3) - 9*a*b*c + 27*(a**2)*d + sqrt( (2*(b**3) - 9*a*b*c + 27*(a**2)*d)**2 - 4*(((b**2)-3*a*c)**3)) ) ) ) \
#      + ( ( 1-1j*sqrt(3)/(6*a) ) * cbrt( 1/2 * ( 2*(b**3) - 9*a*b*c + 27*(a**2)*d - sqrt( (2*(b**3) - 9*a*b*c + 27*(a**2)*d)**2 - 4*(((b**2)-3*a*c)**3)) ) ) )
# x3 = - (b / 3*a) \
#      + ( ( 1-1j*sqrt(3)/(6*a) ) * cbrt( 1/2 * ( 2*(b**3) - 9*a*b*c + 27*(a**2)*d + sqrt( (2*(b**3) - 9*a*b*c + 27*(a**2)*d)**2 - 4*(((b**2)-3*a*c)**3)) ) ) ) \
#      + ( ( 1+1j*sqrt(3)/(6*a) ) * cbrt( 1/2 * ( 2*(b**3) - 9*a*b*c + 27*(a**2)*d - sqrt( (2*(b**3) - 9*a*b*c + 27*(a**2)*d)**2 - 4*(((b**2)-3*a*c)**3)) ) ) )
    