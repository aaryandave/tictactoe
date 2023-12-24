class AlphabetaAI:
    def get_move(self, board):
        best_move, _ = self.alphabeta(board, -float('inf'), float('inf'), 'O')  # 'O' represents AI's move
        return best_move

    def alphabeta(self, board, alpha, beta, player):
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
            score = -self.alphabeta(child_board, -beta, -alpha, 'O' if player == 'X' else 'X')[1]
            if score > best[1]:
                best = (move, score)

            alpha = max(alpha, score)
            if alpha >= beta:
                break
        
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
