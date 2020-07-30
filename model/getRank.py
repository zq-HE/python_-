import pandas as pd
import numpy as np
from scipy.linalg import *


def get(first_data_out):
    # 初始数据的标准化
    temp = first_data_out.set_index('userId')
    second_data_out = ((temp - temp.mean()) / temp.std())
    # print(second_data_out.loc['3544'])

    # 反制loadTimes
    second_data_out['loadTimes'] = -second_data_out['loadTimes']
    # print(second_data_out)

    # 计算相关系数矩阵
    corrM = second_data_out.corr()
    # print(corrM)
    # 计算特征值和特征向量
    npArray = corrM.values
    v, m = np.linalg.eig(npArray)
    # 整理特征值和特征向量
    # 1.排序
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if v[i] < v[j]:
                temp = v[i]
                v[i] = v[j]
                v[j] = temp
                temp = m[:, i]
                m[:, i] = m[:, j]
                m[:, j] = temp
    # 调整特征向量正负
    m = -m
    for i in range(1, 4):
        m[:, i] = -m[:, i]
    # print(m)

    # 计算主成分综合评价值比例
    rate = v / np.sum(v)
    # i=4 则alpha=0.8874471273856057
    # i=5 则alpha=0.9198604254746847
    # i=7 则alpha=0.9710497682465578

    # 计算最终评分，并将排序后的结果输出
    for i in range(4):
        if i == 0:
            res = np.sum(m[i] * second_data_out.values, axis=1) * rate[i]
        else:
            res = res + np.sum(m[i] * second_data_out.values, axis=1) * rate[i]

    final_score = pd.Series(res.tolist())
    # 线性变换
    final_score = (final_score - final_score.min()) / (final_score.max() - final_score.min()) * 100
    first_data_out.insert(1, 'final_score', final_score)
    result = first_data_out.sort_values(by=['final_score'], ascending=[False])
    result = result.reset_index(drop=True)
    return result
