
class Leaderboard(list):

    def __init__(self, board):
        super(Leaderboard, self).__init__(self)
        for b in board:
            self.append(b)


class Leaderboards(dict):
    pass

    def update(self, name, board):
        if name in self.keys:
            self[name].update(board)
        else:
            self[name] = Leaderboard(board)
