print("Heat Index Calculator v1.0\n")

T = float(input("Enter Temperature (Fahrenheit): "))
R = int(input("Enter Relative Humidity (Percent Integer): "))

HI = -42.379 + 2.04901523*T + 10.14333127*R - 0.22475541*T*R \
    - 6.83783 * (10**(-3))*(T**2) - 5.481717 * (10**(-2))*(R**2) \
    + 1.22874 * (10**(-3))*(T**2)*R + 8.5282 * (10**(-4))*T*(R**2) \
    - 1.99 * (10**(-6))*(T**2)*(R**2)

print("\n", end="")

print(f"T = {T}")
print(f"R = {R}")
print(f"HI = {HI}")