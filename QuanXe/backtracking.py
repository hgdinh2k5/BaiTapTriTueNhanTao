def generate_domain(n):
    domain = set()
    for i in range(n):
        for j in range(n):
            domain.add((i, j))
    return domain


def check_constrain(rooks, x, y):
    for r, c in rooks:
        if r == x or c == y:
            return False
    return True


def backtracking(rooks, n, domain, states):
    """Backtracking có lưu lại toàn bộ trạng thái duyệt."""
    if len(rooks) == n:
        states.append(list(rooks))  # lưu trạng thái hoàn chỉnh
        return rooks

    for x, y in domain:
        if check_constrain(rooks, x, y):
            rooks.append((x, y))
            states.append(list(rooks))  # lưu sau khi đặt quân mới

            result = backtracking(rooks, n, domain, states)
            if result:
                return result

            rooks.pop()
            states.append(list(rooks))  # lưu trạng thái sau khi backtrack

    return None


def run_backtracking(N):
    domain = generate_domain(N)
    states = []  # danh sách để lưu tất cả các bước
    result = backtracking([], N, domain, states)
    return result, states
