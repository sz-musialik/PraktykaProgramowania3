class TennisGame3:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """
        Updates the score of a player got won the point.

        Args:
            player_name (str): Name of the player who won the point.

        """
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        """
        Returns the result of a game.

        Args:

        """
        if (self.p1points < 4 and self.p2points < 4) and (
            self.p1points + self.p2points < 6
        ):
            score = self.SCORE_NAMES[self.p1points]

            if self.p1points == self.p2points:
                return score + "-All"
            return score + "-" + self.SCORE_NAMES[self.p2points]

        if self.p1points == self.p2points:
            return "Deuce"

        if self.p1points > self.p2points:
            score = self.player1_name
        else:
            score = self.player2_name

        diff = self.p1points - self.p2points

        if diff * diff == 1:
            return "Advantage " + score

        return "Win for " + score
