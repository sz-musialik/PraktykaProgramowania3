class TennisGame2:
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
        self.increment_player_score(player_name)

    def score(self):
        """
        Returns the result of a game.

        Args:

        """
        if self.p1points == self.p2points:
            if self.p1points < 3:
                return f"{self.SCORE_NAMES[self.p1points]}-All"
            return "Deuce"

        if self.p1points >= 4 or self.p2points >= 4:
            diff = self.p1points - self.p2points
            if diff > 0:
                leader = self.player1_name
            else:
                leader = self.player2_name

            if diff * diff == 1:
                return f"Advantage {leader}"

            return f"Win for {leader}"

        return f"{self.SCORE_NAMES[self.p1points]}-{self.SCORE_NAMES[self.p2points]}"

    def set_player_score(self, number, player_name):
        """
        Sets a players score to the selected value.

        Args:
            nubmer (int): Players score.
            player_name (str): Name of the player whose score should be set.
        """
        for _ in range(number):
            self.increment_player_score(player_name)

    def increment_player_score(self, player_name):
        """
        Increments a players score by one.

        Args:
            player_name (str): Name of the player whose score should be incremented.
        """
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1
