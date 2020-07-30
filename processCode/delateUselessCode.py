import os
import re
import json

path = 'D:\\workspace\\codes'
dirs = os.listdir(path)  # 获取所有代码文件夹列表
dic = {'排序算法': 0,
       '查找算法': 0,
       '树结构': 0,
       '图结构': 0,
       '数字操作': 0,
       '数组': 0,
       '线性表': 0,
       '字符串': 0
       }
sum_of_type = {'排序算法': 0,
               '查找算法': 0,
               '树结构': 0,
               '图结构': 0,
               '数字操作': 0,
               '数组': 0,
               '线性表': 0,
               '字符串': 0
               }
for dir in dirs:
    l = dir.split('-')
    print(l)
    user_id = l[0]  # 学生编号
    c_type = l[1]  # 题目类型

    sum_of_type[c_type] += 1

    c_zip = 'http://mooctest-site.oss-cn-shanghai.aliyuncs.com/target/' + l[2] + '.zip'  # 题目zip地址
    file = path + '\\' + dir + '\\.mooctest\\answer.py'  # 代码路径
    fp = open(file, encoding='utf-8')  # 打开文件下python代码
    iter_f = iter(fp)  # 文件迭代器访问
    str1 = ''  # 代码内容
    sum_of_line = 0  # 代码行数
    for line in iter_f:  # 逐行扫描代码
        str1 = str1 + line
        sum_of_line += 1

    pattern1 = re.compile('if')  # 获取if数
    pattern2 = re.compile('print')  #
    pattern3 = re.compile('include')  # 判断是否为c++代码
    list_if = pattern1.findall(str1)
    list_print = pattern2.findall(str1)
    list_include = pattern3.findall(str1)
    fp.close()  # 关闭文件
    if (len(list_include) != 0) or (len(list_print) > 3 and len(list_if) > 3 and sum_of_line < 22):  # 判断是否为废代码
        dic[c_type] += 1  # 统计废代码数量 按类型统计
        print(dir)
        os.rename(path + '\\' + dir, path + '\\' + c_type + '-' + str(dic[c_type]))

print('各类型废代码数量：')
print(dic)
print('代码类型总数：')
print(sum_of_type)
