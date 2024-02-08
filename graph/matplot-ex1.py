import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 10])  # Plot some data on the axes.
plt.show()

fig2, ax2 = plt.subplots()  #
ax2.plot([2.5, 4, 3, 6])
plt.show()

fig3, ax3 = plt.subplots()
ax3.plot(0.4, 1, 1.2, 4, 3, 2, 4, 10)
plt.show()

