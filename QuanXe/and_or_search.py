# and_or_search.py
def is_valid(state, row, col):
    for (r, c) in state:
        if r == row or c == col:
            return False
    return True


class RooksProblem:
    def __init__(self, N):
        self.N = N
        self.initial_state = []

    def goal_test(self, state):
        return len(state) == self.N

    def actions(self, state):
        row = len(state)
        if row >= self.N:
            return []
        valid_cols = []
        for col in range(self.N):
            if is_valid(state, row, col):
                valid_cols.append(col)
        return valid_cols

    def results(self, state, action):
        
        row = len(state)
        return [state + [(row, action)]]


def or_search(state, problem, path, visited):
    visited.append(state.copy())

    if problem.goal_test(state):
        return state  # trạng thái đạt mục tiêu

    if state in path:
        return None  # tránh vòng lặp

    for action in problem.actions(state):
        result_states = problem.results(state, action)
        plan = and_search(result_states, problem, path + [state], visited)
        if plan is not None:
            return plan

    return None


def and_search(states, problem, path, visited):
    for s in states:
        plan = or_search(s, problem, path, visited)
        if plan is None:
            return None
    return states[-1]


def and_or_graph_search(N):
    problem = RooksProblem(N)
    visited = []
    solution = or_search(problem.initial_state, problem, [], visited)
    return solution, visited, solution
