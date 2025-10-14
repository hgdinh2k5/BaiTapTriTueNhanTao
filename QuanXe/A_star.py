from queue import PriorityQueue

def is_valid(rooks, row, col):
    """Kiểm tra xem quân mới có hợp lệ không"""
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


def g_cost(rooks):
    """g(x): số quân đã đặt"""
    return len(rooks)


def h_cost(rooks, target_rooks):
    """
    h(x): heuristic
    -> khoảng cách Manhattan giữa quân đã đặt và target
    + số quân còn thiếu
    """
    h_val = 0
    for i in range(len(rooks)):
        r1, c1 = rooks[i]
        r2, c2 = target_rooks[i]
        h_val += abs(r1 - r2) + abs(c1 - c2)

    h_val += (len(target_rooks) - len(rooks))  # quân còn thiếu
    return h_val


def A_star(target_rooks, N):
    pq = PriorityQueue()
    pq.put((0, []))  # (f, state)
    visited = set()
    result = []

    while not pq.empty():
        f, rooks = pq.get()
        state_tuple = tuple(rooks)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        result.append((rooks.copy(), f))

        if rooks == target_rooks:
            return result

        for next_state in generate_next_states(rooks, N):
            g_new = g_cost(next_state)
            h_new = h_cost(next_state, target_rooks)
            f_new = g_new + h_new
            pq.put((f_new, next_state))

    return None
