from random import choice
from math import inf


def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    for row in board:
        print("| " + " || ".join(row) + " | ")
        print("\n" + "---------------")
    print("===============")


def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return any(
        all(cell == player for cell in condition) for condition in win_conditions
    )


def check_tie(board):
    return all(cell != " " for row in board for cell in row)


def get_available_moves(board):
    return [
        (row, col) for row in range(3) for col in range(3) if board[row][col] == " "
    ]


def get_random_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves) if available_moves else None


def make_move(board, player, move):
    row, col = move
    board[row][col] = player


def play_game():
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "O":
            best_move = None
            best_score = float("-inf")
            for move in get_available_moves(board):
                temp_board = [row[:] for row in board]
                make_move(temp_board, "O", move)
                score = minimax(temp_board, "X")
                if score > best_score:
                    best_score = score
                    best_move = move
            make_move(board, "O", best_move)
        else:
            try:
                row, col = map(
                    int,
                    input(
                        f"Player {current_player}, enter your move (row, col): "
                    ).split(),
                )
                move = (row - 1, col - 1)
                if move not in get_available_moves(board):
                    print(
                        "Invalid move. The cell is already taken or out of bounds. Try again."
                    )
                    continue
                make_move(board, current_player, move)
            except ValueError:
                print(
                    "Invalid move. Please enter row and column as numbers separated by a space."
                )
                continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


def minimax(board, player):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    elif check_tie(board):
        return 0

    scores = []
    for move in get_available_moves(board):
        temp_board = [row[:] for row in board]
        make_move(temp_board, player, move)
        if player == "X":
            score = minimax(temp_board, "O")
        else:
            score = minimax(temp_board, "X")
        scores.append(score)

    return max(scores) if player == "X" else min(scores)


if __name__ == "__main__":
    play_game()
