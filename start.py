# Please follow the Apache license
# 这是启动界面
# import python begin
import tkinter as tk
# import otherfiles begin
import utime as test
# import end
# GUI BEGIN
window = tk.Tk()
window.title('转换时间戳至可读日期')
window.geometry('500x300')
l = tk.Label(window, text='你好！请输入秒级unix时间戳，谢谢', bg='green', font=('Arial', 12), width=30, height=2)
l.pack()
window.mainloop()
print(test)