import pygame
from Moduls.Board import Board
from Moduls.LowBoard import LowBoard
from Moduls.Screen import Screen
from Moduls.Hero import Hero
from Moduls.Walls import Walls
from Moduls.Items import Items
from Moduls.Objects import Objects
from Moduls.Inv import Inv
from Moduls.Signs import Signs
from Moduls.Bag import Bag
from Moduls.Recycler import Recycler
from Moduls.Steps import Steps


#BOARDS:
board = Board() #generate boards for every level; has methods to save/load local boards.
lowBoard = LowBoard() #generate inventory board.
saved_boards = board.saved_boards_list #keeps temporary boards.

#SCREEN:
screen_object = Screen(board, lowBoard)
cell_size = screen_object.CELL_SIZE
screen_width = screen_object.screen_width
screen_height = screen_object.screen_height

#HERO:
hero = Hero(board) #has hero coordinates tuple, list of hero variations and generate hero graphics dictionary.
hero_position = hero.hero_position

#BAG/ITEMS:
bag = Bag(board, hero)

#WALLS:
walls = Walls() #has list of walls and generate walls graphics dictionary.

#ITEMS:
items = Items() #has list of items and generate items graphics dictionary.

#OBJECTS:
objects = Objects() #has list of objects and generate objects graphics dictionary.

#INVENTORY:
inv = Inv(lowBoard, bag) #generate inventory graphics dictionary, got several inventory functions.

#SIGNS:
signs = Signs() #has list of signs and generate signs graphics dictionary.

#DRAWING FUNCTION:
empty_cells = ['....', 'STAR', 'STA1', 'BACK', '-1-1', '+1+1', 'BrA1', 'BrA2',
               'crow', 'piwf']
def draw_board(cell_size): #draws main board.
    num_cells_x = len(board.board_list[0])
    num_cells_y = len(board.board_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if board.board_list[y][x] == '####':
                screen.blit(walls.wallDict['Cegla1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GLGL':
                screen.blit(walls.wallDict['Cegla1GL'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRGR':
                screen.blit(walls.wallDict['Cegla1GR'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GGGG':
                screen.blit(walls.wallDict['Cegla1G'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'LLLL':
                screen.blit(walls.wallDict['Cegla1L'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'RRRR':
                screen.blit(walls.wallDict['Cegla1R'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'DDDD':
                screen.blit(walls.wallDict['Cegla1D'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'DLDL':
                screen.blit(walls.wallDict['Cegla1DL'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'DRDR':
                screen.blit(walls.wallDict['Cegla1DR'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BrBr':
                screen.blit(walls.wallDict['Cegla1broke'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRF1':
                screen.blit(walls.wallDict['Graffiti1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRF2':
                screen.blit(walls.wallDict['Graffiti2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GF3A':
                screen.blit(walls.wallDict['Graffiti3a'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GF3B':
                screen.blit(walls.wallDict['Graffiti3b'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRF4':
                screen.blit(walls.wallDict['Graffiti4'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HWD1':
                screen.blit(walls.wallDict['HWD1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HWD2':
                screen.blit(walls.wallDict['HWD2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HWD3':
                screen.blit(walls.wallDict['HWD3'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HWD4':
                screen.blit(walls.wallDict['HWD4'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'WRO1':
                screen.blit(walls.wallDict['WRO1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'WKS1':
                screen.blit(walls.wallDict['WKS1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'LOVE':
                screen.blit(walls.wallDict['LOVE'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'KOT1':
                screen.blit(walls.wallDict['GraffitiKot'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'KOCH':
                screen.blit(walls.wallDict['GraffitiKocham'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PACY':
                screen.blit(walls.wallDict['GraffitiPacyfka'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRG1':
                screen.blit(walls.wallDict['GraffitiGirl1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRG2':
                screen.blit(walls.wallDict['GraffitiGirl2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == ',,,,':
                screen.blit(walls.wallDict['Lawn'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TREE':
                screen.blit(walls.wallDict['Tree'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEPI':
                screen.blit(walls.wallDict['HedgePion'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEPO':
                screen.blit(walls.wallDict['HedgePoziom'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEPD':
                screen.blit(walls.wallDict['HedgePrawyDol'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEPG':
                screen.blit(walls.wallDict['HedgePrawaGora'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HELG':
                screen.blit(walls.wallDict['HedgeLewaGora'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HELD':
                screen.blit(walls.wallDict['HedgeLewyDol'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXX':
                screen.blit(walls.wallDict['HedgeCross'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXD':
                screen.blit(walls.wallDict['HedgeCrossDol'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXG':
                screen.blit(walls.wallDict['HedgeCrossGora'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXL':
                screen.blit(walls.wallDict['HedgeCrossLewa'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEXP':
                screen.blit(walls.wallDict['HedgeCrossPrawa'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEHE':
                screen.blit(walls.wallDict['HedgeHeHe'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEEL':
                screen.blit(walls.wallDict['HedgeEndLewa'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HEEP':
                screen.blit(walls.wallDict['HedgeEndPrawa'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'bbbb':
                screen.blit(items.itemDict['Bag1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '$$$$':
                screen.blit(objects.objectDict['Door1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '$1$1':
                screen.blit(objects.objectDict['Door1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '$2$2':
                screen.blit(objects.objectDict['Door1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'dpdp':
                screen.blit(objects.objectDict['Futryna1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'G0G0':
                screen.blit(objects.objectDict['Krata1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'G1G1':
                screen.blit(objects.objectDict['Krata1o'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'MMMM':
                screen.blit(objects.objectDict['ModemOff'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'M1M1':
                screen.blit(objects.objectDict['ModemOn'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PPPP':
                screen.blit(items.itemDict['Phone1m'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'WWWW':
                screen.blit(items.itemDict['Wallet1small'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CCCC':
                screen.blit(items.itemDict['Cigarette1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PoPo':
                screen.blit(items.itemDict['Pojara'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GaGa':
                screen.blit(items.itemDict['Ganja1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'JoJo':
                screen.blit(items.itemDict['Joint'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PIWF':
                screen.blit(items.itemDict['PiwoFull'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PIWE':
                screen.blit(items.itemDict['PiwoEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CIGA':
                screen.blit(items.itemDict['Fajki'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CIG1':
                screen.blit(items.itemDict['Fajki'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'PuPu':
                screen.blit(items.itemDict['Pucha'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'MAKU':
                screen.blit(items.itemDict['Mak'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'QQQQ' or board.board_list[y][x] == 'STA1':
                screen.blit(objects.objectDict['Wyjscie1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '@@@@':
                screen.blit(items.itemDict['Key2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '@1@1':
                screen.blit(items.itemDict['Key1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '@2@2':
                screen.blit(items.itemDict['Key2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CaCa':
                screen.blit(items.itemDict['Czapa1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'toto':
                screen.blit(objects.objectDict['Kibel1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'ClCl':
                screen.blit(objects.objectDict['Szafa1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'tvtv':
                screen.blit(objects.objectDict['TV1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CRUU':
                screen.blit(objects.objectDict['Crusher'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'ZAPA':
                screen.blit(objects.objectDict['Lighter'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CROW':
                screen.blit(items.itemDict['Crowbar'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CRO1':
                screen.blit(items.itemDict['Crowbar'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'RECY':
                screen.blit(objects.objectDict['Recycle'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'KOLO':
                screen.blit(objects.objectDict['Kolo'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'JUNK':
                screen.blit(objects.objectDict['Junkie'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'JUNB':
                screen.blit(objects.objectDict['JunkieBez'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SLUT':
                screen.blit(objects.objectDict['Slut'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'FATM':
                screen.blit(objects.objectDict['Fatman'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CYGA':
                screen.blit(objects.objectDict['Boss'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BIKE':
                screen.blit(objects.objectDict['Bike'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'LASK':
                screen.blit(objects.objectDict['Laska'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'LABE':
                screen.blit(objects.objectDict['LaskaBez'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP1':
                screen.blit(signs.signDict['KoloNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP2':
                screen.blit(signs.signDict['JunkieNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP3':
                screen.blit(signs.signDict['SlutNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP4':
                screen.blit(signs.signDict['JubyNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP5':
                screen.blit(signs.signDict['CyganNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP6':
                screen.blit(signs.signDict['SkejtNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP7':
                screen.blit(signs.signDict['LaskaNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'NAP8':
                screen.blit(signs.signDict['GrabarzNapis1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '10zl':
                screen.blit(signs.signDict['10zl'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '05zl':
                screen.blit(signs.signDict['5zl'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == '20zl':
                screen.blit(signs.signDict['20zl'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SKLE':
                screen.blit(objects.objectDict['Sklep'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SKOP':
                screen.blit(objects.objectDict['SklepOpen'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SKBR':
                screen.blit(objects.objectDict['SklepBroken'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRGF':
                screen.blit(objects.objectDict['TrashGreen'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRGE':
                screen.blit(objects.objectDict['TrashGreenEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRSF':
                screen.blit(objects.objectDict['TrashSilver'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRSE':
                screen.blit(objects.objectDict['TrashSilverEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRYF':
                screen.blit(objects.objectDict['TrashYellow'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRYE':
                screen.blit(objects.objectDict['TrashYellowEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRRE':
                screen.blit(objects.objectDict['TrashRedEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'TRRF':
                screen.blit(objects.objectDict['TrashRed'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BUEM':
                screen.blit(items.itemDict['BucketEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HYDR':
                screen.blit(objects.objectDict['Hydrant'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'POPP':
                screen.blit(objects.objectDict['Poppy'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'COFF':
                screen.blit(objects.objectDict['Coffin'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'URNN':
                screen.blit(objects.objectDict['Urn'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'URNS':
                screen.blit(objects.objectDict['Urns'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'SEKA':
                screen.blit(items.itemDict['Sekator'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'ZNIC':
                screen.blit(objects.objectDict['ZniczSklep'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CAR1':
                screen.blit(objects.objectDict['Car'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'GRAB':
                screen.blit(objects.objectDict['Grabarz'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'AGAT':
                screen.blit(objects.objectDict['Agata'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BOTT':
                screen.blit(items.itemDict['Bottle'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'HERO':
                screen.blit(items.itemDict['Heroina'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'IGNO':
                screen.blit(items.itemDict['Strzykawka'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'IGPu':
                screen.blit(items.itemDict['StrzykawkaEmpty'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'BURN':
                screen.blit(objects.objectDict['Burner'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'EVER':
                screen.blit(items.itemDict['Niesmiertelnik'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CPU1':
                screen.blit(objects.objectDict['Cpun1'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CPU2':
                screen.blit(objects.objectDict['Cpun2'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'CKEY':
                screen.blit(items.itemDict['CarKeys'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] == 'END1':
                screen.blit(signs.signDict['TemporaryEnd'], (x*cell_size,y*cell_size))
            elif board.board_list[y][x] in empty_cells:
                pass
            if x == hero_position[0] and y == hero_position[1]:
                if board.board_list[y][x] == '@@@@' and board.board_list[y][x+1] == 'BrBr':
                    screen.blit(hero.heroDict['LudzikCrowRight'], (x*cell_size,y*cell_size))
                elif board.board_list[y][x] == '@@@@' and board.board_list[y][x-1] == 'BrBr':
                    screen.blit(hero.heroDict['LudzikCrowLeft'], (x*cell_size,y*cell_size))
                elif board.level == 0 and 'bag' not in bag.bag_dict:
                    screen.blit(hero.heroDict['Ludzik1'], (x*cell_size,y*cell_size))
                else:
                    if 'cap' not in bag.bag_dict:
                        screen.blit(hero.heroDict['Ludzik1B'], (x*cell_size,y*cell_size))
                    else:
                        screen.blit(hero.heroDict['Ludzik1BC'], (x*cell_size,y*cell_size))

def draw_lowBoard(cell_size): #draws inventory board.
    num_cells_x = len(lowBoard.lowBoard_list[0])
    num_cells_y = len(lowBoard.lowBoard_list)
    ordinate = len(board.board_list)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            if lowBoard.lowBoard_list[y][x] == 'OCOC':
                screen.blit(signs.signDict['NapisPoczatkowy'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CCCC':
                screen.blit(items.itemDict['Cigarette1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'PoPo':
                screen.blit(items.itemDict['Pojara'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'GaGa':
                screen.blit(items.itemDict['Ganja1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'JoJo':
                screen.blit(items.itemDict['Joint'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'PuPu':
                screen.blit(items.itemDict['Pucha'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CIGA':
                screen.blit(items.itemDict['Fajki'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == '@@@@':
                screen.blit(items.itemDict['Key2'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == '@1@1':
                screen.blit(items.itemDict['Key1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == '@2@2':
                screen.blit(items.itemDict['Key2'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CROW':
                screen.blit(items.itemDict['Crowbar'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CRO1':
                screen.blit(items.itemDict['Crowbar'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'PIWF':
                screen.blit(items.itemDict['PiwoFull'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'PIWE':
                screen.blit(items.itemDict['PiwoEmpty'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'MAKU':
                screen.blit(items.itemDict['Mak'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'BUEM':
                screen.blit(items.itemDict['BucketEmpty'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'BUWA':
                screen.blit(items.itemDict['BucketWater'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'SEKA':
                screen.blit(items.itemDict['Sekator'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'iiii':
                screen.blit(inv.invDict['Inventory1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'i0i0':
                screen.blit(inv.invDict['Phone1'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'i9i9':
                screen.blit(inv.invDict['Wallet1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'iMon':
                screen.blit(signs.signDict['Kwota1'], (x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'bEbE':
                screen.blit(signs.signDict['BagEmpty'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'BOTT':
                screen.blit(items.itemDict['Bottle'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'HERO':
                screen.blit(items.itemDict['Heroina'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'IGNO':
                screen.blit(items.itemDict['Strzykawka'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'IGPu':
                screen.blit(items.itemDict['StrzykawkaEmpty'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'EVER':
                screen.blit(items.itemDict['Niesmiertelnik'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == 'CKEY':
                screen.blit(items.itemDict['CarKeys'],(x*cell_size,(ordinate+y)*cell_size))
            elif lowBoard.lowBoard_list[y][x] == ('....' or 'IIII'):
                pass # empty cell

#MOVE/STEP/ACTION FUNCTION:
steps = Steps(board, lowBoard, bag)

def try_move(stepX, stepY): #main game function - hero moves and actions.
    global hero_position
    new_pos_x = hero_position[0]+stepX
    new_pos_y = hero_position[1]+stepY
    last_pos_x = hero_position[0]
    last_pos_y = hero_position[1]
    bnp = board.board_list[new_pos_y][new_pos_x]
    blp = board.board_list[last_pos_y][last_pos_x]
    lowBoard.remove_opening_credit() #removes starting sign from inventory board.

    if (bnp in board.FREE_MOVES):
        hero_position = (new_pos_x, new_pos_y)
    if (bnp in board.ITEMS_TO_TAKE):
        board.board_list[new_pos_y][new_pos_x] = '....'
    if bnp == '@@@@': #key.
        bag.add_to_Bag('key2', 1)
        lowBoard.add_to_inventory('@@@@', 1)
    if bnp == '@1@1': #key.
        bag.add_to_Bag('key', 1)
        lowBoard.add_to_inventory('@1@1', 1)
    if bnp == '@2@2': #key.
        bag.add_to_Bag('key3', 1)
        lowBoard.add_to_inventory('@2@2', 1)
    if bnp == 'PPPP': #phone.
        bag.add_to_Bag('phone', 1)
        board.modem_switch()
        lowBoard.instal_phone()
    if bnp == 'WWWW': #wallet.
        bag.add_to_Bag('wallet', 1)
        bag.add_to_Bag('money', 50)
        lowBoard.instal_wallet()
        #lowBoard.lowBoard_list[2][4] = 'i9i9' #This is hardcoded, I have to change it.
    if bnp == 'M1M1': #modem - it opens gate.
        board.open_gate()
    if bnp == 'ClCl' and 'key' in bag.bag_dict and bag.bag_dict['key'] == 1: #closet with stuff.
        hero_position = (new_pos_x, new_pos_y)
        steps.open_closet(new_pos_x, new_pos_y)
        bag.remove_from_Bag('key', 1)
        lowBoard.remove_from_inventory('@1@1', 1)
    if bnp == 'BrBr' and blp == 'BrA1': #broken wall - hidden stuff.
        pass
        if ('cigarrete' not in bag.bag_dict or ('cigarrete' in bag.bag_dict and bag.bag_dict['cigarrete'] == 0)) and board.board_list[new_pos_y][new_pos_x-1] == '....':
            board.board_list[new_pos_y][new_pos_x-1] = 'CCCC'
    if bnp == 'BrBr' and blp == 'BrA2': #broken wall - hidden stuff.
        pass
        if ('ganja' not in bag.bag_dict or ('ganja' in bag.bag_dict and bag.bag_dict['ganja'] == 0)) and board.board_list[new_pos_y][new_pos_x-1] == '....':
            board.board_list[new_pos_y][new_pos_x-1] = 'GaGa'
    if bnp == 'BrBr' and blp == 'BrA3': #broken wall - hidden stuff.
        pass
        if 'CRO1' in bag.bag_dict and bag.bag_dict['CRO1'] > 0: #crowbar.
            board.board_list[last_pos_y][last_pos_x] = '@@@@'
            bag.remove_from_Bag('CRO1', 1)
            lowBoard.remove_from_inventory('CRO1', 1)
    if bnp == 'CCCC': #cigarrete.
        bag.add_to_Bag('cigarrete', 1)
        lowBoard.add_to_inventory('CCCC', 1)
    if bnp == 'PoPo': #ciggaret butt (ember).
        bag.add_to_Bag('ember', 1)
        lowBoard.add_to_inventory('PoPo', 1)
    if bnp == 'GaGa': #piece of ganja.
        bag.add_to_Bag('ganja', 1)
        lowBoard.add_to_inventory('GaGa', 1)
    if bnp == 'JoJo': #joint.
        bag.add_to_Bag('joint', 1)
        lowBoard.add_to_inventory('JoJo', 1)
    if bnp == 'PIWF': #full bottle of beer.
        if bag.bag_dict['money'] >= 5:
            bag.add_to_Bag('beerfull', 1)
            lowBoard.add_to_inventory('PIWF', 1)
            bag.remove_from_Bag('money', 5)
            board.board_list[new_pos_y][new_pos_x] = 'piwf'
    if bnp == 'PIWE': #empty bottle of beer.
        bag.add_to_Bag('beerempty', 1)
        lowBoard.add_to_inventory('PIWE', 1)
    if bnp == 'CIGA': #cigarrete box for buy in store.
        hero_position = (new_pos_x, new_pos_y)
        if bag.bag_dict['money'] >= 10:
            bag.add_to_Bag('cigarettebox', 1)
            lowBoard.add_to_inventory('CIGA', 1)
            bag.remove_from_Bag('money', 10)
            board.board_list[new_pos_y][new_pos_x] = 'ciga'
    if bnp == 'CIG1': #cigarrete box to take.
        hero_position = (new_pos_x, new_pos_y)
        bag.add_to_Bag('cigarettebox', 1)
        lowBoard.add_to_inventory('CIGA', 1)
    if bnp == 'PuPu': #can (metal trash).
        bag.add_to_Bag('can', 1)
        lowBoard.add_to_inventory('PuPu', 1)
    if bnp == 'MAKU': #flower of poppy.
        bag.add_to_Bag('poppy', 1)
        lowBoard.add_to_inventory('MAKU', 1)
    if bnp == 'CaCa': #baseball cap.
        bag.add_to_Bag('cap', 1)
    if bnp == '$$$$': #door.
        if 'key3' in bag.bag_dict and bag.bag_dict['key3'] > 0:
            hero_position = (new_pos_x, new_pos_y)
            board.board_list[new_pos_y][new_pos_x] = 'dpdp'
            bag.remove_from_Bag('key3', 1)
            lowBoard.remove_from_inventory('@2@2', 1)
        else:
            pass # cannot move - closed
    if bnp == 'SKLE': #locked store door to destroy.
        if 'CROW' in bag.bag_dict and bag.bag_dict['CROW'] > 0:
            hero_position = (new_pos_x, new_pos_y)
            board.board_list[new_pos_y][new_pos_x] = 'SKBR'
            bag.remove_from_Bag('CROW', 1)
            lowBoard.remove_from_inventory('CROW', 1)
        else:
            pass # cannot move - closed
    if bnp == '$1$1': #door.
        if 'key2' in bag.bag_dict and bag.bag_dict['key2'] == 1:
            hero_position = (new_pos_x, new_pos_y)
            board.board_list[new_pos_y][new_pos_x] = 'dpdp'
            bag.remove_from_Bag('key2', 1)
            lowBoard.remove_from_inventory('@@@@', 1)
        else:
            pass # cannot move - closed
    if bnp == 'bbbb': #bag - we takes it once.
        bag.add_to_Bag('bag', 1)
        lowBoard.wear_bag()
    if bnp == 'QQQQ': #quit to next level.
        board.level += 1
        board.get_new_board()
        board.board_list = board.new_board
        hero.get_new_position()
        hero_position = hero.new_hero_position
    if bnp == 'QQQ1': #quit to next level.
        board.level = 5
        board.get_new_board()
        board.board_list = board.new_board
        hero.get_new_position()
        hero_position = hero.new_hero_position
    if bnp == 'QQQ2': #quit to next level.
        if 'Strzykawka' in bag.bag_dict and bag.bag_dict['Strzykawka'] == 1:
            bag.remove_from_Bag('Strzykawka', 1)
            lowBoard.remove_from_inventory('IGNO', 1)
        if 'StrzykawkaEmpty' in bag.bag_dict and bag.bag_dict['StrzykawkaEmpty'] == 1:
            bag.remove_from_Bag('StrzykawkaEmpty', 1)
            lowBoard.remove_from_inventory('IGPu', 1)
        if 'poppy' in bag.bag_dict and bag.bag_dict['poppy'] == 1:
            bag.remove_from_Bag('poppy', 1)
            lowBoard.remove_from_inventory('MAKU', 1)
        board.level = 9
        board.get_new_board()
        board.board_list = board.new_board
        hero.get_new_position()
        hero_position = hero.new_hero_position
    if bnp == '+1+1': #passage to next sub-level.
        board.save_board()
        board.level += 1
        board.get_new_board()
        board.board_list = board.new_board
        hero.get_new_position()
        hero_position = hero.new_hero_position
    if bnp == '-1-1': #passage to previous sub-level.
        board.save_board()
        board.level -= 1
        board.get_prev_board()
        board.board_list = board.new_board
        hero.get_back_position()
        hero_position = hero.new_hero_position
    if bnp == 'CRUU': #crusher for ganja - we roll joints here.
        inv.roll_joint()
    if bnp == 'ZAPA': #lighter - we open cigarretes here.
        inv.unpack_cigarettes()
    if bnp == 'CROW': #crowbar to buy in store.
        hero_position = (new_pos_x, new_pos_y)
        if ('CROW' not in bag.bag_dict or bag.bag_dict['CROW'] < 1) and bag.bag_dict['money'] >= 20:
            bag.remove_from_Bag('money', 20)
            bag.add_to_Bag('CROW', 1)
            lowBoard.add_to_inventory('CROW', 1)
            board.board_list[new_pos_y][new_pos_x] = 'crow'
    if bnp == 'TRGF': #trash box where you can take crowbar.
        bag.add_to_Bag('CRO1', 1)
        lowBoard.add_to_inventory('CRO1', 1)
        board.board_list[new_pos_y][new_pos_x] = 'TRGE'
    if bnp == 'TRSF': #thrash box where you can take key.
        bag.add_to_Bag('key2', 1)
        lowBoard.add_to_inventory('@@@@', 1)
        board.board_list[new_pos_y][new_pos_x] = 'TRSE'
    if bnp == 'TRYF': #thrash box where you can take can.
        bag.add_to_Bag('can', 1)
        lowBoard.add_to_inventory('PuPu', 1)
        board.board_list[new_pos_y][new_pos_x] = 'TRYE'
    if bnp == 'TRRF': #thrash box where you can take empty bottle.
        bag.add_to_Bag('bottle', 1)
        lowBoard.add_to_inventory('BOTT', 1)
        board.board_list[new_pos_y][new_pos_x] = 'TRRE'
    if bnp == 'RECY': #recycle been - you can exchange here trash for store products.
        recycler.exchange_bottle()
        recycler.exchange_cans()
        recycler.exchange_embers()
        recycler.exchange_plastic_bottles()
        recycler.exchange_needle()
            
    if bnp == 'KOLO': #he sells ganja for cash.
        pass
        board.board_list[1][3] = '....' #this is hardcoded - I have to change it.
        steps.buy_cannabis(new_pos_x, new_pos_y)
    if bnp == 'JUNK': #she takes ganja or heroine for cash; leaves cigarrete butts (ember).
        pass
        steps.deal_with_junkie(new_pos_x, new_pos_y)
    if bnp == 'FATM': #he takes cigarret and leave ciggaret butt (ember).
        pass
        board.board_list[6][3] = '....' #this is hardcoded - I have to change it.
        steps.cigarrete_for_fatman(new_pos_x, new_pos_y)
    if bnp == 'SLUT': #she takes joints for cash; give away cigarret butt.
        pass
        #board.board_list[1][4] = '....' #this is hardcoded - I have to change it.
        steps.deal_with_slut(new_pos_x, new_pos_y)
    if bnp == 'BIKE': #guy with bike - takes beer for cash, give away empty bottle.
        pass
        board.board_list[6][5] = '....' #this is hardcoded - I have to change it.
        steps.beer_for_biker(new_pos_x, new_pos_y)
    if bnp == 'LASK': #she takes cigarrete box for cash and leaves cigarettes and ember.
        pass
        board.board_list[7][3] = '....' # this is hardcoded - I have to change it.
        steps.deel_with_laska(new_pos_x, new_pos_y)
    if bnp == 'CYGA': #first boss - you need to get 300zł or 9 piece of ganja for him.
        pass
        board.board_list[1][1] = '....' # this is hardcoded - I have to change it.
        if 'money' in bag.bag_dict and bag.bag_dict['money'] >= 300:
            board.board_list[new_pos_y][new_pos_x] = '....'
            bag.remove_from_Bag('money', 300)
        elif 'ganja' in bag.bag_dict and bag.bag_dict['ganja'] >= 9:
            board.board_list[new_pos_y][new_pos_x] = '....'
            bag.remove_from_Bag('ganja', 9)
            lowBoard.remove_from_inventory('GaGa', 9)
    if bnp == 'AGAT': #she takes car keys and let you escape; she can buy cigarrete box.
        pass
        if 'cigarettebox' in bag.bag_dict and bag.bag_dict['cigarettebox'] > 0:
            bag.remove_from_Bag('cigarettebox', 1)
            lowBoard.remove_from_inventory('CIGA', 1)
            bag.add_to_Bag('money', 15)
        if 'cigarrete' in bag.bag_dict and bag.bag_dict['cigarrete'] > 0:
            bag.remove_from_Bag('cigarrete', 1)
            lowBoard.remove_from_inventory('CCCC', 1)
            bag.add_to_Bag('money', 5)
        if 'carkeys' in bag.bag_dict and bag.bag_dict['carkeys'] == 1:
            board.board_list[new_pos_y][new_pos_x] = '....'
            bag.remove_from_Bag('carkeys', 1)
            lowBoard.remove_from_inventory('CKEY', 1)
    if bnp == 'CPU1' or bnp == 'CPU2': #junkies who takes heroine for cash and leave everlast and empty syringe.
        pass
        if 'heroina' in bag.bag_dict and bag.bag_dict['heroina'] > 0:
            for y in range(new_pos_y-1, new_pos_y): # have to simplify.
                for x in range(new_pos_x-1, new_pos_x+2):
                    if board.board_list[y][x] == '....':
                        board.board_list[y][x] = 'IGPu'
                        bag.remove_from_Bag('heroina', 1)
                        lowBoard.remove_from_inventory('HERO', 1)
                        bag.add_to_Bag('money', 50)
                        break
                    elif board.board_list[y+1][x] == '....':
                        board.board_list[y+1][x] = 'IGPu'
                        bag.remove_from_Bag('heroina', 1)
                        lowBoard.remove_from_inventory('HERO', 1)
                        bag.add_to_Bag('money', 50)
                        break
                    elif board.board_list[y+2][x] == '....':
                        board.board_list[y+2][x] = 'IGPu'
                        bag.remove_from_Bag('heroina', 1)
                        lowBoard.remove_from_inventory('HERO', 1)
                        bag.add_to_Bag('money', 50)
                        break
            board.board_list[new_pos_y][new_pos_x] = 'EVER'
    if bnp == 'GRAB': #second boss - takes all everlasts and leaves car keys.
        pass
        if bag.bag_dict['money'] < 20:
            bag.add_to_Bag('money', 20)
        if 'everlast' in bag.bag_dict and bag.bag_dict['everlast'] == 6:
            board.board_list[new_pos_y][new_pos_x] = 'CKEY'
            bag.remove_from_Bag('everlast', 6)
            lowBoard.remove_from_inventory('EVER', 6)
            if 'bucketWater' in bag.bag_dict and bag.bag_dict['bucketWater'] == 1:
                bag.remove_from_Bag('bucketWater', 1)
                lowBoard.remove_from_inventory('BUWA', 1)
            if 'bucketEmpty' in bag.bag_dict and bag.bag_dict['bucketEmpty'] == 1:
                bag.remove_from_Bag('bucketEmpty', 1)
                lowBoard.remove_from_inventory('BUEM', 1)
            board.board_list[6][2] = '....' #this is hardcoded - I have to change it.
    if bnp == 'CKEY': #car key.
        bag.add_to_Bag('carkeys', 1)
        lowBoard.add_to_inventory('CKEY', 1)
    if bnp == 'BUEM' and bag.bag_dict['money'] >= 20:
        bag.add_to_Bag('bucketEmpty', 1)
        lowBoard.add_to_inventory('BUEM', 1)
        bag.remove_from_Bag('money', 20)
        board.board_list[new_pos_y][new_pos_x] = 'buem'
    if bnp == 'HYDR': #hydrant - you can get water from here.
        if 'bucketEmpty' in bag.bag_dict and bag.bag_dict['bucketEmpty'] > 0:
            lowBoard.remove_from_inventory('BUEM', 1)
            bag.remove_from_Bag('bucketEmpty', 1)
            lowBoard.add_to_inventory('BUWA', 1)
            bag.add_to_Bag('bucketWater', 1)
    if bnp == 'POPP' and 'bucketWater' in bag.bag_dict and bag.bag_dict['bucketWater'] > 0: #poppy-seed watering.
        bag.remove_from_Bag('bucketWater', 1)
        lowBoard.remove_from_inventory('BUWA', 1)
        bag.add_to_Bag('bucketEmpty', 1)
        lowBoard.add_to_inventory('BUEM', 1)
        board.board_list[new_pos_y][new_pos_x] = 'MAKU'
    if bnp == 'SEKA': #secateurs.
        bag.add_to_Bag('sekator', 1)
        lowBoard.add_to_inventory('SEKA', 1)
    if bnp == 'HEHE': #hedge to cut.
        if 'sekator' in bag.bag_dict and bag.bag_dict['sekator'] > 0:
            board.board_list[new_pos_y][new_pos_x] = '....'
            bag.remove_from_Bag('sekator', 1)
            lowBoard.remove_from_inventory('SEKA', 1)
    if bnp == 'BOTT': #bottle.
        bag.add_to_Bag('bottle', 1)
        lowBoard.add_to_inventory('BOTT', 1)
    if bnp == 'IGNO' and bag.bag_dict['money'] >= 5: #new syringe to buy in store.
            bag.add_to_Bag('Strzykawka', 1)
            lowBoard.add_to_inventory('IGNO', 1)
            bag.remove_from_Bag('money', 5)
            board.board_list[new_pos_y][new_pos_x] = 'igno'
    if bnp == 'IGPu': #used syrigne to exchange in recycler been.
        bag.add_to_Bag('StrzykawkaEmpty', 1)
        lowBoard.add_to_inventory('IGPu', 1)
    if bnp == 'BURN': #burner where you can cook heroine.
        inv.cook_heroin()
    if bnp == 'EVER': #everlast.
        bag.add_to_Bag('everlast', 1)
        lowBoard.add_to_inventory('EVER', 1)
    else:
        pass # cannot move - wall

#OTHER FUNCTIONS AND CLASSES.
def emptyBag(): #checks is bag empty or not.
    if sum(bag.bag_dict.values()) == 1:
        lowBoard.lowBoard_list[0][0] = 'bEbE'
    elif sum(bag.bag_dict.values()) == 2 and 'bag' in bag.bag_dict and 'phone' in bag.bag_dict:
        lowBoard.lowBoard_list[0][0] = '....'
    elif sum(bag.bag_dict.values()) == 3 and 'bag' in bag.bag_dict and 'phone' in bag.bag_dict and 'wallet' in bag.bag_dict:
        lowBoard.lowBoard_list[0][0] = '....'
    elif sum(bag.bag_dict.values()) == 4 and 'bag' in bag.bag_dict and 'phone' in bag.bag_dict and 'wallet' in bag.bag_dict and 'cap' in bag.bag_dict:
        lowBoard.lowBoard_list[0][0] = '....'
    if 'money' in bag.bag_dict:
        screen.blit(font.render((str(bag.bag_dict['money'])+'zł'), True, (255,255, 255)), (350, 475))

recycler = Recycler(board, lowBoard, bag) #exchange trash into goods for buy in store.

#GAME:
pygame.display.set_caption('Gra w pyGame')
pygame.init()
font = pygame.font.SysFont('comicsansms', 24)
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
clock = pygame.time.Clock()

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
