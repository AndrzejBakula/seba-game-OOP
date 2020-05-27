
class Screen:

    CELL_SIZE = 50
    screen_width = 0
    screen_height = 0

    def __init__(self, board, lowBoard):
        self.board = board
        self.lowBoard = lowBoard
        self.screen_width = len(board.board_list[0]) * self.CELL_SIZE
        self.screen_height = len(board.board_list) * self.CELL_SIZE + len(lowBoard.lowBoard_list) * self.CELL_SIZE
