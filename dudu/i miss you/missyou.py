import tkinter as tk
import random
import threading
import time

def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('亲爱的')
    window.geometry("220x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='我想你了！杜杜',
             bg='pink',
             font=('楷体', 18),
             width=25, height=4
             ).pack()
    window.mainloop()

threads = []
# 创建200个线程，每个线程执行dow函数
for i in range(200):
    t = threading.Thread(target=dow)
    threads.append(t)
    # 线程间休眠0.01秒，避免同时创建窗口可能的冲突
    time.sleep(0.01)
    threads[i].start()