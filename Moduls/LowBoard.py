
class LowBoard:

    lowBoard_list = []

    def __init__(self):
        with open("Boards/lowboard.txt") as file_in:
            for line in file_in:
                self.lowBoard_list.append(line.split())

    def add_to_inventory(self, added_item, q):
        num_cells_y = len(self.lowBoard_list)
        while q > 0:
            for x in range(0, 1):
                for y in range(num_cells_y):
                    if self.lowBoard_list[y][x] == 'bEbE' or self.lowBoard_list[y][x] == '....':
                        self.lowBoard_list[y][x] = added_item
                        q -= 1
                        break
                    elif self.lowBoard_list[y][x + 1] == '....':
                        self.lowBoard_list[y][x + 1] = added_item
                        q -= 1
                        break
                    elif self.lowBoard_list[y][x + 2] == '....':
                        self.lowBoard_list[y][x + 2] = added_item
                        q -= 1
                        break
                    elif self.lowBoard_list[y][x + 3] == '....':
                        self.lowBoard_list[y][x + 3] = added_item
                        q -= 1
                        break

    def remove_from_inventory(self, removed_item, q):
        num_cells_y = len(self.lowBoard_list)
        while q > 0:
            for x in range(0, 1):
                for y in range(num_cells_y):
                    if self.lowBoard_list[y][x + 3] == removed_item:
                        self.lowBoard_list[y][x + 3] = '....'
                        q -= 1
                        break
                    elif self.lowBoard_list[y][x + 2] == removed_item:
                        self.lowBoard_list[y][x + 2] = '....'
                        q -= 1
                        break
                    elif self.lowBoard_list[y][x + 1] == removed_item:
                        self.lowBoard_list[y][x + 1] = '....'
                        q -= 1
                        break
                    elif self.lowBoard_list[y][x] == removed_item:
                        self.lowBoard_list[y][x] = '....'
                        q -= 1
                        break

    def wear_bag(self):
        num_cells_x = len(self.lowBoard_list[0])
        num_cells_y = len(self.lowBoard_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.lowBoard_list[y][x] == 'IIII':
                    self.lowBoard_list[y][x] = 'iiii'

    def instal_phone(self):
        num_cells_x = len(self.lowBoard_list[0])
        num_cells_y = len(self.lowBoard_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.lowBoard_list[y][x] == 'I0I0':
                    self.lowBoard_list[y][x] = 'i0i0'

    def instal_wallet(self):
        num_cells_x = len(self.lowBoard_list[0])
        num_cells_y = len(self.lowBoard_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.lowBoard_list[y][x] == 'I9I9':
                    self.lowBoard_list[y][x] = 'i9i9'

    def remove_opening_credit(self):  # hardcoded - have to change it.
        if self.lowBoard_list[0][0] == 'OCOC':
            self.lowBoard_list[0][0] = '....'

    def draw_lowBoard(self, cell_size, screen, items, signs, board, inv):  # draws inventory board.
        num_cells_x = len(self.lowBoard_list[0])
        num_cells_y = len(self.lowBoard_list)
        ordinate = len(board.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.lowBoard_list[y][x] == 'OCOC':
                    screen.blit(signs.signDict['NapisPoczatkowy'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'CCCC':
                    screen.blit(items.itemDict['Cigarette1'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'PoPo':
                    screen.blit(items.itemDict['Pojara'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'GaGa':
                    screen.blit(items.itemDict['Ganja1'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'JoJo':
                    screen.blit(items.itemDict['Joint'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'PuPu':
                    screen.blit(items.itemDict['Pucha'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'CIGA':
                    screen.blit(items.itemDict['Fajki'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == '@@@@':
                    screen.blit(items.itemDict['Key2'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == '@1@1':
                    screen.blit(items.itemDict['Key1'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == '@2@2':
                    screen.blit(items.itemDict['Key2'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'CROW':
                    screen.blit(items.itemDict['Crowbar'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'CRO1':
                    screen.blit(items.itemDict['Crowbar'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'PIWF':
                    screen.blit(items.itemDict['PiwoFull'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'PIWE':
                    screen.blit(items.itemDict['PiwoEmpty'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'MAKU':
                    screen.blit(items.itemDict['Mak'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'BUEM':
                    screen.blit(items.itemDict['BucketEmpty'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'BUWA':
                    screen.blit(items.itemDict['BucketWater'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'SEKA':
                    screen.blit(items.itemDict['Sekator'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'iiii':
                    screen.blit(inv.invDict['Inventory1'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'i0i0':
                    screen.blit(inv.invDict['Phone1'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'i9i9':
                    screen.blit(inv.invDict['Wallet1'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'iMon':
                    screen.blit(signs.signDict['Kwota1'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'bEbE':
                    screen.blit(signs.signDict['BagEmpty'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'BOTT':
                    screen.blit(items.itemDict['Bottle'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'HERO':
                    screen.blit(items.itemDict['Heroina'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'IGNO':
                    screen.blit(items.itemDict['Strzykawka'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'IGPu':
                    screen.blit(items.itemDict['StrzykawkaEmpty'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'EVER':
                    screen.blit(items.itemDict['Niesmiertelnik'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == 'CKEY':
                    screen.blit(items.itemDict['CarKeys'], (x * cell_size, (ordinate + y) * cell_size))
                elif self.lowBoard_list[y][x] == ('....' or 'IIII'):
                    pass  # empty cell