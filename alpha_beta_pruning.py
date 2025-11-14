# -------------------------------------------------------
# Minimax with Alpha-Beta Pruning
# -------------------------------------------------------

def alphabeta(node, alpha, beta, maximizingPlayer, tree):
    # If node is a leaf (a number), just return its value
    if isinstance(tree[node], int):
        return tree[node]

    if maximizingPlayer:
        value = float("-inf")
        for child in tree[node]:
            value = max(value, alphabeta(child, alpha, beta, False, tree))
            alpha = max(alpha, value)
            if alpha >= beta:
                print(f"Pruned at node {node} when checking child {child}")
                break
        return value
    else:
        value = float("inf")
        for child in tree[node]:
            value = min(value, alphabeta(child, alpha, beta, True, tree))
            beta = min(beta, value)
            if beta <= alpha:
                print(f"Pruned at node {node} when checking child {child}")
                break
        return value


# -------------------------------------------------------
# Representation of your tree
# -------------------------------------------------------
# Tree structure:
# A (max)
#   B (min), C (min)
# B -> D, E ;  C -> F, G         # min nodes
# D -> H, I ; E -> J, K          # max nodes
# F -> L, M ; G -> N, O
# H -> 10, 11 ; I -> 9, 12 ... etc

tree = {
    "A": ["B", "C"],

    "B": ["D", "E"],
    "C": ["F", "G"],

    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],

    # MIN nodes with leaf children
    "H": ["H1", "H2"],
    "I": ["I1", "I2"],
    "J": ["J1", "J2"],
    "K": ["K1", "K2"],
    "L": ["L1", "L2"],
    "M": ["M1", "M2"],
    "N": ["N1", "N2"],
    "O": ["O1", "O2"],

    # Leaves
    "H1": 10, "H2": 11,
    "I1": 9,  "I2": 12,

    "J1": 14, "J2": 15,
    "K1": 13, "K2": 14,

    "L1": 5,  "L2": 2,
    "M1": 4,  "M2": 1,

    "N1": 3,  "N2": 22,
    "O1": 20, "O2": 21
}


# -------------------------------------------------------
# Run the search
# -------------------------------------------------------
result = alphabeta("A", float("-inf"), float("inf"), True, tree)
print("\nFinal minimax value at root A =", result)
