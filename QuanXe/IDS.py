def is_valid(rooks, row, col):
    for (r, c) in rooks:
        if r == row or c == col:
            return False
    return True


def generate_next_states(rooks, n):
    """Sinh trạng thái mới: chỉ thêm quân ở hàng kế tiếp"""
    next_states = []
    row = len(rooks)   # hàng tiếp theo để đặt
    if row >= n:
        return next_states
    for col in range(n):
        if is_valid(rooks, row, col):
            next_states.append(rooks + [(row, col)])
    return next_states


def dls(state, target, depth, N, all_states, current_depth=0):
    """Depth-Limited Search: lưu lại các state theo từng độ sâu"""
    # lưu trạng thái hiện tại vào all_states
    if current_depth not in all_states:
        all_states[current_depth] = []
    all_states[current_depth].append(state)

    if state == target:
        return [state]
    if depth == 0:
        return None

    for next_state in generate_next_states(state, N):
        path = dls(next_state, target, depth - 1, N, all_states, current_depth + 1)
        if path is not None:
            return [state] + path
    return None


def IDS(target, N, max_depth=10):
    """Iterative Deepening Search: trả về path và toàn bộ trạng thái tại từng độ sâu"""
    all_states_per_depth = {}

    for depth in range(max_depth + 1):
        all_states = {}  # lưu state cho lần chạy DLS ở độ sâu này
        path = dls([], target, depth, N, all_states)
        all_states_per_depth[depth] = all_states

        if path is not None:
            return path, all_states_per_depth

    return None, all_states_per_depth
