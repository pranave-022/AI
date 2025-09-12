#Implement A* algorithm using Manhattan and Misplaced tiles
import heapq

def manhattan(state, goal):
    n = int(len(state) ** 0.5) 
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0: 
            continue
        goal_index = goal.index(tile)
        x1, y1 = divmod(i, n)
        x2, y2 = divmod(goal_index, n)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def misplaced(state, goal):
    return sum(1 for i, tile in enumerate(state) if tile != 0 and tile != goal[i])

def heuristic(state, goal, h_type="manhattan"):
    if h_type == "manhattan":
        return manhattan(state, goal)
    elif h_type == "misplaced":
        return misplaced(state, goal)
    else:
        raise ValueError("Unknown heuristic type")

def a_star(start_state, goal_state, h_type="manhattan"):
    open_set = []
    visited = set()

    g = 0
    h = heuristic(start_state, goal_state, h_type)
    f = g + h

    heapq.heappush(open_set, (f, g, start_state, []))

    while open_set:
        f, g, state, path = heapq.heappop(open_set)

        if state == goal_state:
            return path + [state]

        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        n = int(len(state) ** 0.5)
        blank_index = state.index(0)
        x, y = divmod(blank_index, n)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_index = nx * n + ny
                new_state = state[:]
                new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]

                if tuple(new_state) not in visited:
                    new_g = g + 1
                    new_h = heuristic(new_state, goal_state, h_type)
                    new_f = new_g + new_h
                    heapq.heappush(open_set, (new_f, new_g, new_state, path + [state]))

    return "No solution"

if __name__ == "__main__":
    start = [1, 2, 3,
             4, 0, 6,
             7, 5, 8]

    goal = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

    print("Using Manhattan heuristic:")
    path = a_star(start, goal, "manhattan")
    for step in path:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()

    print("Steps taken:", len(path)-1)
