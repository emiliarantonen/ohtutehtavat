class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.draw()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.determine_score()

        else:
            score = self.set_result()

        return score
    
    def draw(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        else:
            return "Deuce"
        
    def determine_score(self):

        minus_result = self.player1_score - self. player2_score

        if minus_result == 1:
            return f"Advantage {self.player1_name}"
        elif minus_result == -1:
            return f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"
    
    def set_result(self):
        score = ""
        for i in range(1, 3):
            if i == 1:
                score_helper = self.player1_score
            else:
                score += "-"
                score_helper = self.player2_score

            if score_helper == 0:
                score += "Love"
            elif score_helper == 1:
                score += "Fifteen"
            elif score_helper == 2:
                score += "Thirty"
            elif score_helper == 3:
                score += "Forty"

        return score

