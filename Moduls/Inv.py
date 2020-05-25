import pygame

class Inv:

    INV_LIST = ['Phone1', 'Wallet1', 'Inventory1']
    invDict = {}

    def __init__(self):
        for x in self.INV_LIST:
            self.invDict[x] = pygame.image.load('Images/' + x + '.png')