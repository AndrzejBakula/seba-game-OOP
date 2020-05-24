import pygame
from Boards.Board import Board
from Boards.LowBoard import LowBoard

#BOARDS:

board = Board()
lowBoard = LowBoard()

saved_boards = board.saved_boards_list


#GLOBAL VARIABLES:
Bag = {}

hero_position = (2, 1)

def get_new_position():
    global hero_position
    global new_hero_position
    num_cells_x = len(board.board_list[0])
    num_cells_y = len(board.board_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if board.board_list[y][x] == 'STAR' or board.board_list[y][x] == 'STA1':
                new_hero_position = (x, y) 
                            
def get_back_position():
    global hero_position
    global new_hero_position
    num_cells_x = len(board.board_list[0])
    num_cells_y = len(board.board_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if board.board_list[y][x] == 'BACK':
                new_hero_position = (x, y) 

cell_size = 50
screen_width = len(board.board_list[0]) * cell_size
screen_height = len(board.board_list) * cell_size + len(lowBoard.lowBoard_list) * cell_size

#GRAPHIC ELEMENTS:
#Walls:
wallList = ['Cegla1', 'Cegla1GL', 'Cegla1GR', 'Cegla1G', 'Cegla1L', 'Cegla1R', 'Cegla1D',
             'Cegla1DL', 'Cegla1DR', 'Cegla1broke', 'Lawn', 'Graffiti1', 'Graffiti2', 'Graffiti3a',
            'Graffiti3b', 'HWD1', 'HWD2', 'HWD3', 'HWD4', 'WRO1', 'WKS1', 'LOVE', 'GraffitiKot',
            'GraffitiKocham', 'GraffitiPacyfka', 'Tree', 'HedgePrawyDol', 'HedgePrawaGora',
            'HedgePion', 'HedgeLewyDol', 'HedgePoziom', 'HedgeLewaGora', 'HedgeCrossPrawa',
            'HedgeCrossLewa', 'HedgeCrossGora', 'HedgeCrossDol', 'HedgeCross', 'HedgeHeHe',
            'HedgeEndPrawa', 'HedgeEndLewa', 'GraffitiGirl1', 'GraffitiGirl2', 'Graffiti4']
wallDict = {}
for x in wallList:
    wallDict[x] = pygame.image.load('Images/'+x+'.png')

#Hero:
heroList = ['Ludzik1', 'Ludzik1B', 'Ludzik1BC', 'LudzikCrowRight', 'LudzikCrowLeft',
            ]
heroDict = {}
for x in heroList:
    heroDict[x] = pygame.image.load('Images/'+x+'.png')

#Items:
itemList = ['Key1', 'Key2', 'Bag1', 'Phone1m', 'Wallet1small', 'Cigarette1', 'Ganja1', 'Czapa1',
            'Joint', 'Pojara', 'Crowbar', 'PiwoFull', 'PiwoEmpty', 'Fajki', 'Pucha', 'Mak',
            'BucketEmpty', 'BucketWater', 'Sekator', 'Bottle', 'Heroina', 'Strzykawka',
            'StrzykawkaEmpty', 'Niesmiertelnik', 'CarKeys']
itemDict = {}
for x in itemList:
    itemDict[x] = pygame.image.load('Images/'+x+'.png')

#Objects:
objectList = ['Door1', 'Futryna1', 'Krata1', 'Krata1o', 'ModemOff', 'ModemOn', 'Wyjscie1',
              'Kibel1', 'Szafa1', 'TV1', 'Crusher', 'Kolo', 'Junkie', 'JunkieBez', 'Slut',
              'Fatman', 'Boss', 'Bike', 'Recycle', 'Laska', 'LaskaBez', 'Lighter', 'Sklep',
              'SklepOpen', 'TrashGreen', 'TrashGreenEmpty', 'TrashSilver', 'TrashSilverEmpty',
              'TrashYellow', 'TrashYellowEmpty', 'SklepBroken', 'Hydrant', 'Poppy', 'Coffin',
              'Urn', 'Urns', 'ZniczSklep', 'Car', 'Grabarz', 'Agata', 'TrashRed',
              'TrashRedEmpty', 'Burner', 'Cpun1', 'Cpun2']
objectDict = {}
for x in objectList:
    objectDict[x] = pygame.image.load('Images/'+x+'.png')

#Inventory:
invList = ['Phone1', 'Wallet1', 'Inventory1']
invDict = {}
for x in invList:
    invDict[x] = pygame.image.load('Images/'+x+'.png')

#Signs:
signList = ['NapisPoczatkowy', 'BagEmpty', 'Kwota1', 'KoloNapis1', 'JunkieNapis1',
            'SlutNapis1', 'JubyNapis1', 'CyganNapis1', 'SkejtNapis1', 'LaskaNapis1',
            '10zl', '5zl', '20zl', 'TemporaryEnd', 'GrabarzNapis1']
signDict = {}
for x in signList:
    signDict[x] = pygame.image.load('Images/'+x+'.png')

#Drawing functions:
empty_cells = ['....', 'STAR', 'STA1', 'BACK', '-1-1', '+1+1', 'BrA1', 'BrA2',
               'crow', 'piwf']
def draw_board(cell_size):
    num_cells_x = len(board.board_list[0])
    num_cells_y = len(board.board_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if board.board_list[y][x] == '####':
                screen.blit(wallDict['Cegla1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GLGL':
                screen.blit(wallDict['Cegla1GL'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRGR':
                screen.blit(wallDict['Cegla1GR'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GGGG':
                screen.blit(wallDict['Cegla1G'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'LLLL':
                screen.blit(wallDict['Cegla1L'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'RRRR':
                screen.blit(wallDict['Cegla1R'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'DDDD':
                screen.blit(wallDict['Cegla1D'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'DLDL':
                screen.blit(wallDict['Cegla1DL'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'DRDR':
                screen.blit(wallDict['Cegla1DR'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BrBr':
                screen.blit(wallDict['Cegla1broke'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRF1':
                screen.blit(wallDict['Graffiti1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRF2':
                screen.blit(wallDict['Graffiti2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GF3A':
                screen.blit(wallDict['Graffiti3a'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GF3B':
                screen.blit(wallDict['Graffiti3b'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRF4':
                screen.blit(wallDict['Graffiti4'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HWD1':
                screen.blit(wallDict['HWD1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HWD2':
                screen.blit(wallDict['HWD2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HWD3':
                screen.blit(wallDict['HWD3'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HWD4':
                screen.blit(wallDict['HWD4'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'WRO1':
                screen.blit(wallDict['WRO1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'WKS1':
                screen.blit(wallDict['WKS1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'LOVE':
                screen.blit(wallDict['LOVE'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'KOT1':
                screen.blit(wallDict['GraffitiKot'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'KOCH':
                screen.blit(wallDict['GraffitiKocham'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PACY':
                screen.blit(wallDict['GraffitiPacyfka'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRG1':
                screen.blit(wallDict['GraffitiGirl1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRG2':
                screen.blit(wallDict['GraffitiGirl2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == ',,,,':
                screen.blit(wallDict['Lawn'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TREE':
                screen.blit(wallDict['Tree'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEPI':
                screen.blit(wallDict['HedgePion'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEPO':
                screen.blit(wallDict['HedgePoziom'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEPD':
                screen.blit(wallDict['HedgePrawyDol'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEPG':
                screen.blit(wallDict['HedgePrawaGora'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HELG':
                screen.blit(wallDict['HedgeLewaGora'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HELD':
                screen.blit(wallDict['HedgeLewyDol'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXX':
                screen.blit(wallDict['HedgeCross'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXD':
                screen.blit(wallDict['HedgeCrossDol'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXG':
                screen.blit(wallDict['HedgeCrossGora'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXL':
                screen.blit(wallDict['HedgeCrossLewa'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXP':
                screen.blit(wallDict['HedgeCrossPrawa'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEHE':
                screen.blit(wallDict['HedgeHeHe'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEEL':
                screen.blit(wallDict['HedgeEndLewa'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEEP':
                screen.blit(wallDict['HedgeEndPrawa'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'bbbb':
                screen.blit(itemDict['Bag1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '$$$$':
                screen.blit(objectDict['Door1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '$1$1':
                screen.blit(objectDict['Door1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '$2$2':
                screen.blit(objectDict['Door1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'dpdp':
                screen.blit(objectDict['Futryna1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'G0G0':
                screen.blit(objectDict['Krata1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'G1G1':
                screen.blit(objectDict['Krata1o'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'MMMM':
                screen.blit(objectDict['ModemOff'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'M1M1':
                screen.blit(objectDict['ModemOn'], (x*cell_size,y*cell_size))    
            elif board.board_list[y][x] == 'PPPP':
                screen.blit(itemDict['Phone1m'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'WWWW':
                screen.blit(itemDict['Wallet1small'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CCCC':
                screen.blit(itemDict['Cigarette1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PoPo':
                screen.blit(itemDict['Pojara'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GaGa':
                screen.blit(itemDict['Ganja1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'JoJo':
                screen.blit(itemDict['Joint'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PIWF':
                screen.blit(itemDict['PiwoFull'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PIWE':
                screen.blit(itemDict['PiwoEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CIGA':
                screen.blit(itemDict['Fajki'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CIG1':
                screen.blit(itemDict['Fajki'], (x*cell_size,y*cell_size))    
            elif board.board_list[y][x] == 'PuPu':
                screen.blit(itemDict['Pucha'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'MAKU':
                screen.blit(itemDict['Mak'], (x*cell_size,y*cell_size))    
            elif board.board_list[y][x] == 'QQQQ' or board.board_list[y][x] == 'STA1':
                screen.blit(objectDict['Wyjscie1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '@@@@':
                screen.blit(itemDict['Key2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '@1@1':
                screen.blit(itemDict['Key1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '@2@2':
                screen.blit(itemDict['Key2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CaCa':
                screen.blit(itemDict['Czapa1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'toto':
                screen.blit(objectDict['Kibel1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'ClCl':
                screen.blit(objectDict['Szafa1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'tvtv':
                screen.blit(objectDict['TV1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CRUU':
                screen.blit(objectDict['Crusher'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'ZAPA':
                screen.blit(objectDict['Lighter'], (x*cell_size,y*cell_size))    
            elif board.board_list[y][x] == 'CROW':
                screen.blit(itemDict['Crowbar'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CRO1':
                screen.blit(itemDict['Crowbar'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'RECY':
                screen.blit(objectDict['Recycle'], (x*cell_size,y*cell_size))    
            elif board.board_list[y][x] == 'KOLO':
                screen.blit(objectDict['Kolo'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'JUNK':
                screen.blit(objectDict['Junkie'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'JUNB':
                screen.blit(objectDict['JunkieBez'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SLUT':
                screen.blit(objectDict['Slut'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'FATM':
                screen.blit(objectDict['Fatman'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CYGA':
                screen.blit(objectDict['Boss'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BIKE':
                screen.blit(objectDict['Bike'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'LASK':
                screen.blit(objectDict['Laska'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'LABE':
                screen.blit(objectDict['LaskaBez'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP1':
                screen.blit(signDict['KoloNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP2':
                screen.blit(signDict['JunkieNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP3':
                screen.blit(signDict['SlutNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP4':
                screen.blit(signDict['JubyNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP5':
                screen.blit(signDict['CyganNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP6':
                screen.blit(signDict['SkejtNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP7':
                screen.blit(signDict['LaskaNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP8':
                screen.blit(signDict['GrabarzNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '10zl':
                screen.blit(signDict['10zl'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '05zl':
                screen.blit(signDict['5zl'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '20zl':
                screen.blit(signDict['20zl'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SKLE':
                screen.blit(objectDict['Sklep'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SKOP':
                screen.blit(objectDict['SklepOpen'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SKBR':
                screen.blit(objectDict['SklepBroken'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRGF':
                screen.blit(objectDict['TrashGreen'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRGE':
                screen.blit(objectDict['TrashGreenEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRSF':
                screen.blit(objectDict['TrashSilver'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRSE':
                screen.blit(objectDict['TrashSilverEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRYF':
                screen.blit(objectDict['TrashYellow'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRYE':
                screen.blit(objectDict['TrashYellowEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRRE':
                screen.blit(objectDict['TrashRedEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRRF':
                screen.blit(objectDict['TrashRed'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BUEM':
                screen.blit(itemDict['BucketEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HYDR':
                screen.blit(objectDict['Hydrant'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'POPP':
                screen.blit(objectDict['Poppy'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'COFF':
                screen.blit(objectDict['Coffin'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'URNN':
                screen.blit(objectDict['Urn'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'URNS':
                screen.blit(objectDict['Urns'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SEKA':
                screen.blit(itemDict['Sekator'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'ZNIC':
                screen.blit(objectDict['ZniczSklep'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CAR1':
                screen.blit(objectDict['Car'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRAB':
                screen.blit(objectDict['Grabarz'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'AGAT':
                screen.blit(objectDict['Agata'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BOTT':
                screen.blit(itemDict['Bottle'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HERO':
                screen.blit(itemDict['Heroina'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'IGNO':
                screen.blit(itemDict['Strzykawka'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'IGPu':
                screen.blit(itemDict['StrzykawkaEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BURN':
                screen.blit(objectDict['Burner'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'EVER':
                screen.blit(itemDict['Niesmiertelnik'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CPU1':
                screen.blit(objectDict['Cpun1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CPU2':
                screen.blit(objectDict['Cpun2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CKEY':
                screen.blit(itemDict['CarKeys'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'END1':
                screen.blit(signDict['TemporaryEnd'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] in empty_cells:
                pass
            if x == hero_position[0] and y == hero_position[1]:
                if board.board_list[y][x] == '@@@@' and board.board_list[y][x+1] == 'BrBr':
                    screen.blit(heroDict['LudzikCrowRight'], (x*cell_size,y*cell_size))
                elif board.board_list[y][x] == '@@@@' and board.board_list[y][x-1] == 'BrBr':
                    screen.blit(heroDict['LudzikCrowLeft'], (x*cell_size,y*cell_size))
                elif board.level == 0 and 'bag' not in Bag:
                    screen.blit(heroDict['Ludzik1'], (x*cell_size,y*cell_size))
                else:
                    if 'cap' not in Bag:
                        screen.blit(heroDict['Ludzik1B'], (x*cell_size,y*cell_size))
                    else:
                        screen.blit(heroDict['Ludzik1BC'], (x*cell_size,y*cell_size))

def draw_lowBoard(cell_size):
    num_cells_x = len(lowBoard.lowBoard_list[0])
    num_cells_y = len(lowBoard.lowBoard_list)
    ordinate = len(board.board_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if lowBoard.lowBoard_list[y][x] == 'OCOC':
                screen.blit(signDict['NapisPoczatkowy'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CCCC':
                screen.blit(itemDict['Cigarette1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'PoPo':
                screen.blit(itemDict['Pojara'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'GaGa':
                screen.blit(itemDict['Ganja1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'JoJo':
                screen.blit(itemDict['Joint'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'PuPu':
                screen.blit(itemDict['Pucha'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CIGA':
                screen.blit(itemDict['Fajki'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == '@@@@':
                screen.blit(itemDict['Key2'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == '@1@1':
                screen.blit(itemDict['Key1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == '@2@2':
                screen.blit(itemDict['Key2'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CROW':
                screen.blit(itemDict['Crowbar'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CRO1':
                screen.blit(itemDict['Crowbar'], (x*cell_size,(ordinate+y)*cell_size))    
            elif lowBoard.lowBoard_list[y][x] == 'PIWF':
                screen.blit(itemDict['PiwoFull'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'PIWE':
                screen.blit(itemDict['PiwoEmpty'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'MAKU':
                screen.blit(itemDict['Mak'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'BUEM':
                screen.blit(itemDict['BucketEmpty'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'BUWA':
                screen.blit(itemDict['BucketWater'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'SEKA':
                screen.blit(itemDict['Sekator'], (x*cell_size,(ordinate+y)*cell_size))    
            elif lowBoard.lowBoard_list[y][x] == 'iiii':
                screen.blit(invDict['Inventory1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'i0i0':
                screen.blit(invDict['Phone1'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'i9i9':
                screen.blit(invDict['Wallet1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'iMon':
                screen.blit(signDict['Kwota1'], (x*cell_size,(ordinate+y)*cell_size))    
            elif lowBoard.lowBoard_list[y][x] == 'bEbE':
                screen.blit(signDict['BagEmpty'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'BOTT':
                screen.blit(itemDict['Bottle'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'HERO':
                screen.blit(itemDict['Heroina'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'IGNO':
                screen.blit(itemDict['Strzykawka'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'IGPu':
                screen.blit(itemDict['StrzykawkaEmpty'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'EVER':
                screen.blit(itemDict['Niesmiertelnik'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CKEY':
                screen.blit(itemDict['CarKeys'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == ('....' or 'IIII'):
                pass # empty cell

#Move/action functions:
free_moves = ['....', 'BrA1', 'BrA2', 'BrA3', 'toto', 'tvtv', 'qqqq', '@@@@', '@1@1',
              '@2@2', 'PPPP', 'WWWW', 'M1M1', 'CCCC', 'GaGa', 'CaCa', 'JoJo', 'G1G1',
              'CRUU', 'dpdp', 'bbbb', 'QQQQ', 'PPPP', '+1+1', '-1-1', 'STA1', 'STAR',
              'BACK', 'PoPo', 'NAP1', 'NAP2', 'NAP3', 'NAP4', 'NAP5', 'NAP6', 'NAP7',
              '10zl', '05zl', 'CROW', 'JUNB', 'PIWF', 'PIWE', 'RECY', 'CIGA', 'CIG1',
              'PuPu', 'crow', 'LABE', 'ZAPA', '20zl', 'piwf', 'ciga', 'MAKU', 'SKOP',
              'SKBR', 'BUEM', 'BUWA', 'POPP', 'SEKA', 'ZNIC', ',,,,', 'NAP8', 'BOTT',
              'buem', 'IGPu', 'IGNO', 'igno', 'HERO', 'NAP9', 'BURN', 'EVER', 'CKEY',
              'buem']

item_to_take = ['@@@@', '@1@1', '@2@2', 'PPPP', 'WWWW', 'GaGa', 'CaCa', 'bbbb', 'CCCC',
                'JoJo', 'PoPo', 'PIWE', 'CIG1', 'PuPu', 'MAKU', 'SEKA', 'BOTT', 'HERO',
                'IGPu', 'EVER', 'CKEY']
junkie_try = 0
bike_try = 0
laska_try = 0

def try_move(stepX, stepY):
    global board
    global new_board
    global hero_position
    global level
    global junkie_try
    global bike_try
    global laska_try
    new_pos_x = hero_position[0]+stepX
    new_pos_y = hero_position[1]+stepY
    last_pos_x = hero_position[0]
    last_pos_y = hero_position[1]
    bnp = board.board_list[new_pos_y][new_pos_x]
    blp = board.board_list[last_pos_y][last_pos_x]
    remove_opening_credit()
    
    if (bnp in free_moves):
        hero_position = (new_pos_x, new_pos_y)
    if (bnp in item_to_take):
        board.board_list[new_pos_y][new_pos_x] = '....'
    if bnp == '@@@@':
        add_to_Bag('key2', 1)
        add_to_inventory('@@@@', 1)
    if bnp == '@1@1':
        add_to_Bag('key', 1)
        add_to_inventory('@1@1', 1)
    if bnp == '@2@2':
        add_to_Bag('key3', 1)
        add_to_inventory('@2@2', 1)
    if bnp == 'PPPP':
        add_to_Bag('phone', 1)
        modem_switch()
        instal_phone()
    if bnp == 'WWWW':
        add_to_Bag('wallet', 1)
        add_to_Bag('money', 50)
        instal_wallet()
        #lowBoard.lowBoard_list[2][4] = 'i9i9' #have to change.
    if bnp == 'M1M1':
        open_gate()
    if bnp == 'ClCl' and 'key' in Bag and Bag['key'] == 1: #have to simplify.
        hero_position = (new_pos_x, new_pos_y)
        for y in range(new_pos_y-1, new_pos_y):
            for x in range(new_pos_x-1, new_pos_x+2):
                if board.board_list[y][x] == '....':
                    board.board_list[y][x] = 'CaCa'
                    break
                elif board.board_list[y+1][x] == '....':
                    board.board_list[y+1][x] = 'CaCa'
                    break
                elif board.board_list[y+2][x] == '....':
                    board.board_list[y+2][x] = 'CaCa'
                    break
            for x in range(new_pos_x-1, new_pos_x+2):
                if board.board_list[y][x] == '....':
                    board.board_list[y][x] = '@2@2'
                    break
                elif board.board_list[y+1][x] == '....':
                    board.board_list[y+1][x] = '@2@2'
                    break
                elif board.board_list[y+2][x] == '....':
                    board.board_list[y+2][x] = '@2@2'
                    break
        remove_from_Bag('key', 1)
        remove_from_inventory('@1@1', 1)
    if bnp == 'BrBr' and blp == 'BrA1':
        pass
        if ('cigarrete' not in Bag or ('cigarrete' in Bag and Bag['cigarrete'] == 0)) and board.board_list[new_pos_y][new_pos_x-1] == '....':
            board.board_list[new_pos_y][new_pos_x-1] = 'CCCC'
    if bnp == 'BrBr' and blp == 'BrA2':
        pass
        if ('ganja' not in Bag or ('ganja' in Bag and Bag['ganja'] == 0)) and board.board_list[new_pos_y][new_pos_x-1] == '....':
            board.board_list[new_pos_y][new_pos_x-1] = 'GaGa'
    if bnp == 'BrBr' and blp == 'BrA3':
        pass
        if 'CRO1' in Bag and Bag['CRO1'] > 0:
            board.board_list[last_pos_y][last_pos_x] = '@@@@'
            remove_from_Bag('CRO1', 1)
            remove_from_inventory('CRO1', 1)
    if bnp == 'CCCC':
        add_to_Bag('cigarrete', 1)
        add_to_inventory('CCCC', 1)
    if bnp == 'PoPo':
        add_to_Bag('ember', 1)
        add_to_inventory('PoPo', 1)
    if bnp == 'GaGa':
        add_to_Bag('ganja', 1)
        add_to_inventory('GaGa', 1)
    if bnp == 'JoJo':
        add_to_Bag('joint', 1)
        add_to_inventory('JoJo', 1)
    if bnp == 'PIWF':
        if Bag['money'] >= 5:
            add_to_Bag('beerfull', 1)
            add_to_inventory('PIWF', 1)
            remove_from_Bag('money', 5)
            board.board_list[new_pos_y][new_pos_x] = 'piwf'
    if bnp == 'PIWE':
        add_to_Bag('beerempty', 1)
        add_to_inventory('PIWE', 1)
    if bnp == 'CIGA':
        hero_position = (new_pos_x, new_pos_y)
        if Bag['money'] >= 10:
            add_to_Bag('cigarettebox', 1)
            add_to_inventory('CIGA', 1)
            remove_from_Bag('money', 10)
            board.board_list[new_pos_y][new_pos_x] = 'ciga'
    if bnp == 'CIG1':
        hero_position = (new_pos_x, new_pos_y)
        add_to_Bag('cigarettebox', 1)
        add_to_inventory('CIGA', 1)
    if bnp == 'PuPu':
        add_to_Bag('can', 1)
        add_to_inventory('PuPu', 1)
    if bnp == 'MAKU':
        add_to_Bag('poppy', 1)
        add_to_inventory('MAKU', 1) 
    if bnp == 'CaCa':
        add_to_Bag('cap', 1)    
    if bnp == '$$$$':
        if 'key3' in Bag and Bag['key3'] > 0:
            hero_position = (new_pos_x, new_pos_y)
            board.board_list[new_pos_y][new_pos_x] = 'dpdp'
            remove_from_Bag('key3', 1)
            remove_from_inventory('@2@2', 1)
        else:
            pass # cannot move - closed
    if bnp == 'SKLE':
        if 'CROW' in Bag and Bag['CROW'] > 0:
            hero_position = (new_pos_x, new_pos_y)
            board.board_list[new_pos_y][new_pos_x] = 'SKBR'
            remove_from_Bag('CROW', 1)
            remove_from_inventory('CROW', 1)
        else:
            pass # cannot move - closed
        
    if bnp == '$1$1':
        if 'key2' in Bag and Bag['key2'] == 1:
            hero_position = (new_pos_x, new_pos_y)
            board.board_list[new_pos_y][new_pos_x] = 'dpdp'
            remove_from_Bag('key2', 1)
            remove_from_inventory('@@@@', 1)
        else:
            pass # cannot move - closed
    if bnp == 'bbbb':
        add_to_Bag('bag', 1)
        wear_bag()
    if bnp == 'QQQQ':
        board.level += 1
        board.get_new_board()
        board.board_list = board.new_board
        get_new_position()
        hero_position = new_hero_position
    if bnp == 'QQQ1':
        board.level = 5
        board.get_new_board()
        board.board_list = board.new_board
        get_new_position()
        hero_position = new_hero_position
    if bnp == 'QQQ2':
        if 'Strzykawka' in Bag and Bag['Strzykawka'] == 1:
            remove_from_Bag('Strzykawka', 1)
            remove_from_inventory('IGNO', 1)
        if 'StrzykawkaEmpty' in Bag and Bag['StrzykawkaEmpty'] == 1:
            remove_from_Bag('StrzykawkaEmpty', 1)
            remove_from_inventory('IGPu', 1)
        if 'poppy' in Bag and Bag['poppy'] == 1:
            remove_from_Bag('poppy', 1)
            remove_from_inventory('MAKU', 1)
        board.level = 9
        board.get_new_board()
        board.board_list = board.new_board
        get_new_position()
        hero_position = new_hero_position
    if bnp == '+1+1':
        board.save_board()
        board.level += 1
        board.get_new_board()
        board.board_list = board.new_board
        get_new_position()
        hero_position = new_hero_position
    if bnp == '-1-1':
        board.save_board()
        board.level -= 1
        board.get_prev_board()
        board.board_list = board.new_board
        get_back_position()
        hero_position = new_hero_position
    if bnp == 'CRUU':
        roll_joint()
    if bnp == 'ZAPA':
        unpack_cigarettes()
    if bnp == 'CROW':
        hero_position = (new_pos_x, new_pos_y)
        if ('CROW' not in Bag or Bag['CROW'] < 1) and Bag['money'] >= 20:
            remove_from_Bag('money', 20)
            add_to_Bag('CROW', 1)
            add_to_inventory('CROW', 1)
            board.board_list[new_pos_y][new_pos_x] = 'crow'
    if bnp == 'TRGF':
        add_to_Bag('CRO1', 1)
        add_to_inventory('CRO1', 1)
        board.board_list[new_pos_y][new_pos_x] = 'TRGE'
    if bnp == 'TRSF':
        add_to_Bag('key2', 1)
        add_to_inventory('@@@@', 1)
        board.board_list[new_pos_y][new_pos_x] = 'TRSE'
    if bnp == 'TRYF':
        add_to_Bag('can', 1)
        add_to_inventory('PuPu', 1)
        board.board_list[new_pos_y][new_pos_x] = 'TRYE'
    if bnp == 'TRRF':
        add_to_Bag('bottle', 1)
        add_to_inventory('BOTT', 1)
        board.board_list[new_pos_y][new_pos_x] = 'TRRE'
    if bnp == 'RECY':
        exchange_bottle()
        exchange_cans()
        exchange_embers()
        exchange_plastic_bottles()
        exchange_needle()
            
    if bnp == 'KOLO':
        pass
        board.board_list[1][3] = '....' #have to change.
        if 'money' in Bag and Bag['money'] >= 35:
            for y in range(new_pos_y-1, new_pos_y): #to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'GaGa'
                        remove_from_Bag('money', 35)
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'GaGa'
                        remove_from_Bag('money', 35)
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'GaGa'
                        remove_from_Bag('money', 35)
                        break            
    if bnp == 'JUNK':
        pass
        if 'ganja' in Bag and Bag['ganja'] > 0:
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'PoPo'
                        remove_from_Bag('ganja', 1)
                        remove_from_inventory('GaGa', 1)
                        add_to_Bag('money', 40)
                        junkie_try += 1
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'PoPo'
                        remove_from_Bag('ganja', 1)
                        remove_from_inventory('GaGa', 1)
                        add_to_Bag('money', 40)
                        junkie_try += 1
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'PoPo'
                        remove_from_Bag('ganja', 1)
                        remove_from_inventory('GaGa', 1)
                        add_to_Bag('money', 40)
                        junkie_try += 1
                        break
            if junkie_try == 3:
                board.board_list[new_pos_y][new_pos_x] = 'JUNB'
                board.board_list[6][4] = '....' #have to change.
        if 'heroina' in Bag and Bag['heroina'] > 0:
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'IGPu'
                        remove_from_Bag('heroina', 1)
                        remove_from_inventory('HERO', 1)
                        add_to_Bag('money', 50)
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'IGPu'
                        remove_from_Bag('heroina', 1)
                        remove_from_inventory('HERO', 1)
                        add_to_Bag('money', 50)
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'IGPu'
                        remove_from_Bag('heroina', 1)
                        remove_from_inventory('HERO', 1)
                        add_to_Bag('money', 50)
                        break
            board.board_list[new_pos_y][new_pos_x] = 'EVER'
            #board.board_list[4][2] = '....' #have to change.
    if bnp == 'FATM':
        pass
        board.board_list[6][3] = '....' #have to change.
        if 'cigarrete' in Bag and Bag['cigarrete'] > 0:
            for y in range(new_pos_y-1, new_pos_y): #have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'PoPo'
                        remove_from_Bag('cigarrete', 1)
                        remove_from_inventory('CCCC', 1)
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'PoPo'
                        remove_from_Bag('cigarrete', 1)
                        remove_from_inventory('CCCC', 1)
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'PoPo'
                        remove_from_Bag('cigarrete', 1)
                        remove_from_inventory('CCCC', 1)
                        break
            board.board_list[new_pos_y][new_pos_x] = '....'
    if bnp == 'SLUT':
        pass
        #board.board_list[1][4] = '....' #have to change.
        if 'joint' in Bag and Bag['joint'] > 0:
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'PoPo'
                        remove_from_Bag('joint', 1)
                        remove_from_inventory('JoJo', 1)
                        add_to_Bag('money', 50)
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'PoPo'
                        remove_from_Bag('joint', 1)
                        remove_from_inventory('JoJo', 1)
                        add_to_Bag('money', 50)
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'PoPo'
                        remove_from_Bag('joint', 1)
                        remove_from_inventory('JoJo', 1)
                        add_to_Bag('money', 50)
                        break
        elif 'ganja' in Bag and Bag['ganja'] > 0:
            remove_from_Bag('ganja', 1)
            remove_from_inventory('GaGa', 1)
            add_to_Bag('money', 35)
    if bnp == 'BIKE':
        pass
        board.board_list[6][5] = '....' #have to change.
        if 'beerfull' in Bag and Bag['beerfull'] > 0 and bike_try <= 9:
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'PIWE'
                        remove_from_Bag('beerfull', 1)
                        remove_from_inventory('PIWF', 1)
                        add_to_Bag('money', 10)
                        bike_try += 1
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y][x] = 'PIWE'
                        remove_from_Bag('beerfull', 1)
                        remove_from_inventory('PIWF', 1)
                        add_to_Bag('money', 10)
                        bike_try += 1
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y][x] = 'PIWE'
                        remove_from_Bag('beerfull', 1)
                        remove_from_inventory('PIWF', 1)
                        add_to_Bag('money', 10)
                        bike_try += 1
                        break
    if bnp == 'LASK':
        pass
        board.board_list[7][3] = '....' # have to change.
        if 'cigarettebox' in Bag and Bag['cigarettebox'] > 0:
            remove_from_Bag('cigarettebox', 1)
            remove_from_inventory('CIGA', 1)
            add_to_Bag('money', 15)
            board.board_list[new_pos_y][new_pos_x] = 'LABE'
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'CCCC'
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'CCCC'
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'CCCC'
                        break
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'CCCC'
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'CCCC'
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'CCCC'
                        break
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'PoPo'
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'PoPo'
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'PoPo'
                        break
        elif 'ganja' in Bag and Bag['ganja'] > 0 and laska_try < 2:
            remove_from_Bag('ganja', 1)
            remove_from_inventory('GaGa', 1)
            add_to_Bag('money', 40)
            laska_try += 1
    if bnp == 'CYGA':
        pass
        board.board_list[1][1] = '....' #have to change.
        if 'money' in Bag and Bag['money'] >= 300:
            board.board_list[new_pos_y][new_pos_x] = '....'
            remove_from_Bag('money', 300)
        elif 'ganja' in Bag and Bag['ganja'] >= 9:
            board.board_list[new_pos_y][new_pos_x] = '....'
            remove_from_Bag('ganja', 9)
            remove_from_inventory('GaGa', 9)
    if bnp == 'AGAT':
        pass
        if 'cigarettebox' in Bag and Bag['cigarettebox'] > 0:
            remove_from_Bag('cigarettebox', 1)
            remove_from_inventory('CIGA', 1)
            add_to_Bag('money', 15)
        if 'cigarrete' in Bag and Bag['cigarrete'] > 0:
            remove_from_Bag('cigarrete', 1)
            remove_from_inventory('CCCC', 1)
            add_to_Bag('money', 5)
        if 'carkeys' in Bag and Bag['carkeys'] == 1:
            board.board_list[new_pos_y][new_pos_x] = '....'
            remove_from_Bag('carkeys', 1)
            remove_from_inventory('CKEY', 1)
    if bnp == 'CPU1' or bnp == 'CPU2':
        pass
        if 'heroina' in Bag and Bag['heroina'] > 0:
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'IGPu'
                        remove_from_Bag('heroina', 1)
                        remove_from_inventory('HERO', 1)
                        add_to_Bag('money', 50)
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'IGPu'
                        remove_from_Bag('heroina', 1)
                        remove_from_inventory('HERO', 1)
                        add_to_Bag('money', 50)
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'IGPu'
                        remove_from_Bag('heroina', 1)
                        remove_from_inventory('HERO', 1)
                        add_to_Bag('money', 50)
                        break
            board.board_list[new_pos_y][new_pos_x] = 'EVER'
    if bnp == 'GRAB':
        pass
        if Bag['money'] < 20:
            add_to_Bag('money', 20)
        if 'everlast' in Bag and Bag['everlast'] == 6:
            board.board_list[new_pos_y][new_pos_x] = 'CKEY'
            remove_from_Bag('everlast', 6)
            remove_from_inventory('EVER', 6)
            if 'bucketWater' in Bag and Bag['bucketWater'] == 1:
                remove_from_Bag('bucketWater', 1)
                remove_from_inventory('BUWA', 1)
            if 'bucketEmpty' in Bag and Bag['bucketEmpty'] == 1:
                remove_from_Bag('bucketEmpty', 1)
                remove_from_inventory('BUEM', 1)
            board.board_list[6][2] = '....' #have to change.
    if bnp == 'CKEY':
        add_to_Bag('carkeys', 1)
        add_to_inventory('CKEY', 1)
    if bnp == 'BUEM' and Bag['money'] >= 20:
        add_to_Bag('bucketEmpty', 1)
        add_to_inventory('BUEM', 1)
        remove_from_Bag('money', 20)
        board.board_list[new_pos_y][new_pos_x] = 'buem'
    if bnp == 'HYDR':
        if 'bucketEmpty' in Bag and Bag['bucketEmpty'] > 0:
            remove_from_inventory('BUEM', 1)
            remove_from_Bag('bucketEmpty', 1)
            add_to_inventory('BUWA', 1)
            add_to_Bag('bucketWater', 1)
    if bnp == 'POPP' and 'bucketWater' in Bag and Bag['bucketWater'] > 0:
        remove_from_Bag('bucketWater', 1)
        remove_from_inventory('BUWA', 1)
        add_to_Bag('bucketEmpty', 1)
        add_to_inventory('BUEM', 1)
        board.board_list[new_pos_y][new_pos_x] = 'MAKU'
    if bnp == 'SEKA':
        add_to_Bag('sekator', 1)
        add_to_inventory('SEKA', 1)
    if bnp == 'HEHE':
        if 'sekator' in Bag and Bag['sekator'] > 0:
            board.board_list[new_pos_y][new_pos_x] = '....'
            remove_from_Bag('sekator', 1)
            remove_from_inventory('SEKA', 1)
    if bnp == 'BOTT':
        add_to_Bag('bottle', 1)
        add_to_inventory('BOTT', 1)
    if bnp == 'IGNO' and Bag['money'] >= 5:
            add_to_Bag('Strzykawka', 1)
            add_to_inventory('IGNO', 1)
            remove_from_Bag('money', 5)
            board.board_list[new_pos_y][new_pos_x] = 'igno'
    if bnp == 'IGPu':
        add_to_Bag('StrzykawkaEmpty', 1)
        add_to_inventory('IGPu', 1)
    if bnp == 'BURN':
        cook_heroin()
    if bnp == 'EVER':
        add_to_Bag('everlast', 1)
        add_to_inventory('EVER', 1)
    else:
        pass # cannot move - wall

def remove_from_board(taken_item):
    num_cells_x = len(board.board_list[0])
    num_cells_y = len(board.board_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if board.board_list[y][x] == taken_item and x == hero_position[0] and y == hero_position[1]:
                board.board_list[y][x] = '....'
                
def add_to_Bag(added_item, q):
    if added_item in Bag:
        Bag[added_item] += q
    else:
        Bag[added_item] = q

def remove_from_Bag(removed_item, q):
    Bag[removed_item] -= q

def add_to_inventory(added_item, q):
    num_cells_y = len(lowBoard.lowBoard_list)
    while q > 0:
        for x in range(0,1):
            for y in range(num_cells_y):
                if lowBoard.lowBoard_list[y][x] == 'bEbE' or lowBoard.lowBoard_list[y][x] == '....':
                    lowBoard.lowBoard_list[y][x] = added_item
                    q -= 1
                    break
                elif lowBoard.lowBoard_list[y][x+1] == '....':
                    lowBoard.lowBoard_list[y][x+1] = added_item
                    q -= 1
                    break
                elif lowBoard.lowBoard_list[y][x+2] == '....':
                    lowBoard.lowBoard_list[y][x+2] = added_item
                    q -= 1
                    break
                elif lowBoard.lowBoard_list[y][x+3] == '....':
                    lowBoard.lowBoard_list[y][x+3] = added_item
                    q -= 1
                    break

def remove_from_inventory(removed_item, q):
    num_cells_y = len(lowBoard.lowBoard_list)
    while q > 0:
        for x in range(0,1):
            for y in range(num_cells_y):
                if lowBoard.lowBoard_list[y][x+3] == removed_item:
                    lowBoard.lowBoard_list[y][x+3] = '....'
                    q -= 1
                    break
                elif lowBoard.lowBoard_list[y][x+2] == removed_item:
                    lowBoard.lowBoard_list[y][x+2] = '....'
                    q -= 1
                    break
                elif lowBoard.lowBoard_list[y][x+1] == removed_item:
                    lowBoard.lowBoard_list[y][x+1] = '....'
                    q -= 1
                    break
                elif lowBoard.lowBoard_list[y][x] == removed_item:
                    lowBoard.lowBoard_list[y][x] = '....'
                    q -= 1
                    break

def roll_joint():
    if ('cigarrete' in Bag and Bag['cigarrete'] >= 1) and ('ganja' in Bag and Bag['ganja'] >= 1):
        remove_from_Bag('cigarrete', 1)
        remove_from_Bag('ganja', 1)
        remove_from_inventory('CCCC', 1)
        remove_from_inventory('GaGa', 1)
        add_to_Bag('joint', 1)
        add_to_inventory('JoJo', 1)

def roll_cigarrete():
    if 'ember' in Bag and Bag['ember'] >= 2:
        remove_from_Bag('ember', 2)
        remove_from_inventory('PoPo', 2)
        add_to_Bag('cigarrete', 1)
        add_to_inventory('CCCC', 1)

def cook_heroin():
    if ('poppy' in Bag and Bag['poppy'] >= 1) and ('Strzykawka' in Bag and Bag['Strzykawka'] >= 1):
        remove_from_Bag('Strzykawka', 1)
        remove_from_Bag('poppy', 1)
        remove_from_inventory('MAKU', 1)
        remove_from_inventory('IGNO', 1)
        add_to_Bag('heroina', 1)
        add_to_inventory('HERO', 1)

def unpack_cigarettes():
    if 'cigarettebox' in Bag and Bag['cigarettebox'] > 0:
        remove_from_Bag('cigarettebox', 1)
        remove_from_inventory('CIGA', 1)
        add_to_Bag('ember', 1)
        add_to_inventory('PoPo', 1)
        add_to_Bag('cigarrete', 2)
        add_to_inventory('CCCC', 2)

def emptyBag():
    if sum(Bag.values()) == 1:
        lowBoard.lowBoard_list[0][0] = 'bEbE'
    elif sum(Bag.values()) == 2 and 'bag' in Bag and 'phone' in Bag:
        lowBoard.lowBoard_list[0][0] = '....'
    elif sum(Bag.values()) == 3 and 'bag' in Bag and 'phone' in Bag and 'wallet' in Bag:
        lowBoard.lowBoard_list[0][0] = '....'
    elif sum(Bag.values()) == 4 and 'bag' in Bag and 'phone' in Bag and 'wallet' in Bag and 'cap' in Bag:
        lowBoard.lowBoard_list[0][0] = '....'
    if 'money' in Bag:
        screen.blit(font.render((str(Bag['money'])+'zł'), True, (255,255, 255)), (350, 475))

def remove_opening_credit(): #have to change it.
    if lowBoard.lowBoard_list[0][0] == 'OCOC':
        lowBoard.lowBoard_list[0][0] = '....'

def modem_switch():
    num_cells_x = len(board.board_list[0])
    num_cells_y = len(board.board_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if board.board_list[y][x] == 'MMMM':
                board.board_list[y][x] = 'M1M1'

def open_gate():
    num_cells_x = len(board.board_list[0])
    num_cells_y = len(board.board_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if board.board_list[y][x] == 'G0G0':
                board.board_list[y][x] = 'G1G1'

def wear_bag():
    num_cells_x = len(lowBoard.lowBoard_list[0])
    num_cells_y = len(lowBoard.lowBoard_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if lowBoard.lowBoard_list[y][x] == 'IIII':
                lowBoard.lowBoard_list[y][x] = 'iiii'

def instal_phone():
    num_cells_x = len(lowBoard.lowBoard_list[0])
    num_cells_y = len(lowBoard.lowBoard_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if lowBoard.lowBoard_list[y][x] == 'I0I0':
                lowBoard.lowBoard_list[y][x] = 'i0i0'

def instal_wallet():
    num_cells_x = len(lowBoard.lowBoard_list[0])
    num_cells_y = len(lowBoard.lowBoard_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if lowBoard.lowBoard_list[y][x] == 'I9I9':
                lowBoard.lowBoard_list[y][x] = 'i9i9'
                
def exchange_bottle():
    if 'beerempty' in Bag and Bag['beerempty'] > 0:
        num_cells_x = len(board.board_list[0])
        num_cells_y = len(board.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if board.board_list[y][x] == 'piwf':
                    board.board_list[y][x] = 'PIWF'
                    add_to_Bag('money', 2)
                    remove_from_Bag('beerempty', 1)
                    remove_from_inventory('PIWE', 1)
                    
def exchange_cans():
    if 'can' in Bag and Bag['can'] >= 3:
        num_cells_x = len(board.board_list[0])
        num_cells_y = len(board.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if board.board_list[y][x] == 'crow':
                    board.board_list[y][x] = 'CROW'
                    remove_from_Bag('can', 3)
                    remove_from_inventory('PuPu', 3)
                    add_to_Bag('money', 3)

def exchange_embers():
    if 'ember' in Bag and Bag['ember'] >= 4:
        num_cells_x = len(board.board_list[0])
        num_cells_y = len(board.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if board.board_list[y][x] == 'ciga':
                    board.board_list[y][x] = 'CIGA'
                    remove_from_Bag('ember', 4)
                    remove_from_inventory('PoPo', 4)
                    add_to_Bag('money', 2)

def exchange_plastic_bottles():
    if 'bottle' in Bag and Bag['bottle'] >= 3:
        num_cells_x = len(board.board_list[0])
        num_cells_y = len(board.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if board.board_list[y][x] == 'buem':
                    board.board_list[y][x] = 'BUEM'
                    remove_from_Bag('bottle', 3)
                    remove_from_inventory('BOTT', 3)
                    add_to_Bag('money', 3)

def exchange_needle():
    if 'StrzykawkaEmpty' in Bag and Bag['StrzykawkaEmpty'] > 0:
        num_cells_x = len(board.board_list[0])
        num_cells_y = len(board.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if board.board_list[y][x] == 'igno':
                    board.board_list[y][x] = 'IGNO'
                    add_to_Bag('money', 1)
                    remove_from_Bag('StrzykawkaEmpty', 1)
                    remove_from_inventory('IGPu', 1)
                    
                    
#GAME:
pygame.display.set_caption('Gra w pyGame')
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsansms', 24)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            try_move(0, +1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            try_move(0, -1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            try_move(-1, 0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            try_move(+1, 0)

    screen.fill((0,0,0))
    draw_board(cell_size)
    draw_lowBoard(cell_size)
    emptyBag()    
            
    pygame.display.flip()
    clock.tick(60)



