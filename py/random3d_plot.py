import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.subplot(1, 1, 1, projection = '3d')

x = np.random.rand(25, 25)
y = np.random.rand(25, 25)
z = np.random.rand(25, 25)

ax.scatter(x, y, z)
plt.show()