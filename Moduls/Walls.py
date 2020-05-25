import pygame

class Walls:
    WALL_LIST = ['Cegla1', 'Cegla1GL', 'Cegla1GR', 'Cegla1G', 'Cegla1L', 'Cegla1R', 'Cegla1D',
                'Cegla1DL', 'Cegla1DR', 'Cegla1broke', 'Lawn', 'Graffiti1', 'Graffiti2', 'Graffiti3a',
                'Graffiti3b', 'HWD1', 'HWD2', 'HWD3', 'HWD4', 'WRO1', 'WKS1', 'LOVE', 'GraffitiKot',
                'GraffitiKocham', 'GraffitiPacyfka', 'Tree', 'HedgePrawyDol', 'HedgePrawaGora',
                'HedgePion', 'HedgeLewyDol', 'HedgePoziom', 'HedgeLewaGora', 'HedgeCrossPrawa',
                'HedgeCrossLewa', 'HedgeCrossGora', 'HedgeCrossDol', 'HedgeCross', 'HedgeHeHe',
                'HedgeEndPrawa', 'HedgeEndLewa', 'GraffitiGirl1', 'GraffitiGirl2', 'Graffiti4']
    wallDict = {}

    def __init__(self):
        for x in self.WALL_LIST:
            self.wallDict[x] = pygame.image.load('Images/' + x + '.png')