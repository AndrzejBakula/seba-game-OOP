
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