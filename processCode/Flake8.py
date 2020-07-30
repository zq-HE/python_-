# run the plugin flake8
'''下载路径'''
import radarchart
import os
def flake88(path):
    p2 = {"Eerr": 1128, "Werr": 295, "Ferr": 2.9, "Cerr": 0, "Nerr": 0, "Herr": 92}
    dirs = os.listdir(path)
    flakeRes = {"Eerr": 0, "Werr": 0, "Ferr": 0, "Cerr": 0, "Nerr": 0, "Herr": 0}
    for dir in dirs:
        op = 'flake8 '+ path +'\\'+dir+'\\' + '.mooctest' + '\\' + 'answer.py'
        try:
            p = os.popen(op)
            res_Str = str(p.read())
            # 报告内容分析
            # 逐行提取报错码类型
            for line in res_Str.splitlines():
                l2 = line.split(' ')
                temp = l2[1]
                errorCode = l2[1][0]
                if errorCode == 'E':
                    flakeRes['Eerr'] += 1
                elif errorCode == 'W':
                    flakeRes['Werr'] += 1
                elif errorCode == 'F':
                    flakeRes['Ferr'] += 1
                elif errorCode == 'C':
                    flakeRes['Cerr'] += 1
                elif errorCode == 'N':
                    flakeRes['Nerr'] += 1
                elif errorCode == 'H':
                    flakeRes['Herr'] += 1
                else:
                    continue

        except Exception:
            print
            ("Error: 非python文件")
    radarchart.get(flakeRes,p2)

