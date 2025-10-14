def generate_domain(n):
    """Khởi tạo miền: tất cả các ô trên bàn cờ"""
    return {(i, j) for i in range(n) for j in range(n)}

def remove_inconsistent_values(rooks, domain):
    """Loại bỏ các ô không hợp lệ dựa trên quân đã đặt"""
    new_domain = set()
    for x, y in domain:
        valid = True
        for r, c in rooks:
            if r == x or c == y or abs(r - x) == abs(c - y):  # kiểm tra hàng, cột, đường chéo
                valid = False
                break
        if valid:
            new_domain.add((x, y))
    return new_domain

def ac3_backtracking(rooks, n, domain, states):
    """Backtracking kết hợp AC-3"""
    # Lưu trạng thái hiện tại
    states.append((list(rooks), set(domain)))

    # Nếu đủ n quân, trả về nghiệm
    if len(rooks) == n:
        return list(rooks)

    # Cập nhật miền bằng AC-3
    domain = remove_inconsistent_values(rooks, domain)

    for x, y in list(domain):
        rooks.append((x, y))
        new_domain = set(domain)
        new_domain.remove((x, y))  # loại bỏ ô vừa đặt
        states.append((list(rooks), new_domain))

        result = ac3_backtracking(rooks, n, new_domain, states)
        if result:
            return result

        rooks.pop()
        states.append((list(rooks), new_domain))  # lưu trạng thái sau khi backtrack

    return None

def run_ac3_backtracking(N):
    domain = generate_domain(N)
    states = []  # lưu toàn bộ trạng thái
    result = ac3_backtracking([], N, domain, states)
    return result, states


