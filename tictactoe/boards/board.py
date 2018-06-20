from abc import ABC, abstractmethod

class Board(ABC):
    def __init__(self, values, symbol):
        """Init Tic-Tac-Toe Board.
            :param values: board values
            :param symbol: starting symbol ('x' or 'o')"""
        self.values = values
        self.symbol = symbol

    @abstractmethod
    def change_symbol(self, symbol):
        """Change the current symbol.
            :symbol: either 'x' or 'o'"""
        ...

    @abstractmethod
    def next_move(self):
        """Let the user pick the next coord for the current symbol.
            :returns: a coordinate tuple (i, j) where 0 <= i,j < 3"""
        ...

    @abstractmethod
    def wait_for_quit(self, winner):
        """Finish the game and show the winner
            :param winner: winner symbol ('x' or 'o')"""
        ...
