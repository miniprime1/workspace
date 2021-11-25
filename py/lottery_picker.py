from random import *

A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

result = []
bonus = []

print("Lottery Picker v1.0\n")
print("Option")
print("1. Powerball (5/69 + 1/26)")
print("2. Lotto 6/45 (6/45 + 1/45)")
print("3. Other Lottery (x/y + a/b)")
opt = int(input("Enter choice: "))

num = int(input("\nEnter number of ticket(s): "))
print()

if (opt == 1):
    for j in range(num):
        for i in range(5): 
            exec("".join((chr(97+i), "=", "randint(1, 69+1)")))
        
        if (a==b or a==c or a==d or a==e or b==c or b==d or b==e or c==d or c==e or d==e): 
            while (a==b or a==c or a==d or a==e or b==c or b==d or b==e or c==d or c==e or d==e):
                for i in range(5): 
                    exec("".join((chr(97+i), "=", "randint(1, 69+1)")))
        
        bonus = [randint(1, 26+1)]
        result = [a, b, c, d, e]
        result.sort()
        print(result, '/', bonus)

elif (opt == 2):
    for j in range(num):
        for i in range(6): 
            exec("".join((chr(97+i), "=", "randint(1, 45+1)")))

        if (a==b or a==c or a==d or a==e or a==f or b==c or b==d or b==e or b==f or c==d or c==e or c==f or d==e or d==f or e==f): 
            while (a==b or a==c or a==d or a==e or a==f or b==c or b==d or b==e or b==f or c==d or c==e or c==f or d==e or d==f or e==f):
                for i in range(6): 
                    exec("".join((chr(97+i), "=", "randint(1, 45+1)")))
        
        bonus = [randint(1, 45+1)]
        result = [a, b, c, d, e, f]
        result.sort()
        print(result, '/', bonus)

elif (opt == 3):
    nums1 = int(input("Enter number of lottery uses: "))
    high1 = int(input("Enter highest of numbers: "))
    nums2 = int(input("Enter number of bonus number(s): "))
    high2 = int(input("Enter highest of bonus numbers(s): "))
    print()
    if (nums1 <= 26 and nums2 <= 26):
        for k in range(num):
            result.clear()
            bonus.clear()
            for i in range(nums1): exec("".join((chr(97+i), "=", "randint(1,", str(high1)+"+1)")))
            for j in range(nums2): exec("".join((chr(65+j), "=", "randint(1,", str(high2)+"+1)")))
            for r in range(nums1): eval("".join(('result.append(', chr(97+r), ')')))
            for b in range(nums2): eval("".join(('bonus.append(', chr(65+b), ')')))
            result.sort()
            bonus.sort()
            print(result, '/', bonus)
    else:
        print("Error!")