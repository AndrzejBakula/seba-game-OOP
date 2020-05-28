
class Recycler:

    def __init__(self, board, lowBoard, bag):
        self.board = board
        self.lowBoard = lowBoard
        self.bag = bag

    def exchange_bottle(self):  # exchanges empty bottle to beer in store.
        if 'beerempty' in self.bag.bag_dict and self.bag.bag_dict['beerempty'] > 0:
            num_cells_x = len(self.board.board_list[0])
            num_cells_y = len(self.board.board_list)
            for y in range(num_cells_y):
                for x in range(num_cells_x):
                    if self.board.board_list[y][x] == 'piwf':
                        self.board.board_list[y][x] = 'PIWF'
                        self.bag.add_to_Bag('money', 2)
                        self.bag.remove_from_Bag('beerempty', 1)
                        self.lowBoard.remove_from_inventory('PIWE', 1)

    def exchange_cans(self):  # exchanges 3 cans to crowbar in store.
        if 'can' in self.bag.bag_dict and self.bag.bag_dict['can'] >= 3:
            num_cells_x = len(self.board.board_list[0])
            num_cells_y = len(self.board.board_list)
            for y in range(num_cells_y):
                for x in range(num_cells_x):
                    if self.board.board_list[y][x] == 'crow':
                        self.board.board_list[y][x] = 'CROW'
                        self.bag.remove_from_Bag('can', 3)
                        self.lowBoard.remove_from_inventory('PuPu', 3)
                        self.bag.add_to_Bag('money', 3)

    def exchange_embers(self):  # exchanges 4 embers to cigarrete box in store.
        if 'ember' in self.bag.bag_dict and self.bag.bag_dict['ember'] >= 4:
            num_cells_x = len(self.board.board_list[0])
            num_cells_y = len(self.board.board_list)
            for y in range(num_cells_y):
                for x in range(num_cells_x):
                    if self.board.board_list[y][x] == 'ciga':
                        self.board.board_list[y][x] = 'CIGA'
                        self.bag.remove_from_Bag('ember', 4)
                        self.lowBoard.remove_from_inventory('PoPo', 4)
                        self.bag.add_to_Bag('money', 2)

    def exchange_plastic_bottles(self):  # exchanges 3 plastic bottles to empty bucket in store.
        if 'bottle' in self.bag.bag_dict and self.bag.bag_dict['bottle'] >= 3:
            num_cells_x = len(self.board.board_list[0])
            num_cells_y = len(self.board.board_list)
            for y in range(num_cells_y):
                for x in range(num_cells_x):
                    if self.board.board_list[y][x] == 'buem':
                        self.board.board_list[y][x] = 'BUEM'
                        self.bag.remove_from_Bag('bottle', 3)
                        self.lowBoard.remove_from_inventory('BOTT', 3)
                        self.bag.add_to_Bag('money', 3)

    def exchange_needle(self):  # exchanges empty syringe to new one in store.
        if 'StrzykawkaEmpty' in self.bag.bag_dict and self.bag.bag_dict['StrzykawkaEmpty'] > 0:
            num_cells_x = len(self.board.board_list[0])
            num_cells_y = len(self.board.board_list)
            for y in range(num_cells_y):
                for x in range(num_cells_x):
                    if self.board.board_list[y][x] == 'igno':
                        self.board.board_list[y][x] = 'IGNO'
                        self.bag.add_to_Bag('money', 1)
                        self.bag.remove_from_Bag('StrzykawkaEmpty', 1)
                        self.lowBoard.remove_from_inventory('IGPu', 1)