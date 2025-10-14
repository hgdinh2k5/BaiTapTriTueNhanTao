import tkinter as tk
from tkinter import ttk
from grid import Grid
from button import Button
import random
from config import N, CELL_SIZE
from backtracking import *
from forwardchecking import *
from DFS import *
from BFS import *
from UCS import *
from IDS import *
from Greedy import *
from A_star import *
from Hill_Climbing import *
from beamsearch import *
from GA import *
from Simulated_Anneling import *
import time
from and_or_search import *
from AC3 import *
from Sensorless import *
from Partial_observation import *
from DLS import *
# =============================
# Global biến
# =============================
rooks_target = [(0,6), (1, 0), (2, 2), (3, 4), (4, 1), (5, 5), (6, 3), (7, 7)]

# =============================
# Random Target
# =============================
def random_target(is_Partial_Observable_Space=None):
    global rooks_target
    rooks_target = []
    if is_Partial_Observable_Space:
        set_r = set()
        set_c = set()
        n = random.randint(1, N)
        for i in range(n):
            r = random.randint(0, N - 1)
            c = random.randint(0, N - 1)
            if r not in set_r and c not in set_c:
                set_r.add(r)
                set_c.add(c)
                rooks_target.append((r, c))
        grid_target.draw_rooks(rooks_target, 0)
    else:
        cols = list(range(N))
        random.shuffle(cols)
        for c, r in enumerate(cols):
            rooks_target.append((c, r))
        grid_target.draw_rooks([(i, cols[i]) for i in range(N)], 0)

# =============================
# GUI Tkinter
# =============================
root = tk.Tk()
root.state('zoomed')
root.title("Quân xe")

# Bàn cờ bên trái: dùng cho thuật toán
grid_algo = Grid(root, x=50, y=50)

# Bàn cờ giữa: Target Rooks
grid_target = Grid(root, x=470, y=50)
grid_target.draw_rooks(rooks_target, 0)


# =============================
# Text hiển thị path
# =============================
txt_path = tk.Text(root, font=("Arial", 11), wrap="word")
txt_path.place(x=1025, y=30, width=500, height=750)

# =============================
# Panel hiển thị thời gian và bước đi
# =============================
panel_info = tk.Frame(root, bg="lightgray")
panel_info.place(x=10, y=490, width=500, height= 100)

lbl_time = tk.Label(panel_info, text="Thời gian chạy: -- giây", font=("Arial", 14, "bold"))
lbl_time.pack(anchor="w")

lbl_steps = tk.Label(panel_info, text="Số bước: --", font=("Arial", 14, "bold"))
lbl_steps.pack(anchor="w")



# =============================
# Thuật toán
# =============================
def run_backtrack():
    start = time.time()
    result, path = run_backtracking(N)
    end = time.time()
    elapsed = end - start
    grid_algo.draw_rooks(result)
    txt_path.delete("1.0", tk.END)   # xóa text cũ
    txt_path.insert(tk.END, "Backtracking Path:\n")
    for i in range(len(path)):
        txt_path.insert(tk.END, f"Step {i}: {path[i]}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(path)} bước")

def run_forwardcheck():
    start = time.time()
    result, path = run_forwardchecking(N)
    end = time.time()
    elapsed = end - start
    grid_algo.draw_rooks(result)
    txt_path.delete("1.0", tk.END)   # xóa text cũ
    txt_path.insert(tk.END, "Forwardchecking Path:\n")
    for i in range(len(path)):
        txt_path.insert(tk.END, f"Step {i}: {path[i]}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(path)} bước")

def run_dfs():
    start = time.time()
    result = DFS(rooks_target, N)
    end = time.time()
    elapsed = end - start
    grid_algo.draw_rooks(result[-1])
    txt_path.delete("1.0", tk.END)   # xóa text cũ
    txt_path.insert(tk.END, "DFS Path:\n")
    for i in range(len(result)):
        txt_path.insert(tk.END, f"Step {i}: {result[i]}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(result)} bước")

def run_bfs():
    start = time.time()
    result = BFS(rooks_target, N)
    end = time.time()
    elapsed = end - start
    grid_algo.draw_rooks(result[-1])
    txt_path.delete("1.0", tk.END)   # xóa text cũ
    txt_path.insert(tk.END, "BFS Path:\n")
    for i in range(len(result)):
        txt_path.insert(tk.END, f"Step {i}: {result[i]}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(result)} bước")


def run_ucs():

    start = time.time()
    result = UCS(rooks_target, N)
    end = time.time()
    elapsed = end - start
    grid_algo.draw_rooks(result[-1][0])
    txt_path.delete("1.0", tk.END)   # xóa text cũ
    txt_path.insert(tk.END, "UCS Path:\n")
    for i in range(len(result)):
        txt_path.insert(tk.END, f"Step {i}: {result[i][0]} - cost = {result[i][1]}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(result)} bước")


def run_dls():
    start = time.time()
    result, all_states = run_dls_module(rooks_target, N)
    end = time.time()
    elapsed = end - start
    txt_path.delete("1.0", tk.END)
    txt_path.insert(tk.END, "IDS Path:\n")
    grid_algo.draw_rooks(result)
    for i in range(0, 200):
        txt_path.insert(tk.END, f"  {all_states[i]}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(all_states)} bước")

def run_ids():
    start = time.time()
    path, all_states = IDS(rooks_target, N, max_depth=10)
    end = time.time()
    elapsed = end - start

    if path:
        grid_algo.draw_rooks(path[-1])

    # hiển thị vào text
    txt_path.delete("1.0", tk.END)
    txt_path.insert(tk.END, "IDS Path:\n")

    step = 0
    # in toàn bộ trạng thái theo độ sâu
    for depth, states in all_states.items():
        txt_path.insert(tk.END, f"\nDepth {depth}:\n")
        
        for st in states.get(depth, []):   # tránh lỗi nếu depth trống
            txt_path.insert(tk.END, f"  {st}\n")
            step += 1
            

    lbl_time.config(text=f"Thời gian chạy: {elapsed:.6f} giây")
    if path:
        lbl_steps.config(text=f"Số bước: {step} bước")
    else:
        lbl_steps.config(text="Không tìm thấy kết quả")


def run_greedy():
    start = time.time()
    result = greedy(rooks_target, N)
    end = time.time()
    elapsed = end - start
    grid_algo.draw_rooks(result[-1][0])
    txt_path.delete("1.0", tk.END)   # xóa text cũ
    txt_path.insert(tk.END, "Greedy Path:\n")
    for i in range(len(result)):
        txt_path.insert(tk.END, f"Step {i}: {result[i][0]} - h(x) = {result[i][1]}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(result)} bước")
    

def run_astar():
    start = time.time()
    result = A_star(rooks_target, N)
    end = time.time()
    elapsed = end - start
    grid_algo.draw_rooks(result[-1][0])
    txt_path.delete("1.0", tk.END)   # xóa text cũ
    txt_path.insert(tk.END, "Astar path:\n")
    for i in range(len(result)):
        txt_path.insert(tk.END, f"Step {i}: {result[i][0]} - f(x) = {result[i][1]}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(result)} bước")
    
    

def run_hill():
    

    start = time.time()
    result = hill_climbing(rooks_target, N)
    end = time.time()
    elapsed = end - start
    grid_algo.draw_rooks(result[-1][0])
    txt_path.delete("1.0", tk.END)   # xóa text cũ
    txt_path.insert(tk.END, "Hill Climbing Path:\n")
    for i in range(len(result)):
        txt_path.insert(tk.END, f"Step {i}: {result[i][0]} - f(x) = {result[i][1]}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(result)} bước")

def run_beam():
    start = time.time()
    history = beam_search(rooks_target, N, beam_width=2)
    end = time.time()
    elapsed = end - start

    if history:
        # Beam cuối cùng trong lịch sử tìm kiếm
        final_beam = history[-1]
        # Lấy trạng thái đầu tiên trong beam (tốt nhất)
        final_state = final_beam[0]

        grid_algo.draw_rooks(final_state)

        # Hiển thị thông tin trong Text box
        txt_path.delete("1.0", tk.END)
        txt_path.insert(tk.END, "Beam Search Path:\n")
        step_beam = 0

        # In ra từng bước (beam)
        for step, beam in enumerate(history):
            txt_path.insert(tk.END, f"\nStep {step} (beam size = {len(beam)}):\n")
            for state in beam:
                txt_path.insert(tk.END, f"  {state}\n")
                step_beam += 1

        lbl_time.config(text=f"Thời gian chạy: {elapsed:.6f} giây")
        lbl_steps.config(text=f"Số bước: {step_beam}")

def run_genetic():
    start = time.time()
    states, step = genetic_algorithm(N, rooks_target)
    end = time.time()
    elapsed = end - start

    final_state, best_fit = states[-1]
    grid_algo.draw_rooks(final_state)

    txt_path.delete("1.0", tk.END)
    txt_path.insert(tk.END, "Genetic Algorithm Path:\n")
    for i in range(max(0, len(states) - 10), len(states)):
        state, fit = states[i]
        txt_path.insert(tk.END, f"Gen {i}: fitness = {fit}\n")

    lbl_time.config(text=f"Thời gian chạy: {elapsed:.6f} giây")
    lbl_steps.config(text=f"Số bước: {step}")




def run_Simulated():
    start = time.time()
    states = simulated_annealing(rooks_target, N)
    end = time.time()
    elapsed = end - start

    # Lấy trạng thái cuối cùng
    final_state, h_curr, T, best_state, h_best = states[-1]

    # Vẽ lên lưới
    grid_algo.draw_rooks(final_state)

    # Hiển thị thông tin
    txt_path.delete("1.0", tk.END)
    txt_path.insert(tk.END, "Simulated Annealing Path:\n")

    # In 10 bước cuối cùng (tránh quá dài)
    for i in range(len(states)):
        rooks, h, T, best, h_best = states[i]
        txt_path.insert(
            tk.END,
            f"Step {i}: h = {h}, T = {T:.4f}, best = {h_best}\n"
        )

    lbl_time.config(text=f"Thời gian chạy: {elapsed:.6f} giây")
    lbl_steps.config(text=f"Số bước: {len(states)} bước")


def run_and_or():
    start = time.time()
    found_solution, visited, plan = and_or_graph_search(N)
    end = time.time()
    elapsed = end - start

    # Vẽ trạng thái cuối nếu tìm thấy
    if found_solution:
        grid_algo.draw_rooks(visited[-1])
    else:
        grid_algo.draw_rooks([])

    # Hiển thị thông tin trong Text box
    txt_path.delete("1.0", tk.END)
    txt_path.insert(tk.END, "AND-OR Search Path:\n")

    for i, state in enumerate(visited):
        txt_path.insert(tk.END, f"Step {i}: {state}\n")

    lbl_time.config(text=f"Thời gian chạy: {elapsed:.6f} giây")
    lbl_steps.config(text=f"Số bước: {len(visited)} bước")
    
def run_ac3():
    start = time.time()
    result, states = run_ac3_backtracking(N)
    end = time.time()
    elapsed = end - start
    grid_algo.draw_rooks(result)
    txt_path.delete("1.0", tk.END)   # xóa text cũ
    txt_path.insert(tk.END, "AC3 Path:\n")
    for step, (rooks_state, domain_state) in enumerate(states):
        txt_path.insert(tk.END, f"Step {step}: Rooks={rooks_state}, Domain={domain_state}\n")
    lbl_time.config(text=f"Thời gian chạy: {elapsed} giây")
    lbl_steps.config(text=f"Số bước: {len(states)} bước")

def run_niemtin():
    start = time.time()
    result, all_states, step = Niemtin(N)
    end = time.time()
    elapsed = end - start

    if result:
        grid_algo.draw_rooks(result)
    else:
        grid_algo.draw_rooks([])

    txt_path.delete("1.0", tk.END)
    txt_path.insert(tk.END, "Sensorless Path:\n")

    for i, state in enumerate(all_states[-10:]):  # in 10 bước cuối
        txt_path.insert(tk.END, f"Step {i}: {state}\n")

    lbl_time.config(text=f"Thời gian chạy: {elapsed:.6f} giây")
    lbl_steps.config(text=f"Số bước: {step}")

def run_partial():
    start = time.time()
    result, states = Partial_Observation(rooks_target, N)
    end = time.time()
    elapsed = end - start

    grid_algo.draw_rooks(result)
    txt_path.delete("1.0", tk.END)
    txt_path.insert(tk.END, "Partial Observation Path:\n")
    for i, s in enumerate(states[-10:]):
        txt_path.insert(tk.END, f"Step {i}: {s}\n")

    lbl_time.config(text=f"Thời gian chạy: {elapsed:.6f} giây")
    lbl_steps.config(text=f"Số bước: {len(states)}")

    

# =============================
# Buttons
# =============================
btn_random = Button(root, x=560, y=500, w=120, h=40,
                    text="Random Rooks",
                    color="SystemButtonFace",
                    font=("Arial", 11),
                    action=lambda: random_target())
btn_random_partial = Button(root, x=700, y=500, w=120, h=40,
                    text="Partial Rooks",
                    color="SystemButtonFace",
                    font=("Arial", 11),
                    action=lambda: random_target(1))


btn_bfs = Button(root, x=900, y=30, w=120, h=40,
                 text="BFS",
                 color="SystemButtonFace",
                 font=("Arial", 11),
                 action=run_bfs)
btn_dfs = Button(root, x=900, y=80, w=120, h=40,
                 text="DFS",
                 color="SystemButtonFace",
                 font=("Arial", 11),
                 action=run_dfs)
btn_ucs = Button(root, x=900, y=130, w=120, h=40,
                 text="UCS",
                 color="SystemButtonFace",
                 font=("Arial", 11),
                 action=run_ucs)
btn_ids = Button(root, x=900, y=180, w=120, h=40,
                 text="IDS",
                 color="SystemButtonFace",
                 font=("Arial", 11),
                 action=run_ids)
btn_greedy = Button(root, x=900, y=230, w=120, h=40,
                    text="Greedy",
                    color="SystemButtonFace",
                    font=("Arial", 11),
                    action=run_greedy)
btn_astar = Button(root, x=900, y=280, w=120, h=40,
                   text="A*",
                   color="SystemButtonFace",
                   font=("Arial", 11),
                   action=run_astar)
btn_hill = Button(root, x=900, y=330, w=120, h=40,
                  text="Hill Climbing",
                  color="SystemButtonFace",
                  font=("Arial", 11),
                  action=run_hill)
btn_genetic = Button(root, x=900, y=380, w=120, h=40,
                  text="Genetic Algorithm",
                  color="SystemButtonFace",
                  font=("Arial", 11),
                  action=run_genetic)
btn_beam = Button(root, x=900, y=430, w=120, h=40,
                  text="Beam Search",
                  color="SystemButtonFace",
                  font=("Arial", 11),
                  action=run_beam)
btn_simulate = Button(root, x=900, y=480, w=120, h=40,
                  text="Simulated Anneling",
                  color="SystemButtonFace",
                  font=("Arial", 11),
                  action=run_Simulated)
btn_andor = Button(root, x=900, y=530, w=120, h=40,
                  text="And Or Search",
                  color="SystemButtonFace",
                  font=("Arial", 11),
                  action=run_and_or)
btn_niemtin = Button(root, x=900, y=580, w=120, h=40,
                  text="Sensorless",
                  color="SystemButtonFace",
                  font=("Arial", 11),
                  action=run_niemtin)
btn_partial = Button(root, x=900, y=630, w=120, h=40,
                  text="Partial Obs.",
                  color="SystemButtonFace",
                  font=("Arial", 11),
                  action=lambda: run_partial())
btn_backtrack = Button(root, x=900, y=680, w=120, h=40,
                       text="Backtrack",
                       color="SystemButtonFace",
                       font=("Arial", 11),
                       action=run_backtrack)
btn_forward = Button(root, x=900, y=730, w=120, h=40,
                     text="Forward",
                     color="SystemButtonFace",
                     font=("Arial", 11),
                     action=run_forwardcheck)
btn_ac3 = Button(root, x=770, y=730, w=120, h=40,
                  text="AC3",
                  color="SystemButtonFace",
                  font=("Arial", 11),
                  action=run_ac3)

btn_dls = Button(root, x=770, y=680, w=120, h=40,
                  text="DLS",
                  color="SystemButtonFace",
                  font=("Arial", 11),
                  action=run_dls)




# =============================
root.mainloop()
