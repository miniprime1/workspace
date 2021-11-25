import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)
y = (1+x)**(1/x)
e = np.exp(1)

plt.plot(x, y, "r-", label="f(x) = (1+x)^(1/x)")
plt.plot(0, e, "go", label="(0, e)")

plt.axis([-3, 3, 0, 5])
plt.title("Plot of Trigonometric Functions")
plt.legend(loc = "upper right")
plt.grid()
plt.show()