import pygame

class Inv:

    INV_LIST = ['Phone1', 'Wallet1', 'Inventory1']
    invDict = {}

    pygame.display.set_caption('Gra w pyGame')
    pygame.init()
    font = pygame.font.SysFont('comicsansms', 24)



    def __init__(self, lowBoard, bag):
        self.lowBoard = lowBoard
        self.bag = bag
        for x in self.INV_LIST:
            self.invDict[x] = pygame.image.load('Images/' + x + '.png')

    def roll_joint(self):  # rolls joint.
        if ('cigarrete' in self.bag.bag_dict and self.bag.bag_dict['cigarrete'] >= 1) and (
                'ganja' in self.bag.bag_dict and self.bag.bag_dict['ganja'] >= 1):
            self.bag.remove_from_Bag('cigarrete', 1)
            self.bag.remove_from_Bag('ganja', 1)
            self.lowBoard.remove_from_inventory('CCCC', 1)
            self.lowBoard.remove_from_inventory('GaGa', 1)
            self.bag.add_to_Bag('joint', 1)
            self.lowBoard.add_to_inventory('JoJo', 1)

    def roll_cigarrete(self):  # rolls cigarrete (not in use at the moment).
        if 'ember' in self.bag.bag_dict and self.bag.bag_dict['ember'] >= 2:
            self.bag.remove_from_Bag('ember', 2)
            self.lowBoard.remove_from_inventory('PoPo', 2)
            self.bag.add_to_Bag('cigarrete', 1)
            self.lowBoard.add_to_inventory('CCCC', 1)

    def cook_heroin(self):  # cooks heroine.
        if ('poppy' in self.bag.bag_dict and self.bag.bag_dict['poppy'] >= 1) and (
                'Strzykawka' in self.bag.bag_dict and self.bag.bag_dict['Strzykawka'] >= 1):
            self.bag.remove_from_Bag('Strzykawka', 1)
            self.bag.remove_from_Bag('poppy', 1)
            self.lowBoard.remove_from_inventory('MAKU', 1)
            self.lowBoard.remove_from_inventory('IGNO', 1)
            self.bag.add_to_Bag('heroina', 1)
            self.lowBoard.add_to_inventory('HERO', 1)

    def unpack_cigarettes(self):  # unpacking cigarret box.
        if 'cigarettebox' in self.bag.bag_dict and self.bag.bag_dict['cigarettebox'] > 0:
            self.bag.remove_from_Bag('cigarettebox', 1)
            self.lowBoard.remove_from_inventory('CIGA', 1)
            self.bag.add_to_Bag('ember', 1)
            self.lowBoard.add_to_inventory('PoPo', 1)
            self.bag.add_to_Bag('cigarrete', 2)
            self.lowBoard.add_to_inventory('CCCC', 2)