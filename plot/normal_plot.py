from matplotlib import pyplot as plt
import numpy as np


def get(data):
    # 成绩分布图
    t = np.arange(len(data))
    s = data

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='index', ylabel='final_score',
           title='the final_score of all the data')
    plt.show()