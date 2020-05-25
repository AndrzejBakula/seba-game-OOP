import pygame

class Signs:

    SIGN_LIST = ['NapisPoczatkowy', 'BagEmpty', 'Kwota1', 'KoloNapis1', 'JunkieNapis1',
                'SlutNapis1', 'JubyNapis1', 'CyganNapis1', 'SkejtNapis1', 'LaskaNapis1',
                '10zl', '5zl', '20zl', 'TemporaryEnd', 'GrabarzNapis1']
    signDict = {}

    def __init__(self):
        for x in self.SIGN_LIST:
            self.signDict[x] = pygame.image.load('Images/' + x + '.png')