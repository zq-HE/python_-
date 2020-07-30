import json
import pandas as pd
import getpath

def get():
    # 初始数据的获得
    f = open(getpath.get_root_path()+'/data/data.json', encoding='utf-8')
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
        totalC = 0
        graphC = 0
        stringC = 0
        searchC = 0
        treeC = 0
        arrayC = 0
        sortC = 0
        numberC = 0
        ListC = 0
        loadTimes = 0
        data_list = data[key]['cases']
        dic['userId'].append(key)
        for i in range(len(data_list)):
            temp = data_list[i]
            total = total + temp['final_score']
            totalC = totalC + 1
            loadTimes = loadTimes + len(temp['upload_records'])
            if temp['case_type'] == '图结构':
                graph = graph + temp['final_score']
                graphC = graphC + 1
            elif temp['case_type'] == '字符串':
                string = string + temp['final_score']
                stringC = stringC + 1
            elif temp['case_type'] == '查找算法':
                search = search + temp['final_score']
                searchC = searchC + 1
            elif temp['case_type'] == '树结构':
                tree = tree + temp['final_score']
                treeC = treeC + 1
            elif temp['case_type'] == '数组':
                array = array + temp['final_score']
                arrayC = arrayC + 1
            elif temp['case_type'] == '排序算法':
                sort = sort + temp['final_score']
                sortC = sortC + 1
            elif temp['case_type'] == '数字操作':
                number = number + temp['final_score']
                numberC = numberC + 1
            elif temp['case_type'] == '线性表':
                List = List + temp['final_score']
                ListC = ListC + 1
            if i == len(data_list) - 1:
                if graphC == 0:
                    dic['graph'].append(0)
                else:
                    dic['graph'].append(graph / graphC)
                if stringC == 0:
                    dic['string'].append(0)
                else:
                    dic['string'].append(string / stringC)
                if searchC == 0:
                    dic['search'].append(0)
                else:
                    dic['search'].append(search / searchC)
                if treeC == 0:
                    dic['tree'].append(0)
                else:
                    dic['tree'].append(tree / treeC)
                if arrayC == 0:
                    dic['array'].append(0)
                else:
                    dic['array'].append(array / arrayC)
                if sortC == 0:
                    dic['sort'].append(0)
                else:
                    dic['sort'].append(sort / sortC)
                if numberC == 0:
                    dic['number'].append(0)
                else:
                    dic['number'].append(number / numberC)
                if ListC == 0:
                    dic['list'].append(0)
                else:
                    dic['list'].append(List / ListC)
                dic['total'].append(total / (graphC + stringC + searchC + treeC + arrayC + sortC + numberC + ListC))
                dic['loadTimes'].append(
                    loadTimes / (graphC + stringC + searchC + treeC + arrayC + sortC + numberC + ListC))
    first_data_out = pd.DataFrame(dic)
    return first_data_out