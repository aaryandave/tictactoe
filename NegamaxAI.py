class NegamaxAI:
    def get_move(self, board):
        best_move, _ = self.negamax(board, 'O')  # 'O' represents AI's move
        return best_move

    def negamax(self, board, player):
        if self.is_winner(board, player):
            return None, 1
        elif self.is_winner(board, 'O' if player == 'X' else 'X'):
            return None, -1

        moves = [i for i in range(len(board)) if board[i] == ' ']
        if not moves:
            return None, 0

        best = (None, -float('inf'))
        for move in moves:
            child_board = board[:move] + player + board[move + 1:]
            score = -self.negamax(child_board, 'O' if player == 'X' else 'X')[1]
            if score > best[1]:
                best = (move, score)
        
        return best

    def is_winner(self, board, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for combo in winning_combinations:
            if all(board[cell] == player for cell in combo):
                return True
        return False