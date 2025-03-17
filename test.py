import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("我的第一个 Tkinter 窗口")  # 设置窗口标题
root.geometry("400x300")  # 设置窗口大小（宽 x 高）

# 添加一个标签
label = tk.Label(root, text="你好，Tkinter！", font=("Arial", 16))
label.pack(pady=20)  # 将标签放置在窗口中

# 添加一个按钮
def on_button_click():
    label.config(text="按钮被点击了！")

button = tk.Button(root, text="点击我", command=on_button_click)
button.pack(pady=10)

# 运行事件循环
root.mainloop()