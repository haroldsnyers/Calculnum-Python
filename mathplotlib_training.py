import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)[source]
# num is the nbr of sample points
# if endpoints=True, last sample point is stop
y = np.cos(x)
plt.plot(x, y, linewidth=2.5, label='cos(x)', color='red')
plt.legend(loc='lower right')
plt.show()
