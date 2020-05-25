import pygame

class Objects:

    OBJECT_LIST = ['Door1', 'Futryna1', 'Krata1', 'Krata1o', 'ModemOff', 'ModemOn', 'Wyjscie1',
                  'Kibel1', 'Szafa1', 'TV1', 'Crusher', 'Kolo', 'Junkie', 'JunkieBez', 'Slut',
                  'Fatman', 'Boss', 'Bike', 'Recycle', 'Laska', 'LaskaBez', 'Lighter', 'Sklep',
                  'SklepOpen', 'TrashGreen', 'TrashGreenEmpty', 'TrashSilver', 'TrashSilverEmpty',
                  'TrashYellow', 'TrashYellowEmpty', 'SklepBroken', 'Hydrant', 'Poppy', 'Coffin',
                  'Urn', 'Urns', 'ZniczSklep', 'Car', 'Grabarz', 'Agata', 'TrashRed',
                  'TrashRedEmpty', 'Burner', 'Cpun1', 'Cpun2']
    objectDict = {}

    def __init__(self):
        for x in self.OBJECT_LIST:
            self.objectDict[x] = pygame.image.load('Images/' + x + '.png')