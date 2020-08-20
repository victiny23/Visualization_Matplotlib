import matplotlib.pyplot as plt
import numpy as np

suptitle = ['Suptitle A',
            'Suptitle B',
            'Suptitle C']
# create invisible subplots to add titles
fig, big_axes = plt.subplots(figsize=(40, 30),
                            nrows=3, ncols=1, sharey=True)
# add more space between rows
fig.subplots_adjust(hspace=.8)
# set subplot invisible
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.set_title(suptitle[row-1], fontsize=20, y=1.2)
    big_ax.tick_params(labelcolor=(1., 1., 1., 0.0), top='off',
                       bottom='off', left='off', right='off')
    big_ax._frameon = False
# add real subplots
x = np.arange(0, 4*np.pi, 0.05)
rows, cols = 3, 4
for row in range(rows):
    for col in range(cols):
        index = row * cols + col + 1
        ax = fig.add_subplot(rows, cols, index)
        ax.plot(x, np.sin(x+index/4*np.pi), 'r--')
        ax.set_title('Plot: {}'.format(index))
plt.show()

