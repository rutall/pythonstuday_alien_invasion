class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.load_high_score()

    def reset_stats(self):
        self.ships_left = 3
        self.score = 0
        self.level = 1

    def load_high_score(self):
        try:
            with open('high_score.txt') as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
