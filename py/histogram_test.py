# my first histogram
# something wrong shape

import matplotlib.pyplot as plt
import numpy as np

data = [5, 10,
        15, 20,
        25, 25, 25, 30, 30, 30, 
        35, 40,
        45, 50]

plt.hist(data)
plt.show()