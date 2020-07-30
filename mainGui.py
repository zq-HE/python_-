import tkinter
import os
import json
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
from Gui import helpPage, infoGui, aboutPage,outputGui
from processCode import downLoadCode, RankData


def download_code():
    j = get_input()
    try:
        js = json.loads(j)

        if  len(js) != 1:
            infoGui.info_gui('输入错误，请重新输入！')
        else:
            downLoadCode.download_zip(js)
        return True
    except Exception:
        infoGui.info_gui('输入错误，请重新输入！')


def get_path():
    return os.getcwd()


def get_input():
    input_text = input_window.get('0.0', 'end')
    return input_text


def out_put():
    input_data = get_input()
    try:
        js = json.loads(input_data)
        if len(js) != 1:
            infoGui.info_gui('格式错误，请重新输入！')
        else:
            o = RankData.print_data(js)
            outputGui.show_output(o)
            show_charts()
    except Exception:
        infoGui.info_gui('格式错误，请重新输入！')


def about_page():
    aboutPage.about_gui()


def help_page():
    helpPage.help_gui()

def show_charts():
    lena = img.imread(get_path()+'\\data\\charts.png')
    lena.shape
    plt.figure(figsize=(9, 9))
    m = plt.get_current_fig_manager()
    # m.window.wm_geometry('+0+0')
    plt.imshow(lena)
    plt.axis('off')
    plt.show()

# 窗口由菜单栏，输入框，确认按钮，输出框组成
root_window = tkinter.Tk()
root_window.geometry("550x630+60+60")
root_window.title("个人编程能力评估")
root_window.resizable(0, 0)  # 窗口大小不可变
root_window.update()

    # 菜单条
menubar = tkinter.Menu(root_window)
root_window.config(menu=menubar)
menubar.add_cascade(label='帮助', command=help_page)
menubar.add_cascade(label='关于', command=about_page)

    # 确认按钮
    # 输入框
input_window = tkinter.Text(root_window, width=61, height=37)
input_window.config(font=('黑体', 12))
input_window.place(x=13, y=21)
label = tkinter.Label(root_window,
                          text='输入数据:',
                          fg='black',
                          font=('黑体', 10),
                          width=10,
                          height=1,
                          anchor='w',
                          )
label.place(x=13, y=0)
button1 = tkinter.Button(root_window, text='开\n始\n评\n估', command=out_put)
button1.place(x=515, y=180)

button2 = tkinter.Button(root_window, text='下\n载\n代\n码', command=download_code)
button2.place(x=515, y=280)

root_window.mainloop()
