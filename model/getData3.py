import json
import pandas as pd


def get(path):
    f = open(path, encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    dic = {'userId': [], 'total': [], 'graph': [], 'string': [], 'search': [], 'tree': [], 'array': [], 'sort': [],
           'number': [], 'list': [], 'loadTimes': []}

    for key in data:
        total = 0
        graph = 0
        string = 0
        search = 0
        tree = 0
        array = 0
        sort = 0
        number = 0
        List = 0
        loadTimes = 0
        data_list = data[key]['cases']
        dic['userId'].append(key)
        for i in range(len(data_list)):
            temp = data_list[i]
            total = total + temp['final_score']
            loadTimes = loadTimes + len(temp['upload_records'])
            if temp['case_type'] == '图结构':
                graph = graph + temp['final_score']
            elif temp['case_type'] == '字符串':
                string = string + temp['final_score']
            elif temp['case_type'] == '查找算法':
                search = search + temp['final_score']
            elif temp['case_type'] == '树结构':
                tree = tree + temp['final_score']
            elif temp['case_type'] == '数组':
                array = array + temp['final_score']
            elif temp['case_type'] == '排序算法':
                sort = sort + temp['final_score']
            elif temp['case_type'] == '数字操作':
                number = number + temp['final_score']
            elif temp['case_type'] == '线性表':
                List = List + temp['final_score']
            if i == len(data_list) - 1:
                if graph / 12 > 100:
                    dic['graph'].append(100)
                else:
                    dic['graph'].append(graph / 12)
                if string / 17 > 100:
                    dic['string'].append(100)
                else:
                    dic['string'].append(string / 17)
                if search / 20 > 100:
                    dic['search'].append(100)
                else:
                    dic['search'].append(search / 20)
                if tree / 28 > 100:
                    dic['tree'].append(100)
                else:
                    dic['tree'].append(tree / 28)
                if array / 44 > 100:
                    dic['array'].append(100)
                else:
                    dic['array'].append(array / 44)
                if sort / 11 > 100:
                    dic['sort'].append(100)
                else:
                    dic['sort'].append(sort / 11)
                if number / 35 > 100:
                    dic['number'].append(100)
                else:
                    dic['number'].append(number / 35)
                if List / 30 > 100:
                    dic['list'].append(100)
                else:
                    dic['list'].append(List / 30)
                dic['total'].append(total / 197)
                dic['loadTimes'].append(loadTimes / 197)
    first_data_out = pd.DataFrame(dic)
    return first_data_out
