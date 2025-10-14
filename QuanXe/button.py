import tkinter as tk

class Button:
    def __init__(self, parent, x, y, w, h, text, color, font, action=None):
        """
        parent: root hoặc frame
        x, y: tọa độ
        w, h: kích thước
        text: chữ trên nút
        color: màu nền
        font: tuple, ví dụ ("Arial", 12, "bold")
        action: hàm gọi khi nhấn nút
        """
        self.action = action
        self.button = tk.Button(parent, text=text, bg=color, font=font, command=self.on_click)
        self.button.place(x=x, y=y, width=w, height=h)

    def on_click(self):
        if self.action:
            self.action()
