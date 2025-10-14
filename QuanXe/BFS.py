from collections import deque

def is_valid(rooks, row, col):
    for (r, c) in rooks:
        if r == row or c == col:
            return False
    return True

def generate_next_states(rooks, n):
    """Sinh trạng thái mới: đặt thêm 1 quân vào hàng kế tiếp"""
    next_states = []
    row = len(rooks)   # hàng kế tiếp
    if row >= n:
        return next_states
    for col in range(n):
        if is_valid(rooks, row, col):
            next_states.append(rooks + [(row, col)])
    return next_states

def BFS(target_rooks, N):
    queue = deque([[]])  
    visited = set()
    path = []  # lưu lại quá trình duyệt

    while queue:
        rooks = queue.popleft()
        state_tuple = tuple(rooks)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        path.append(rooks)
        
        # kiểm tra đích
        if rooks == target_rooks:
            return path

        for state in generate_next_states(rooks, N):
            queue.append(state)

    return path  # nếu không tìm thấy
