

def is_valid(rooks, row, col):
    """Kiểm tra quân mới có hợp lệ không"""
    for (r, c) in rooks:
        if r == row or c == col:
            return False
    return True

def generate_next_states(rooks, n):
    """Sinh trạng thái mới: thêm 1 quân ở hàng kế tiếp"""
    next_states = []
    row = len(rooks)
    if row >= n:
        return next_states
    for col in range(n):
        if is_valid(rooks, row, col):
            next_states.append(rooks + [(row, col)])
    return next_states

def h_cost(rooks, target_rooks):
    """
    Heuristic: khoảng cách Manhattan + số quân còn thiếu
    """
    h_val = 0
    for i in range(len(rooks)):
        r1, c1 = rooks[i]
        r2, c2 = target_rooks[i]
        h_val += abs(r1 - r2) + abs(c1 - c2)
    h_val += (len(target_rooks) - len(rooks))  # quân còn thiếu
    return h_val

def hill_climbing(target_rooks, N, max_steps=100):
    state = []  # bắt đầu từ rỗng
    result = [(state, h_cost(state, target_rooks))]

    for _ in range(max_steps):
        neighbors = generate_next_states(state, N)
        if not neighbors:
            break

        # chọn neighbor tốt nhất
        best = min(neighbors, key=lambda s: h_cost(s, target_rooks))
        h_best = h_cost(best, target_rooks)
        h_cur = h_cost(state, target_rooks)

        # nếu tốt hơn thì leo tiếp
        if h_best < h_cur:
            state = best
            result.append((state, h_best))
        else:
            # kẹt ở local optimum
            break

        if state == target_rooks:
            break

    return result
