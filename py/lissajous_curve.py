import matplotlib.pyplot as plt
import numpy as np

# Print Program Name
print("Lissajous Curve\n")

# Input Variable
a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter m: "))
n = int(input("Enter n: "))
alpha = int(input("Enter alpha: "))
beta = int(input("Enter beta: "))
print("\n", end='')

# Draw Graph
t = np.linspace(0, 2*np.pi, 1000);
x = a * np.sin(m*t + alpha);
y = b * np.sin(n*t + beta);
plt.plot(x, y, 'b', label="Lissajous Curve")
plt.legend()

# Show Plot
plt.show()