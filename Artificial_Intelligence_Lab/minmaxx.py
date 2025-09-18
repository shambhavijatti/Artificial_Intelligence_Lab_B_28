import math

# Function to print board
def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()

# Function to check winner
def check_winner(board):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]] != " ":
            return board[state[0]]
    if " " not in board:
        return "Draw"
    return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X": return 1
    if winner == "O": return -1
    if winner == "Draw": return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth+1, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth+1, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

# Find best move for AI (X)
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and AI is 'X'")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                move = int(input("Enter your move (0-8): "))
                if 0 <= move < 9 and board[move] == " ":
                    board[move] = "O"
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 0 and 8.")

        print_board(board)
        if check_winner(board) is not None:
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = "X"
        print("AI chooses:", ai_move)
        print_board(board)
        if check_winner(board) is not None:
            break

    # Game result
    result = check_winner(board)
    if result == "Draw":
        print("It's a draw!")
    else:
        print(f"{result} wins!")

# Run the game
if __name__ == "__main__":
    play_game()

