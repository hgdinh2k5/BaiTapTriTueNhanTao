from queue import PriorityQueue

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


def cost_function(state):
    
    return len(state)


def UCS(target_rooks, N):
    pq = PriorityQueue()
    pq.put((0, []))  
    visited = set()
    result = []

    while not pq.empty():
        cost, rooks = pq.get()

        state_tuple = tuple(rooks)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        result.append((rooks.copy(), cost))

        if rooks == target_rooks:
            return result

        for next_state in generate_next_states(rooks, N):
            step_cost = cost_function(next_state)
            pq.put((step_cost, next_state))

    return result
