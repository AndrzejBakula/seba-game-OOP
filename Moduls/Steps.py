
class Steps:

    junkie_try = 0
    bike_try = 0
    laska_try = 0

    def __init__(self, board, lowBoard, bag):
        self.board = board
        self.lowBoard = lowBoard
        self.bag = bag

    def open_closet(self, new_pos_x, new_pos_y):
        for y in range(new_pos_y-1, new_pos_y):
            for x in range(new_pos_x-1, new_pos_x+2):
                if self.board.board_list[y][x] == '....':
                    self.board.board_list[y][x] = 'CaCa'
                    break
                elif self.board.board_list[y+1][x] == '....':
                    self.board.board_list[y+1][x] = 'CaCa'
                    break
                elif self.board.board_list[y+2][x] == '....':
                    self.board.board_list[y+2][x] = 'CaCa'
                    break
            for x in range(new_pos_x-1, new_pos_x+2):
                if self.board.board_list[y][x] == '....':
                    self.board.board_list[y][x] = '@2@2'
                    break
                elif self.board.board_list[y+1][x] == '....':
                    self.board.board_list[y+1][x] = '@2@2'
                    break
                elif self.board.board_list[y+2][x] == '....':
                    self.board.board_list[y+2][x] = '@2@2'
                    break

    def buy_cannabis(self, new_pos_x, new_pos_y):
        if 'money' in self.bag.bag_dict and self.bag.bag_dict['money'] >= 35:
            for y in range(new_pos_y - 1, new_pos_y):  # to simplify.
                for x in range(new_pos_x - 1, new_pos_x + 2):
                    if self.board.board_list[y][x] == '....':
                        self.board.board_list[y][x] = 'GaGa'
                        self.bag.remove_from_Bag('money', 35)
                        break
                    elif self.board.board_list[y + 1][x] == '....':
                        self.board.board_list[y + 1][x] = 'GaGa'
                        self.bag.remove_from_Bag('money', 35)
                        break
                    elif self.board.board_list[y + 2][x] == '....':
                        self.board.board_list[y + 2][x] = 'GaGa'
                        self.bag.remove_from_Bag('money', 35)
                        break

    def deal_with_junkie(self, new_pos_x, new_pos_y):
        if 'ganja' in self.bag.bag_dict and self.bag.bag_dict['ganja'] > 0:
            for y in range(new_pos_y - 1, new_pos_y):  # have to simplify.
                for x in range(new_pos_x - 1, new_pos_x + 2):
                    if self.board.board_list[y][x] == '....':
                        self.board.board_list[y][x] = 'PoPo'
                        self.bag.remove_from_Bag('ganja', 1)
                        self.lowBoard.remove_from_inventory('GaGa', 1)
                        self.bag.add_to_Bag('money', 40)
                        self.junkie_try += 1
                        break
                    elif self.board.board_list[y + 1][x] == '....':
                        self.board.board_list[y + 1][x] = 'PoPo'
                        self.bag.remove_from_Bag('ganja', 1)
                        self.lowBoard.remove_from_inventory('GaGa', 1)
                        self.bag.add_to_Bag('money', 40)
                        self.junkie_try += 1
                        break
                    elif self.board.board_list[y + 2][x] == '....':
                        self.board.board_list[y + 2][x] = 'PoPo'
                        self.bag.remove_from_Bag('ganja', 1)
                        self.lowBoard.remove_from_inventory('GaGa', 1)
                        self.bag.add_to_Bag('money', 40)
                        self.junkie_try += 1
                        break
            if self.junkie_try == 3:
                self.board.board_list[new_pos_y][new_pos_x] = 'JUNB'
                self.board.board_list[6][4] = '....'  # this is hardcoded - I have to change it.
        if 'heroina' in self.bag.bag_dict and self.bag.bag_dict['heroina'] > 0:
            for y in range(new_pos_y - 1, new_pos_y):  # have to simplify this.
                for x in range(new_pos_x - 1, new_pos_x + 2):
                    if self.board.board_list[y][x] == '....':
                        self.board.board_list[y][x] = 'IGPu'
                        self.bag.remove_from_Bag('heroina', 1)
                        self.lowBoard.remove_from_inventory('HERO', 1)
                        self.bag.add_to_Bag('money', 50)
                        break
                    elif self.board.board_list[y + 1][x] == '....':
                        self.board.board_list[y + 1][x] = 'IGPu'
                        self.bag.remove_from_Bag('heroina', 1)
                        self.lowBoard.remove_from_inventory('HERO', 1)
                        self.bag.add_to_Bag('money', 50)
                        break
                    elif self.board.board_list[y + 2][x] == '....':
                        self.board.board_list[y + 2][x] = 'IGPu'
                        self.bag.remove_from_Bag('heroina', 1)
                        self.lowBoard.remove_from_inventory('HERO', 1)
                        self.bag.add_to_Bag('money', 50)
                        break
            self.board.board_list[new_pos_y][new_pos_x] = 'EVER'
            # board.board_list[4][2] = '....' #this is hardcoded - I have to change it.

    def cigarrete_for_fatman(self, new_pos_x, new_pos_y):
        if 'cigarrete' in self.bag.bag_dict and self.bag.bag_dict['cigarrete'] > 0:
            for y in range(new_pos_y-1, new_pos_y): #have to simplify this.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if self.board.board_list[y][x] == '....':
                        self.board.board_list[y][x] = 'PoPo'
                        self.bag.remove_from_Bag('cigarrete', 1)
                        self.lowBoard.remove_from_inventory('CCCC', 1)
                        break
                    elif self.board.board_list[y+1][x] == '....':
                        self.board.board_list[y+1][x] = 'PoPo'
                        self.bag.remove_from_Bag('cigarrete', 1)
                        self.lowBoard.remove_from_inventory('CCCC', 1)
                        break
                    elif self.board.board_list[y+2][x] == '....':
                        self.board.board_list[y+2][x] = 'PoPo'
                        self.bag.remove_from_Bag('cigarrete', 1)
                        self.lowBoard.remove_from_inventory('CCCC', 1)
                        break
            self.board.board_list[new_pos_y][new_pos_x] = '....'

    def deal_with_slut(self, new_pos_x, new_pos_y):
        if 'joint' in self.bag.bag_dict and self.bag.bag_dict['joint'] > 0:
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if self.board.board_list[y][x] == '....':
                        self.board.board_list[y][x] = 'PoPo'
                        self.bag.remove_from_Bag('joint', 1)
                        self.lowBoard.remove_from_inventory('JoJo', 1)
                        self.bag.add_to_Bag('money', 50)
                        break
                    elif self.board.board_list[y+1][x] == '....':
                        self.board.board_list[y+1][x] = 'PoPo'
                        self.bag.remove_from_Bag('joint', 1)
                        self.lowBoard.remove_from_inventory('JoJo', 1)
                        self.bag.add_to_Bag('money', 50)
                        break
                    elif self.board.board_list[y+2][x] == '....':
                        self.board.board_list[y+2][x] = 'PoPo'
                        self.bag.remove_from_Bag('joint', 1)
                        self.lowBoard.remove_from_inventory('JoJo', 1)
                        self.bag.add_to_Bag('money', 50)
                        break
        elif 'ganja' in self.bag.bag_dict and self.bag.bag_dict['ganja'] > 0:
            self.bag.remove_from_Bag('ganja', 1)
            self.lowBoard.remove_from_inventory('GaGa', 1)
            self.bag.add_to_Bag('money', 35)

    def beer_for_biker(self, new_pos_x, new_pos_y):
        if 'beerfull' in self.bag.bag_dict and self.bag.bag_dict['beerfull'] > 0 and self.bike_try <= 9:
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if self.board.board_list[y][x] == '....':
                        self.board.board_list[y][x] = 'PIWE'
                        self.bag.remove_from_Bag('beerfull', 1)
                        self.lowBoard.remove_from_inventory('PIWF', 1)
                        self.bag.add_to_Bag('money', 10)
                        self.bike_try += 1
                        break
                    elif self.board.board_list[y+1][x] == '....':
                        self.board.board_list[y][x] = 'PIWE'
                        self.bag.remove_from_Bag('beerfull', 1)
                        self.lowBoard.remove_from_inventory('PIWF', 1)
                        self.bag.add_to_Bag('money', 10)
                        self.bike_try += 1
                        break
                    elif self.board.board_list[y+2][x] == '....':
                        self.board.board_list[y][x] = 'PIWE'
                        self.bag.remove_from_Bag('beerfull', 1)
                        self.lowBoard.remove_from_inventory('PIWF', 1)
                        self.bag.add_to_Bag('money', 10)
                        self.bike_try += 1
                        break

    def deel_with_laska(self, new_pos_x, new_pos_y):
        if 'cigarettebox' in self.bag.bag_dict and self.bag.bag_dict['cigarettebox'] > 0:
            self.bag.remove_from_Bag('cigarettebox', 1)
            self.lowBoard.remove_from_inventory('CIGA', 1)
            self.bag.add_to_Bag('money', 15)
            self.board.board_list[new_pos_y][new_pos_x] = 'LABE'
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if self.board.board_list[y][x] == '....':
                        self.board.board_list[y][x] = 'CCCC'
                        break
                    elif self.board.board_list[y+1][x] == '....':
                        self.board.board_list[y+1][x] = 'CCCC'
                        break
                    elif self.board.board_list[y+2][x] == '....':
                        self.board.board_list[y+2][x] = 'CCCC'
                        break
                for x in range(new_pos_x-1, new_pos_x+2):
                    if self.board.board_list[y][x] == '....':
                        self.board.board_list[y][x] = 'CCCC'
                        break
                    elif self.board.board_list[y+1][x] == '....':
                        self.board.board_list[y+1][x] = 'CCCC'
                        break
                    elif self.board.board_list[y+2][x] == '....':
                        self.board.board_list[y+2][x] = 'CCCC'
                        break
                for x in range(new_pos_x-1, new_pos_x+2):
                    if self.board.board_list[y][x] == '....':
                        self.board.board_list[y][x] = 'PoPo'
                        break
                    elif self.board.board_list[y+1][x] == '....':
                        self.board.board_list[y+1][x] = 'PoPo'
                        break
                    elif self.board.board_list[y+2][x] == '....':
                        self.board.board_list[y+2][x] = 'PoPo'
                        break
        elif 'ganja' in self.bag.bag_dict and self.bag.bag_dict['ganja'] > 0 and self.laska_try < 2: #she also can buy 2 pieces of ganja.
            self.bag.remove_from_Bag('ganja', 1)
            self.lowBoard.remove_from_inventory('GaGa', 1)
            self.bag.add_to_Bag('money', 40)
            self.laska_try += 1