import random

class RandomAI:
    def get_move(self, board):
        available_positions = [i for i in range(len(board)) if board[i] == ' ']
        if available_positions:
            return random.choice(available_positions)
        else:
            return None
