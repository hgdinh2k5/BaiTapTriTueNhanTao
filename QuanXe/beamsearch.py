def is_valid(rooks, row, col):
    """Kiểm tra có đặt quân xe hợp lệ không"""
    for (r, c) in rooks:
        if r == row or c == col:
            return False
    return True


def generate_next_states(rooks, n):
    """Sinh các trạng thái tiếp theo hợp lệ"""
    next_states = []
    for r in range(n):
        for c in range(n):
            if (r, c) not in rooks and is_valid(rooks, r, c):
                next_states.append(rooks + [(r, c)])
    return next_states


def heuristic(state, target):
    """Hàm đánh giá: càng ít quân sai vị trí càng tốt"""
    return len(target) - sum([1 for r in state if r in target])


def beam_search(target_rooks, N, beam_width=3):
    """
    Thuật toán Beam Search để sắp quân giống target_rooks.
    Trả về danh sách 'history' gồm các beam qua từng bước để hiển thị.
    """
    frontier = [[]]  # bắt đầu từ trạng thái rỗng
    history = []     # lưu danh sách các beam theo từng vòng lặp

    while frontier:
        new_frontier = []
        history.append(frontier.copy())  # 🟢 Lưu toàn bộ beam hiện tại

        # kiểm tra xem đã đạt mục tiêu chưa
        for state in frontier:
            if state == target_rooks:
                history.append([state])
                return history

        # sinh tất cả trạng thái con hợp lệ từ beam hiện tại
        for state in frontier:
            next_states = generate_next_states(state, N)
            new_frontier.extend(next_states)

        # nếu có nhiều hơn beam_width thì chỉ giữ top-k theo heuristic
        if new_frontier:
            new_frontier.sort(key=lambda x: heuristic(x, target_rooks))
            frontier = new_frontier[:beam_width]
        else:
            break

    return history
