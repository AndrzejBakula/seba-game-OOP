import pygame
class Hero:

    HERO_LIST = ['Ludzik1', 'Ludzik1B', 'Ludzik1BC', 'LudzikCrowRight', 'LudzikCrowLeft']
    heroDict = {}

    hero_position = (2, 1)

    def __init__(self):
        for x in self.HERO_LIST:
            self.heroDict[x] = pygame.image.load('Images/' + x + '.png')
