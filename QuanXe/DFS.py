def is_valid(rooks, row, col):
    for (r, c) in rooks:
        if r == row or c == col:
            return False
    return True


def generate_next_states(rooks, n):
    """Sinh trạng thái mới: chỉ thêm 1 quân ở hàng kế tiếp"""
    next_states = []
    row = len(rooks)   # hàng kế tiếp
    if row >= n:
        return next_states
    for col in range(n):
        if is_valid(rooks, row, col):
            next_states.append(rooks + [(row, col)])
    return next_states


def DFS(target_rooks, N):
    stack = [[]]  # bắt đầu từ trạng thái rỗng
    visited = set()
    result = []

    while stack:
        rooks = stack.pop()
        state_tuple = tuple(rooks)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        result.append(rooks.copy())# lưu lại để debug/animate

        
        if target_rooks and rooks == target_rooks:
            return result

        if len(rooks) == N:
            continue

        next_states = generate_next_states(rooks, N)
        for state in reversed(next_states):  # DFS -> push ngược để duyệt đúng thứ tự
            stack.append(state)

    return result  # duyệt hết nếu không tìm thấy
