import matplotlib.pyplot as plt
import numpy as np

def plot_vector2d(vector2d, origin=[0, 0], **options):
    return plt.arrow(origin[0], origin[1], vector2d[0], vector2d[1],
          head_width=0.2, head_length=0.3, length_includes_head=True,
          width=0.02, 
          **options)

plot_vector2d([1,0], color='g')
plot_vector2d([0,1], color='g')

plot_vector2d([2,10], color='r')
plot_vector2d([3,1], color='r')

plt.axis([-3, 6, -2, 11], 'equal')
plt.xticks(np.arange(-3, 7, 1))
plt.yticks(np.arange(-2, 11, 1))
plt.grid()
plt.show()