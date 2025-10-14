def check_rooks(rooks):
    rows = set()
    cols = set()
    for row, col in rooks:
        if row in rows or col in cols:
            return False  # trùng hàng hoặc cột
        rows.add(row)
        cols.add(col)
    return True


def MoveNiemTin(rooks, N):
    """Di chuyển mỗi quân sang cột kế tiếp (quay vòng nếu vượt N-1)"""
    new_state = []
    for row, col in rooks:
        new_col = (col + 1) % N
        new_state.append((row, new_col))
    return new_state


def DatNiemTin(rooks, N):
    """Thêm 1 quân xe mới vào cột kế tiếp"""
    col = len(rooks)
    for row in range(N):
        new_state = rooks + [(row, col)]
        if check_rooks(new_state):
            return new_state
    return rooks  # nếu không đặt được thì trả lại


def Niemtin(N):
    """Thuật toán niềm tin - mô phỏng quá trình tìm cách đặt N quân xe"""
    stack = [[[], [(0, 1)]]]  # ban đầu có 2 trạng thái niềm tin
    step = 0
    all_state = []

    while stack:
        state_group = stack.pop()
        new_group = []
        step += 1

        for st in state_group:
            # Nếu đủ N quân và hợp lệ → nghiệm thành công
            if len(st) == N and check_rooks(st):
                return st, all_state, step

            # Sinh 2 trạng thái mới từ st
            moved = MoveNiemTin(st, N)
            added = DatNiemTin(st, N)

            if check_rooks(moved):
                new_group.append(moved)
                all_state.append(moved)
            if check_rooks(added):
                new_group.append(added)
                all_state.append(added)

        if new_group:
            stack.append(new_group)

    return None
