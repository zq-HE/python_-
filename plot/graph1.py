from matplotlib import pyplot as plt
import json
import getpath
def show_chart():
    plt.rcParams['font.family'] = ['FangSong']
    fp = open('C:\\Users\\66355\\PycharmProjects\\demo1\\data\\numOfCode.json', encoding='utf-8')
    res = fp.read()
    data = json.loads(res)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x_useless = []
    y_useless = []
    x_all = []
    y_all = []
    tick_site = []
    tick_name = []
    x = 1
    for i in data['代码总数']:
        tick_site.append(x + 0.5)
        tick_name.append(i)
        x_useless.append(x)
        x_all.append(x + 1)
        y_useless.append(data['废代码总数'][i])
        y_all.append(data['代码总数'][i])
        x = x + 3

    plt.bar(x_useless, y_useless, align='center')
    plt.bar(x_all, y_all, align='center')
    ax.set_xticks(tick_site)
    ax.set_xticklabels(tick_name, rotation=30, fontsize=12)
    plt.title('代码统计')
    plt.show()