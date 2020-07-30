import numpy as np
from Gui import infoGui
from matplotlib import pyplot as plt

'''p1,p2处理'''


#p1为去掉userid和total的个人数据，p2为总数据
def get(p1, p2):
    fig = plt.figure(figsize=(8, 8))
    ax1 = fig.add_subplot(1, 2, 1, polar=True)

    data1 = np.array([i for i in p1.values()]).astype(int)
    data2 = np.array([i for i in p2.values()]).astype(int)
    lable = ['error', 'warning', 'pep8', 'complexity', 'naming', 'hacking']
    types = ['personal', 'average']

    angle = np.linspace(0, 2*np.pi, len(data1), endpoint=False)
    angles = np.concatenate((angle, [angle[0]]))
    data1 = np.concatenate((data1, [data1[0]]))
    data2 = np.concatenate((data2, [data2[0]]))

    ax1.set_thetagrids(angles*180/np.pi, lable, fontproperties="Microsoft Yahei")
    ax1.plot(angles, data1, "o-")
    ax1.set_theta_zero_location('NW')
    ax1.set_rlim(0, 1200)
    ax1.fill(angles, data1, facecolor='b', alpha=0.2)
    ax1.set_rlabel_position(255)
    ax1.plot(angles, data2, "o-")
    ax1.set_theta_zero_location('NW')
    ax1.set_rlim(0, 1200)
    ax1.fill(angles, data2, facecolor='r', alpha=0.2)
    ax1.set_rlabel_position(255)
    ax1.set_title("个人报错与平均报错对比图", fontproperties="SimHei", fontsize=16)
    plt.legend(types, loc=0, ncol=1)
    plt.show()
    return 0

