import random

def place(rooks, target_rooks, N):
    """Thêm 1 quân xe mới vào rooks, không trùng hàng/cột với target_rooks và rooks"""
    row_set = {r for r, _ in target_rooks + rooks}
    col_set = {c for _, c in target_rooks + rooks}

    # Sinh ngẫu nhiên 1 vị trí hợp lệ
    while True:
        r_new = random.randint(0, N - 1)
        c_new = random.randint(0, N - 1)
        if r_new not in row_set and c_new not in col_set:
            return rooks + [(r_new, c_new)]


def goal_test(rooks, N):
    """Đã đặt đủ N quân xe chưa"""
    return len(rooks) == N


def Partial_Observation(target_rooks, N):
    """DFS dùng stack để mở rộng các trạng thái đặt xe"""
    all_state = []
    stack = [target_rooks]

    while stack:
        rooks = stack.pop()
        all_state.append(rooks)

        if goal_test(rooks, N):
            return rooks, all_state  # Trả về kết quả và toàn bộ trạng thái đã thăm

        # Sinh ra 1 hoặc nhiều trạng thái mới từ state hiện tại
        new_state = place(rooks, target_rooks, N)
        stack.append(new_state)

    return None, all_state
