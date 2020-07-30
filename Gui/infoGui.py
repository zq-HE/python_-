import tkinter


def info_gui(info):
    win = tkinter.Tk()
    win.geometry('300x70+200+300')
    win.title('关于')
    win.resizable(0,0)
    label = tkinter.Label(win,
                          text='\n'+info,
                          font=('黑体', 12),
                          anchor='center')
    label.pack()
    win.mainloop()



