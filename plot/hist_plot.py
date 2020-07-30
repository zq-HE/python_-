from matplotlib import pyplot as plt, colors
from matplotlib.ticker import PercentFormatter


def get(data):
    fig, ax = plt.subplots()
    N, bins, patches = ax.hist(data, bins=40)
    # We'll color code by height, but you could use any scalar
    fracs = N / N.max()
    # we need to normalize the data to 0..1 for the full range of the colormap
    norm = colors.Normalize(fracs.min(), fracs.max())
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    ax.set(xlabel='final_score', ylabel='number',
           title='the distribution of final_score')
    plt.grid()
    plt.show()
