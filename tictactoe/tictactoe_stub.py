from boards.graphic import GraphicBoard as Board
import sys

def main():
    player = 'O'
    values = ['   ', '   ', '   ']
    winner = None
    board = Board(values, player)

    for i, j in board.next_move():
        #
        # TODO: change values to make values[i][j] = player
        #
        if False: # change this condition to tell if there is a winner
            winner = player
            break

        #
        # TODO: update player variable to be equal to next move player
        #
        board.change_symbol(player)

    board.wait_for_quit(winner)
 
if __name__ == "__main__":
    main()
