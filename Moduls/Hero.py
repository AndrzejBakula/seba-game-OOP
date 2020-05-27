import pygame
class Hero:

    HERO_LIST = ['Ludzik1', 'Ludzik1B', 'Ludzik1BC', 'LudzikCrowRight', 'LudzikCrowLeft']
    heroDict = {}

    hero_position = (2, 1)
    new_hero_position = ()

    def __init__(self, board):
        self.board = board
        for x in self.HERO_LIST:
            self.heroDict[x] = pygame.image.load('Images/' + x + '.png')

    def get_new_position(self):  # generates new hero position when changing levels forvard.
        global hero_position
        global new_hero_position
        num_cells_x = len(self.board.board_list[0])
        num_cells_y = len(self.board.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.board.board_list[y][x] == 'STAR' or self.board.board_list[y][x] == 'STA1':
                    self.new_hero_position = (x, y)

    def get_back_position(self):  # generates new hero position when changing levels backwards.
        global hero_position
        global new_hero_position
        num_cells_x = len(self.board.board_list[0])
        num_cells_y = len(self.board.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.board.board_list[y][x] == 'BACK':
                    self.new_hero_position = (x, y)