import random

def compute_conflicts(state):
    """Count number of attacking pairs (rows and diagonals)."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def random_state(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def get_best_neighbor(state):
    n = len(state)
    best_state = list(state)
    best_conflicts = compute_conflicts(state)

    for col in range(n):
        for row in range(n):
            if state[col] == row:
                continue
            neighbor = list(state)
            neighbor[col] = row
            c = compute_conflicts(neighbor)
            if c < best_conflicts:
                best_conflicts = c
                best_state = neighbor
    return best_state, best_conflicts

def hill_climbing(n):
    current = random_state(n)
    current_conflicts = compute_conflicts(current)

    while True:
        neighbor, neighbor_conflicts = get_best_neighbor(current)
        if neighbor_conflicts >= current_conflicts:
            break
        current, current_conflicts = neighbor, neighbor_conflicts

    return current, current_conflicts

# random-restart wrapper (optional, helps escape local maxima)
def random_restart_hill_climb(n, restarts=50):
    best_state, best_conflicts = None, float('inf')
    for _ in range(restarts):
        state, conf = hill_climbing(n)
        if conf < best_conflicts:
            best_state, best_conflicts = state, conf
        if best_conflicts == 0:
            break
    return best_state, best_conflicts

if __name__ == "__main__":
    N = 4
    solution, conflicts = random_restart_hill_climb(N, restarts=100)
    print("Final State:", solution)
    print("Conflicts:", conflicts)
    print("✅ Solution found!" if conflicts == 0 else "⚠️ Local maximum reached.")
