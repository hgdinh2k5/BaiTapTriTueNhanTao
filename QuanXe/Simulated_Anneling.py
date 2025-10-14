import random
import math

def generate_neighbor(rooks, N):
    """Sinh hàng xóm bằng cách thay đổi vị trí 1 quân xe."""
    new_rooks = list(rooks)
    i = random.randint(0, N - 1)
    new_rooks[i] = (i, random.randint(0, N - 1))
    return new_rooks


def random_initial_rooks(N):
    """Khởi tạo ngẫu nhiên dàn quân xe ban đầu."""
    return [(i, random.randint(0, N - 1)) for i in range(N)]


def heuristic(rooks, target_rooks):
    """Tính số quân xe đúng vị trí."""
    return sum(1 for (r, c) in rooks if (r, c) in target_rooks)


def simulated_annealing(target_rooks, N, T=100, alpha=0.95, max_iter=500):
    """Thuật toán Simulated Annealing tìm cách sắp quân giống target."""
    rooks = random_initial_rooks(N)
    best = list(rooks)
    h_best = heuristic(best, target_rooks)
    h_curr = heuristic(rooks, target_rooks)

    # Danh sách lưu lại trạng thái qua từng bước để hiển thị
    states = [(list(rooks), h_curr, T, list(best), h_best)]

    for _ in range(max_iter):
        rooks_new = generate_neighbor(rooks, N)
        h_new = heuristic(rooks_new, target_rooks)
        delta = h_new - h_curr

        # Nếu tốt hơn hoặc vượt qua xác suất e^(-delta/T)
        if delta > 0 or random.random() < math.exp(min(700, delta / max(T, 1e-9))):
            rooks = rooks_new
            h_curr = h_new

        # Cập nhật best nếu có tiến bộ
        if h_curr > h_best:
            best = list(rooks)
            h_best = h_curr

        states.append((list(rooks), h_curr, T, list(best), h_best))
        T *= alpha  # giảm nhiệt độ dần

        if h_best == N:
            break  # nếu đạt mục tiêu hoàn hảo thì dừng

    return states
