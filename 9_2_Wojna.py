
class Card(object):
    """ Karty do gry. """
    RANKS = ["2", "3", "4", "5", "6", "7", "8",
             "9", "10", "J", "Q", "K", "A"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit


class Player(object):
    """ Uczestnik gry. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

