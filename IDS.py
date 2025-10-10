from copy import deepcopy

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]] 


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    x, y = find_blank(state)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves


def is_goal(state):
    return state == GOAL_STATE


def depth_limited_search(state, depth_limit, path, visited):
    if is_goal(state):
        return path

    if depth_limit == 0:
        return None  # cutoff

    visited.add(tuple(sum(state, [])))  # flatten the 2D list to tuple for hashability

    for neighbor in get_neighbors(state):
        flat = tuple(sum(neighbor, []))
        if flat not in visited:
            result = depth_limited_search(neighbor, depth_limit - 1, path + [neighbor], visited)
            if result is not None:
                return result

    return None


# Iterative Deepening DFS
def iterative_deepening_search(start_state, max_depth=50):
    for depth in range(max_depth):
        visited = set()
        result = depth_limited_search(start_state, depth, [start_state], visited)
        if result is not None:
            print(f"✅ Solution found at depth {depth}")
            return result
    print("❌ No solution found within depth limit.")
    return None


# --- Example usage ---
if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 6],
             [7, 5, 8]]

    solution_path = iterative_deepening_search(start)

    if solution_path:
        print("\nSolution path:")
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            for row in state:
                print(row)
            print()
