import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
x = [['A panel', 'A panel', 'edge'],
     ['C panel', '.',       'edge']]
fig, axs = plt.subplot_mosaic([['linear', 'linear-log'],
                               ['linear', 'linear222']], layout='constrained')
for ax_name, ax in axs.items():
    ax.text(0.5, 0.5, ax_name, ha='center', va='center')
for ax_name, ax in axs.items():
    ax.text(0.5, 0.5, ax_name, ha='center', va='center')
plt.show()