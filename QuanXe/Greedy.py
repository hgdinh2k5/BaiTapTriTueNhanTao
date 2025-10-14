from queue import PriorityQueue


def is_valid(rooks, row, col):
    for (r, c) in rooks:
        if r == row or c == col:
            return False
    return True


def generate_next_states(rooks, n):
    row = len(rooks)  
    next_states = []
    for col in range(n):
        if is_valid(rooks, row, col):
            new_state = rooks + [(row, col)]
            next_states.append(new_state)
    return next_states

def h(rooks, target_rooks):
    cost = len(target_rooks) - len(rooks)  
    for r1, c1 in rooks:
        for r2, c2 in target_rooks:
            if r1 == r2 or c1 == c2:  
                cost += abs(c2 - c1) + abs(r1 - r2)
    return cost


def greedy(target_rooks, N):
    pq = PriorityQueue()
    pq.put((h([], target_rooks), []))  
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
            pq.put((h(next_state, target_rooks), next_state))

    return None
