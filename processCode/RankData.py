from model import judge
from plot import normal_plot, hist_plot, box_plot,graph1
import getpath
import json

def print_data(js):
    data = judge.judge(js)
    # 获取rank、final_score、totalRank
    s = '学生评价分排名: '+str(data['rank'])+'\n\n学生个人题目数据: \n'+str(data['personal_data']).split('Name')[0]+'\n\n总体数据:\n'
    temp = '排名{0:>5}{1:>7}{2:>7}{3:>7}{4:>7}{5:>6}{6:>6}{7:>5}{8:>7}{9:>6}{10:>5}{11:>6}'.format(
        '学生ID',
        '评价',
        '平均分',
        '图结构',
        '字符串',
        '查找算法',
        '树结构',
        '数组',
        '排序算法',
        '数字操作',
        '线性表',
        '提交次数')
    for i in range(0,271):
        temp = temp+'\n'+'{0:<4}{1:>6}{2:>10}{3:>10}{4:>10}{5:>10}{6:>9}{7:>9}{8:>9}{9:>9}{10:>9}{11:>9}{12:>9}'.format(
            i,
            data['totalRank']['userId'][i],
            round(data['totalRank']['final_score'][i],3),
            round(data['totalRank']['total'][i],3),
            round(data['totalRank']['graph'][i],3),
            round(data['totalRank']['string'][i],3),
            round(data['totalRank']['search'][i],3),
            round(data['totalRank']['tree'][i],3),
            round(data['totalRank']['array'][i],3),
            round(data['totalRank']['sort'][i],3),
            round(data['totalRank']['number'][i],3),
            round(data['totalRank']['list'][i],3),
            round(data['totalRank']['loadTimes'][i],3))
    return s+temp
