
class Bag:
    bag_dict = {}  # keeps the hero's items.

    def __init__(self, board, hero):
        self.board = board
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