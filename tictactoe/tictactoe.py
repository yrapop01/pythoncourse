#from boards.graphic import GraphicBoard as Board
from boards.shell import ShellBoard as Board
import sys

def is_a_win(board, symbol):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

def main():
    symbol = 'O'
    winner = None
    values = ['   ' for i in range(3)]
    board = Board(values, symbol)

    for i, j in board.next_move():
        values[i] = values[i][:j] + symbol + values[i][j+1:]
        if is_a_win(values, symbol):
            winner = symbol
            break

        symbol = 'X' if symbol == 'O' else 'O'
        board.change_symbol(symbol)

    board.wait_for_quit(winner)
 
if __name__ == "__main__":
    main()
