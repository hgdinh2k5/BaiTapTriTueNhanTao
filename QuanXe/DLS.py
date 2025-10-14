import time
all_state_dls = []

def is_valid(rooks, row, col):
    for (r, c) in rooks:
        if r == row or c == col:
            return False
    return True


def generate_next_states(rooks, n):
    next_states = []
    row = len(rooks)
    if row >= n:
        return next_states
    for col in range(n):
        if is_valid(rooks, row, col):
            next_states.append(rooks + [(row, col)])
    return next_states


def DLS(state, target, N, depth):
    global all_state_dls
    all_state_dls.append(state)

    if state == target:
        return state

    if depth == 0:
        return None

    for next_state in generate_next_states(state, N):
        result = DLS(next_state, target, N, depth - 1)
        if result is not None:
            return result

    return None


def run_dls_module(target, N):
    global all_state_dls
    all_state_dls = []
    solution = DLS([], target, N, depth=N)
    return solution, all_state_dls
