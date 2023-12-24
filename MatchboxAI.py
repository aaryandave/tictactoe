import random

class MatchboxAI:
    def __init__(self, weights_file="matchbox_weights.txt"):
        self.weights = self.load_weights(weights_file)

    def load_weights(self, filename):
        weights = {}
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(':')
                key = parts[0]
                values = parts[1].strip()[1:-1].split('),(')
                weights[key] = {}
                for value in values:
                    if value == '':
                        continue
                    index, weight = value.split(', ')
                    weights[key][int(index)] = int(weight)
        return weights

    def get_move(self, board):
        if board in self.weights:
            weights = self.weights[board]
            weighted_choices = [(k, v) for k, v in weights.items()]
            moves, weights = zip(*weighted_choices)

            # Choose a move randomly based on weights
            return random.choices(moves, weights=weights)[0]
        else:
            return None

if __name__ == '__main__':
    ai = MatchboxAI()
    print(ai.get_move("X        "))