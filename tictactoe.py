from RandomAI import RandomAI

def print_board(board_string):
    board = [c for c in board_string]
    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()

def initial_board():
    return ' ' * 9

def get_winner(board):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)  # diags
    ]

    for pos in winning_positions:
        if board[pos[0]] != ' ' and board[pos[0]] == board[pos[1]] == board[pos[2]]:
            return board[pos[0]]

    return None

def check_draw(board):
    return ' ' not in board

def make_move(board, player, position):
    if board[position] == ' ':
        board = board[:position] + player + board[position + 1:]
        return board
    else:
        print('invalid move')
        return None

if __name__ == '__main__':
    print('choose ai:')
    print('1. random')

    ai = input()
    if ai == '1':
        ai = RandomAI()
    else:
        print('invalid ai')
        exit()

    board = initial_board()
    print_board(board)

    while True:
        while True:
            try:
                player_position = int(input("move (1-9): ")) - 1
                if 0 <= player_position <= 8:
                    board = make_move(board, 'X', player_position)
                    if board:
                        break
                    else:
                        continue
                else:
                    print("invalid input. number (1-9).")
            except ValueError:
                print("invalid input. number.")

        print_board(board)

        winner = get_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        elif check_draw(board):
            print("draw!")
            break
      
        ai_position = ai.get_move(board)
        board = make_move(board, 'O', ai_position)

        print_board(board)

        winner = get_winner(board)
        if winner:
            print(f"ai wins! {winner}")
            break
        elif check_draw(board):
            print("draw!")
            break
