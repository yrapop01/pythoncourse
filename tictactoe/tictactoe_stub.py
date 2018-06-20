from boards.graphic import GraphicBoard as Board
import sys

def main():
    values = ['   ', '   ', '   ']
    board = Board(values, 'O')

    for i, j in board.next_move():
        # TODO: Play
        pass

    board.wait_for_quit('X')
 
if __name__ == "__main__":
    main()
