
class Bag:
    bag_dict = {}  # keeps the hero's items.

    def __init__(self, board, lowBoard, hero):
        self.board = board
        self.lowBoard = lowBoard
        self.hero = hero

    def remove_from_board(self, taken_item):  # removes items from board after hero step on it. Not in use atm.
        num_cells_x = len(self.board.board_list[0])
        num_cells_y = len(self.board.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.board.board_list[y][x] == taken_item and x == self.hero.hero_position[0] and y == self.hero.hero_position[1]:
                    self.board.board_list[y][x] = '....'

    def add_to_Bag(self, added_item, q):  # adds taken item to bag.
        if added_item in self.bag_dict:
            self.bag_dict[added_item] += q
        else:
            self.bag_dict[added_item] = q

    def remove_from_Bag(self, removed_item, q):  # removes item from bag.
        self.bag_dict[removed_item] -= q

    def emptyBag(self, font, screen):  # checks is bag empty or not.
        if sum(self.bag_dict.values()) == 1:
            self.lowBoard.lowBoard_list[0][0] = 'bEbE'
        elif sum(self.bag_dict.values()) == 2 and 'bag' in self.bag_dict and 'phone' in self.bag_dict:
            self.lowBoard.lowBoard_list[0][0] = '....'
        elif sum(
                self.bag_dict.values()) == 3 and 'bag' in self.bag_dict and 'phone' in self.bag_dict and 'wallet' in self.bag_dict:
            self.lowBoard.lowBoard_list[0][0] = '....'
        elif sum(
                self.bag_dict.values()) == 4 and 'bag' in self.bag_dict and 'phone' in self.bag_dict and 'wallet' in self.bag_dict and 'cap' in self.bag_dict:
            self.lowBoard.lowBoard_list[0][0] = '....'
        if 'money' in self.bag_dict:
            screen.blit(font.render((str(self.bag_dict['money']) + 'zł'), True, (255, 255, 255)), (350, 475))