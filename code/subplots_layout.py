import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

"""Basic Quickstart"""
# using subplots
gif1, f1_axes = plt.subplots(ncols=2, nrows=2,
                            constrained_layout=True)
# using gridspec
fig2 = plt.figure(constrained_layout=True)
spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig2)
f2_ax1 = fig2.add_subplot(spec2[0, 0])
f2_ax2 = fig2.add_subplot(spec2[0, 1])
f2_ax3 = fig2.add_subplot(spec2[1, 0])
f2_ax4 = fig2.add_subplot(spec2[1, 1])

"""gridspec for subplots that span rows and columns"""
fig3 = plt.figure(constrained_layout=True)
gs = fig3.add_gridspec(3, 3)
f3_ax1 = fig3.add_subplot(gs[0, :])
f3_ax1.set_title('gs[0, :]')
f3_ax2 = fig3.add_subplot(gs[1, :-1])
f3_ax2.set_title('gs[1, :-1]')
f3_ax3 = fig3.add_subplot(gs[1:, -1])
f3_ax3.set_title('gs[1:, -1]')
f3_ax4 = fig3.add_subplot(gs[-1, 0])
f3_ax4.set_title('[gs[-1, 0]')
f3_ax5 = fig3.add_subplot(gs[-1, -2])
f3_ax5.set_title('gs[-1, -2]')

"""gridspec for subplots with different widths"""
# initialize a uniform grid distribution
# then use numpy indexing and slicing to allocate multiple cells
# for a given subplot
fig4 = plt.figure(constrained_layout=True)
spec4 = fig4.add_gridspec(ncols=2, nrows=2)
anno_opts = dict(xy=(0.5, 0.5), xycoords='axes fraction',
                 va='center', ha='center')
f4_ax1 = fig4.add_subplot(spec4[0, :])
f4_ax1.annotate('GridSpec[0, :]', **anno_opts)
fig4.add_subplot(spec4[1, 0]).annotate('GridSpec[1, 0]', **anno_opts)
fig4.add_subplot(spec4[-1, -1]).annotate('GridSpec[1, 1]', **anno_opts)


# use width_ratios + height_ratios
# only their relative ratio matter, i.e. [1, 2, 4] == [2, 4, 8]
fig5 = plt.figure(constrained_layout=True)
widths = [2, 3, 1.5]
heights = [1, 4, 2]
spec5 = fig5.add_gridspec(ncols=3, nrows=3,
                          width_ratios=widths,
                          height_ratios=heights)
for row in range(3):
    for col in range(3):
        ax = fig5.add_subplot(spec5[row, col])
        label = 'Width: {}\nHeight: {}'.format(widths[col],
                                               heights[row])
        ax.annotate(label, (0.2, 0.5), xycoords='axes fraction',
                            va='center')

# width_ratios and height_ratios can be accepted by subplots
# within the gridspec_kw parameter
gs_kw = dict(width_ratios=widths, height_ratios=heights)
fig6, f6_axs = plt.subplots(ncols=3, nrows=3,
                                 constrained_layout=True,
                                 gridspec_kw=gs_kw)
for r, row in enumerate(f6_axs):
    for c, ax in enumerate(row):
        label = 'Width: {}\nHeight: {}'.format(widths[c],
                                               heights[r])
        ax.annotate(label, (0.4, 0.7), xycoords='axes fraction',
                    va='center', ha='center')

"""combine subplots and gridspec"""
fig7, f7_axs = plt.subplots(ncols=3, nrows=3)
gs = f7_axs[0, 0].get_gridspec()
# or gs = gridspec.Gridspec(3, 3)
# f7_axs[0, 0].get_gridspec() == f7_axs[1, 2].get_gridspec()
# removing the underlying axes
for ax in f7_axs[1:, -1]:
    ax.remove()
# fill with a new subplot
axbig = fig7.add_subplot(gs[1:, -1])
axbig.annotate('Big Axes\nGridSpec[1:, -1]', (0.5, 0.2),
               xycoords='axes fraction',
               va='center',ha='center')

"""fine adjustment to a Gridspec layout"""
# this is not compatible with constrained_layout=True
# or Figure.tight_layout
"""boundary, space"""
fig8 = plt.figure(constrained_layout=False)
gs = fig8.add_gridspec(ncols=3, nrows=3,
                       left=0.3, right=0.8,
                       wspace=0.1, hspace=0.4)
f8_ax1 = fig8.add_subplot(gs[:-1, :])
f8_ax2 = fig8.add_subplot(gs[-1, :-1])
f8_ax3 = fig8.add_subplot(gs[-1, -1])

""" multiple GridSpec on a figure"""
"""one given GridSpec only affects the subplots created by itself"""
fig9 = plt.figure(constrained_layout=False)
gs1 = fig9.add_gridspec(nrows=3, ncols=3,
                        left=0.05, right=0.48,
                        wspace=0.05)
f9_ax1 = fig9.add_subplot(gs1[:-1, :])
f9_ax2 = fig9.add_subplot(gs1[-1:, :-1])
f9_ax3 = fig9.add_subplot(gs1[-1, -1])
gs2 = fig9.add_gridspec(nrows=4, ncols=5,
                        left=0.55, right=0.98,
                        hspace=0.05)
f9_ax4 = fig9.add_subplot(gs2[1:3, :-2])
f9_ax5 = fig9.add_subplot(gs2[3, 1:4])
f9_ax6 = fig9.add_subplot(gs2[:-1, -1])
g9_ax7 = fig9.add_subplot(gs2[-1, -1])

"""subgridspec within gridspec"""
fig10 = plt.figure(constrained_layout=True)
gs0 = fig10.add_gridspec(1, 2)
gs00 = gs0[0].subgridspec(2, 3)
gs01 = gs0[1].subgridspec(3, 2)
for a in range(2):
    for b in range(3):
        fig10.add_subplot(gs00[a, b])
        fig10.add_subplot(gs01[b, a])


"""Nested GridSpec"""
def squiggle_xy(a, b, c, d, i=np.arange(0.0, 2*np.pi, 0.05)):
    return np.sin(i*a) * np.cos(i*b), np.sin(i*c) * np.cos(i*d)

res = np.arange(0.0, 2*np.pi, 0.05)
fig11 = plt.figure(figsize=(12, 12), constrained_layout=False)
outer_grid = fig11.add_gridspec(4, 4,
                                wspace=0.0, hspace=0.0)
for i in range(16):
    inner_grid = outer_grid[i].subgridspec(3, 3,
                                           wspace=0.0,
                                           hspace=0.0)
    a, b = int(i/4)+1, i%4+1
    for j in range(9):
        ax = fig11.add_subplot(inner_grid[j])
        c, d = int(j / 3) + 1, j % 3 + 1
        ax.plot(*squiggle_xy(a, b, c, d))
        # or:
        # ax.plot(np.sin(res*a) * np.cos(res*b), np.sin(res*c) * np.cos(res*d))
        ax.set_xticks([])
        ax.set_yticks([])

all_axes = fig11.get_axes()
for ax in all_axes:
    for sp in ax.spines.values():
        sp.set_visible(False)
    if ax.is_first_row():
        ax.spines['top'].set_visible(True)
    if ax.is_last_row():
        ax.spines['bottom'].set_visible(True)
    if ax.is_first_col():
        ax.spines['left'].set_visible(True)
    if ax.is_first_col():
        ax.spines['right'].set_visible(True)

plt.show()
