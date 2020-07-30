import tkinter
import os
def help_gui():
    t = '使用说明：\n' \
        '输入json格式正确的学生代码提交记录，点\n' \
        '击开始评估，将显示学生个人评估结果，总\n' \
        '体水平。点击下载代码按钮，将按json中url\n' \
        '下载json中学生提交代码，并保存在系统目录\n' \
        'codePackages文件夹内以学生id为文件夹名，\n' \
        '并解压分析代码规范'

    help = tkinter.Tk()
    help.geometry('600x200+420+300')
    help.title('关于')
    help.resizable(0,0)
    label = tkinter.Label(help,
                          text=t,
                          font=('黑体', 14),
                          anchor='center')
    label.pack()
    help.mainloop()
print(os.getcwd())
