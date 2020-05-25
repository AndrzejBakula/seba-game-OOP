import pygame

class Items:

    ITEM_LIST = ['Key1', 'Key2', 'Bag1', 'Phone1m', 'Wallet1small', 'Cigarette1', 'Ganja1', 'Czapa1',
                'Joint', 'Pojara', 'Crowbar', 'PiwoFull', 'PiwoEmpty', 'Fajki', 'Pucha', 'Mak',
                'BucketEmpty', 'BucketWater', 'Sekator', 'Bottle', 'Heroina', 'Strzykawka',
                'StrzykawkaEmpty', 'Niesmiertelnik', 'CarKeys']
    itemDict = {}

    def __init__(self):
        for x in self.ITEM_LIST:
            self.itemDict[x] = pygame.image.load('Images/' + x + '.png')