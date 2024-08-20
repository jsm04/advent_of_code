class Solve:
    def __init__(self, game_line: str):
        self.max_allowed = {"red": 12, "blue": 14, "green": 13}
        self.games_sum = {"red": 0, "blue": 0, "green": 0}
        self.split_id_and_game(game_line)

    def split_id_and_game(self, game_line: str):
        self.game_id, self.game_scores = game_line.split(":")

    def check_values_inside_bounderies(self, key: str):
        if self.games_sum[key] > self.max_allowed[key]:
            return False
        return True

    def process(self):
        for score_cube_set in self.game_scores.split(";"):
            for color in self.games_sum:
                self.games_sum[color] = 0
            score_cube_set = score_cube_set.split(",")
            for current_score in score_cube_set:
                cube_score, cube_color = current_score.split()
                self.games_sum[cube_color] += int(cube_score)
                if not self.check_values_inside_bounderies(cube_color):
                    return -1
        return int(self.game_id.split()[1])
