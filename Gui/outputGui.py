import tkinter
def show_output(s):
    win = tkinter.Tk()
    win.geometry("953x630+510+100")
    win.title("个人编程能力评估")
    win.resizable(0, 0)  # 窗口大小不可变
    ouput_window = tkinter.Text(win, width=116, height=37)
    ouput_window.place(x=10, y=22)
    ouput_window.config(font=('黑体', 12))
    label = tkinter.Label(win,
                          text='评估结果：',
                          fg='black',
                          font=('黑体', 10),
                          width=10,
                          height=1,
                          anchor='w',
                          )
    label.place(x=10, y=0)
    ouput_window.delete('0.0', 'end')
    ouput_window.insert(tkinter.INSERT, s)
