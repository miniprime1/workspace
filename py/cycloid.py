import matplotlib.pyplot as plt
import numpy as np

# Variable
a = 1

# Cycloid
t = np.linspace(0, 2*np.pi, 1000);
x = a * (t - np.sin(t))
y = a * (1 - np.cos(t))
plt.plot(x, y, "b--", label='Cycloid')

# Circle
xc = np.linspace(-1, 1, 1000);
ycp = 1 + np.sqrt(a**2 - np.power(xc,2));
ycm = 1 - np.sqrt(a**2 - np.power(xc,2));
plt.plot(xc, ycp, "k", label='Circle');
plt.plot(xc, ycm, "k");

# Point
plt.plot(0, 0, "b.", markersize=15, label='Point');

# XY Axis
xax = plt.plot([0, 0], [-1, 3], "k", linewidth=1);
yax = plt.plot([-2, 2*np.pi+1], [0, 0], "k", linewidth=1);

# Prettier Plot
plt.axes().set_aspect('equal')
plt.axis((-1-1, 2*np.pi+1, 0-1, 2*a+1))
plt.grid()
plt.legend()

# Show Plot
plt.show()