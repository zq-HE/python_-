import tkinter
import flake8
def about_gui():
    t = '个人编程能力评估系统\n' \
        'by：何知谦、杨云波、郑涛'
    about = tkinter.Tk()
    about.geometry('600x400+420+300')
    about.title('关于')
    about.resizable(0,0)
    label = tkinter.Label(about,
                          text=t,
                          font=('黑体', 14),
                          anchor='center')
    label.pack()
    about.mainloop()
