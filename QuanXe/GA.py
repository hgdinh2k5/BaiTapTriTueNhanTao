import random

def random_population(N, popsize):
    return [[(i, random.randint(0, N - 1)) for i in range(N)] for _ in range(popsize)]


def fitness(ind, target_rooks):
    """Đếm số quân xe đúng vị trí."""
    return sum(1 for r1, c1 in ind if (r1, c1) in target_rooks)


def crossover(p1, p2, N):
    """Lai ghép 2 cá thể tại điểm ngẫu nhiên."""
    p = random.randint(1, N - 2)
    return p1[:p] + p2[p:]


def mutation(ind, N):
    """Đột biến: dịch toàn bộ các quân xe sang phải một lượng ngẫu nhiên."""
    shift = random.randint(1, N - 1)
    return [(r, (c + shift) % N) for r, c in ind]


def tournament_selection(pop, target_rooks, k=3):
    """Chọn cá thể tốt nhất trong k cá thể ngẫu nhiên."""
    selected = random.sample(pop, k)
    return max(selected, key=lambda ind: fitness(ind, target_rooks))


def evolve(N, target_rooks, popsize=200, generations=500, crossover_rate=0.9, mutation_rate=0.2):
    """Chạy quá trình tiến hóa, trả về toàn bộ lịch sử để hiển thị."""
    step = 0
    pop = random_population(N, popsize)
    best = max(pop, key=lambda ind: fitness(ind, target_rooks))
    best_fit = fitness(best, target_rooks)

    states = [(best.copy(), best_fit)]

    for gen in range(generations):
        new_pop = []
        pop.sort(key=lambda ind: fitness(ind, target_rooks), reverse=True)
        new_pop.extend(pop[:2])  # elitism

        while len(new_pop) < popsize:
            p1 = tournament_selection(pop, target_rooks)
            p2 = tournament_selection(pop, target_rooks)

            child = crossover(p1, p2, N) if random.random() < crossover_rate else p1.copy()
            if random.random() < mutation_rate:
                child = mutation(child, N)

            new_pop.append(child)
            step += 1

        pop = new_pop
        current_best = max(pop, key=lambda ind: fitness(ind, target_rooks))
        current_fit = fitness(current_best, target_rooks)

        if current_fit > best_fit:
            best, best_fit = current_best.copy(), current_fit

        states.append((best.copy(), best_fit))

        if best_fit == N:
            break

    return states, step


def genetic_algorithm(N, target_rooks):
    """Bao hàm chính, trả về danh sách các trạng thái."""
    states, step = evolve(N, target_rooks)
    return states, step
