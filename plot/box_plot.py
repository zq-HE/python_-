import matplotlib.pyplot as plt


def get(data):
    data = data.drop(['userId', 'total', 'loadTimes'], axis=1)
    labels = ['score', 'graph', 'string', 'search', 'tree', 'sort', 'array', 'number', 'list']
    fig, ax = plt.subplots()
    plot = ax.boxplot(data.values, vert=True, patch_artist=True, labels=labels)
    ax.set_title('box_plot')

    colors = ['pink', 'lightblue', 'lightgreen', 'red', 'yellow', 'black', 'gray', 'green', 'white']
    for patch, color in zip(plot['boxes'], colors):
        patch.set_facecolor(color)
    plt.show()