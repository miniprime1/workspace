for i in range(1, 1000+1):
    print(f"Divisor of {i}:", end=" ")
    for j in range(1, i+1):
        if i % j == 0:
            print(j, end=", ")
    print("", end="\n")