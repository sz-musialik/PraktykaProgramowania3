class TennisGame1:
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

    def _get_equal_score(self):
        """
        Returns the result of a game where the score is tied.

        Args:

        """
        if self.p1points >= 3:
            return "Deuce"

        return f"{self.SCORE_NAMES[self.p1points]}-All"

    def _get_score(self):
        """
        Returns the result of a game that is 1 point away from winning or is already finished.

        Args:

        """
        diff = self.p1points - self.p2points

        if diff > 0:
            leader = self.player1_name
        else:
            leader = self.player2_name

        if diff * diff == 1:
            return f"Advantage {leader}"

        return f"Win for {leader}"

    def score(self):
        """
        Returns the result of a game that is not tied, is not 1 point away from winning and is not finished.

        Args:

        """
        if self.p1points == self.p2points:
            return self._get_equal_score()

        if self.p1points >= 4 or self.p2points >= 4:
            return self._get_score()

        return f"{self.SCORE_NAMES[self.p1points]}-{self.SCORE_NAMES[self.p2points]}"
