
class Board:
    FREE_MOVES = ['....', 'BrA1', 'BrA2', 'BrA3', 'toto', 'tvtv', 'qqqq', '@@@@', '@1@1',
                  '@2@2', 'PPPP', 'WWWW', 'M1M1', 'CCCC', 'GaGa', 'CaCa', 'JoJo', 'G1G1',
                  'CRUU', 'dpdp', 'bbbb', 'QQQQ', 'PPPP', '+1+1', '-1-1', 'STA1', 'STAR',
                  'BACK', 'PoPo', 'NAP1', 'NAP2', 'NAP3', 'NAP4', 'NAP5', 'NAP6', 'NAP7',
                  '10zl', '05zl', 'CROW', 'JUNB', 'PIWF', 'PIWE', 'RECY', 'CIGA', 'CIG1',
                  'PuPu', 'crow', 'LABE', 'ZAPA', '20zl', 'piwf', 'ciga', 'MAKU', 'SKOP',
                  'SKBR', 'BUEM', 'BUWA', 'POPP', 'SEKA', 'ZNIC', ',,,,', 'NAP8', 'BOTT',
                  'buem', 'IGPu', 'IGNO', 'igno', 'HERO', 'NAP9', 'BURN', 'EVER', 'CKEY',
                  'buem']

    ITEMS_TO_TAKE = ['@@@@', '@1@1', '@2@2', 'PPPP', 'WWWW', 'GaGa', 'CaCa', 'bbbb', 'CCCC',
                    'JoJo', 'PoPo', 'PIWE', 'CIG1', 'PuPu', 'MAKU', 'SEKA', 'BOTT', 'HERO',
                    'IGPu', 'EVER', 'CKEY']

    level = 0
    board_list = []
    saved_boards_list = []
    new_board = []

    def __init__(self):
        with open("Boards/board.txt") as file_in:
            for line in file_in:
                self.board_list.append(line.split())

    def save_board(self):
        self.saved_boards_list.append("Boards/board" + str(self.level) + "_1.txt")
        with open("Boards/board" + str(self.level) + "_1.txt", "w") as fp:
            fp.writelines('%s\n' % '\t'.join(items) for items in self.board_list)

    def get_new_board(self):
        self.new_board = []
        if "Boards/board" + str(self.level) + "_1.txt" in self.saved_boards_list:
            with open("Boards/board" + str(self.level) + "_1.txt") as file_in:
                for line in file_in:
                    self.new_board.append(line.split())
        else:
            with open("Boards/board" + str(self.level) + ".txt") as file_in:
                for line in file_in:
                    self.new_board.append(line.split())

    def get_prev_board(self):
        self.new_board = []
        with open("Boards/board" + str(self.level) + "_1.txt") as file_in:
            for line in file_in:
                self.new_board.append(line.split())

    def modem_switch(self):
        num_cells_x = len(self.board_list[0])
        num_cells_y = len(self.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.board_list[y][x] == 'MMMM':
                    self.board_list[y][x] = 'M1M1'

    def open_gate(self):
        num_cells_x = len(self.board_list[0])
        num_cells_y = len(self.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.board_list[y][x] == 'G0G0':
                    self.board_list[y][x] = 'G1G1'
