import tkinter as tk
from config import N, CELL_SIZE, COLOR_LIGHT, COLOR_DARK

class Grid:
    def __init__(self, parent, x=0, y=0):
        """
        parent: root hoặc frame
        x, y: vị trí đặt canvas trong parent
        """
        self.canvas = tk.Canvas(parent, width=N*CELL_SIZE, height=N*CELL_SIZE)
        self.canvas.place(x=x, y=y)
        self.draw_board()

    def draw_board(self):
        """Vẽ bàn cờ N x N"""
        self.canvas.delete("all")
        for i in range(N):
            for j in range(N):
                color = COLOR_LIGHT if (i + j) % 2 == 0 else COLOR_DARK
                self.canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE,
                                             (j+1)*CELL_SIZE, (i+1)*CELL_SIZE,
                                             fill=color)

    def draw_rooks(self, rooks, delay=300):
        """
        Vẽ từng quân xe lần lượt với khoảng trễ giữa mỗi quân.
        """
        self.draw_board()

        def draw_step(i):
            if i < len(rooks):
                row, col = rooks[i]
                x1, y1 = col * CELL_SIZE, row * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE

                self.canvas.create_text((x1 + x2)//2, (y1 + y2)//2,
                                        text="♖", font=("Arial", 28), fill="red")

                self.canvas.update()  # cập nhật ngay để thấy quân mới xuất hiện
                self.canvas.after(delay, draw_step, i + 1)

        draw_step(0)


    def clear(self):
        """Xóa quân cờ nhưng giữ bàn cờ"""
        self.draw_board()
