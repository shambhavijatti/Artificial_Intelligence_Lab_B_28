# Alpha-Beta Pruning Algorithm Implementation

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, maxDepth):
    """
    Alpha-Beta pruning recursive function.

    depth : current depth of the node
    nodeIndex : index of the node in the values array
    maximizingPlayer : True if current player is MAX, False if MIN
    values : list of leaf node values (game tree terminal states)
    alpha : best value that MAX can guarantee so far
    beta : best value that MIN can guarantee so far
    maxDepth : maximum depth of the game tree
    """
    # Base case: reached leaf node
    if depth == maxDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')

        # Recur for left and right children
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)

            # Beta cut-off
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')

        # Recur for left and right children
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha cut-off
            if beta <= alpha:
                break
        return best


# Driver Code
if __name__ == "__main__":
    # Example leaf node values (game tree terminal values)
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    maxDepth = 3   # Tree depth (log2 of number of leaf nodes)

    print("Leaf node values:", values)

    optimal = alphabeta(0, 0, True, values, float('-inf'), float('inf'), maxDepth)
    print("Optimal value (with Alpha-Beta Pruning):", optimal)

