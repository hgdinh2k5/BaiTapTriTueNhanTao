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


def forward_checking(domain, x, y):
    new_domain = set()
    for r, c in domain:
        if x == r or y == c:
            continue
        new_domain.add((r, c))
    return new_domain


def backtracking(rooks, n, domain, all_states):
    # Lưu lại trạng thái hiện tại (copy để không bị thay đổi sau)
    all_states.append(rooks.copy())

    # Nếu đã đặt đủ N quân thì trả kết quả
    if len(rooks) == n:
        return rooks

    for x, y in domain:
        if check_constrain(rooks, x, y):
            rooks.append((x, y))
            new_domain = forward_checking(domain, x, y)
            result = backtracking(rooks, n, new_domain, all_states)
            if result:
                return result
            rooks.pop()  # backtrack

    return None


def run_forwardchecking(N):
    domain = generate_domain(N)
    all_states = []
    result = backtracking([], N, domain, all_states)
    return result, all_states
