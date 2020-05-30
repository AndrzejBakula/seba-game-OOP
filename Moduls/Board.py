
class Board:

    FREE_MOVES = ['....', 'BrA1', 'BrA2', 'BrA3', 'toto', 'tvtv', 'qqqq', '@@@@', '@1@1',
                  '@2@2', 'PPPP', 'WWWW', 'M1M1', 'CCCC', 'GaGa', 'CaCa', 'JoJo', 'G1G1',
                  'CRUU', 'dpdp', 'bbbb', 'QQQQ', 'PPPP', '+1+1', '-1-1', 'STA1', 'STAR',
                  'BACK', 'PoPo', 'NAP1', 'NAP2', 'NAP3', 'NAP4', 'NAP5', 'NAP6', 'NAP7',
                  '10zl', '05zl', 'CROW', 'JUNB', 'PIWF', 'PIWE', 'RECY', 'CIGA', 'CIG1',
                  'PuPu', 'crow', 'LABE', 'ZAPA', '20zl', 'piwf', 'ciga', 'MAKU', 'SKOP',
                  'SKBR', 'BUEM', 'BUWA', 'POPP', 'SEKA', 'ZNIC', ',,,,', 'NAP8', 'BOTT',
                  'buem', 'IGPu', 'IGNO', 'igno', 'HERO', 'NAP9', 'BURN', 'EVER', 'CKEY',
                  'buem']

    ITEMS_TO_TAKE = ['@@@@', '@1@1', '@2@2', 'PPPP', 'WWWW', 'GaGa', 'CaCa', 'bbbb', 'CCCC',
                    'JoJo', 'PoPo', 'PIWE', 'CIG1', 'PuPu', 'MAKU', 'SEKA', 'BOTT', 'HERO',
                    'IGPu', 'EVER', 'CKEY']

    EMPTY_CELLS = ['....', 'STAR', 'STA1', 'BACK', '-1-1', '+1+1', 'BrA1', 'BrA2',
                   'crow', 'piwf']

    level = 0
    board_list = []
    saved_boards_list = []
    new_board = []

    def __init__(self):
        with open("Boards/board.txt") as file_in:
            for line in file_in:
                self.board_list.append(line.split())

    def save_board(self):
        self.saved_boards_list.append("Boards/board" + str(self.level) + "_1.txt")
        with open("Boards/board" + str(self.level) + "_1.txt", "w") as fp:
            fp.writelines('%s\n' % '\t'.join(items) for items in self.board_list)

    def get_new_board(self):
        self.new_board = []
        if "Boards/board" + str(self.level) + "_1.txt" in self.saved_boards_list:
            with open("Boards/board" + str(self.level) + "_1.txt") as file_in:
                for line in file_in:
                    self.new_board.append(line.split())
        else:
            with open("Boards/board" + str(self.level) + ".txt") as file_in:
                for line in file_in:
                    self.new_board.append(line.split())

    def get_prev_board(self):
        self.new_board = []
        with open("Boards/board" + str(self.level) + "_1.txt") as file_in:
            for line in file_in:
                self.new_board.append(line.split())

    def modem_switch(self):
        num_cells_x = len(self.board_list[0])
        num_cells_y = len(self.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.board_list[y][x] == 'MMMM':
                    self.board_list[y][x] = 'M1M1'

    def open_gate(self):
        num_cells_x = len(self.board_list[0])
        num_cells_y = len(self.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.board_list[y][x] == 'G0G0':
                    self.board_list[y][x] = 'G1G1'

    def draw_board(self, cell_size, screen, walls, items, objects, signs, hero, hero_position, bag):  # draws main board.
        num_cells_x = len(self.board_list[0])
        num_cells_y = len(self.board_list)
        for y in range(num_cells_y):
            for x in range(num_cells_x):
                if self.board_list[y][x] == '####':
                    screen.blit(walls.wallDict['Cegla1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GLGL':
                    screen.blit(walls.wallDict['Cegla1GL'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GRGR':
                    screen.blit(walls.wallDict['Cegla1GR'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GGGG':
                    screen.blit(walls.wallDict['Cegla1G'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'LLLL':
                    screen.blit(walls.wallDict['Cegla1L'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'RRRR':
                    screen.blit(walls.wallDict['Cegla1R'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'DDDD':
                    screen.blit(walls.wallDict['Cegla1D'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'DLDL':
                    screen.blit(walls.wallDict['Cegla1DL'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'DRDR':
                    screen.blit(walls.wallDict['Cegla1DR'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'BrBr':
                    screen.blit(walls.wallDict['Cegla1broke'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GRF1':
                    screen.blit(walls.wallDict['Graffiti1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GRF2':
                    screen.blit(walls.wallDict['Graffiti2'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GF3A':
                    screen.blit(walls.wallDict['Graffiti3a'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GF3B':
                    screen.blit(walls.wallDict['Graffiti3b'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GRF4':
                    screen.blit(walls.wallDict['Graffiti4'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HWD1':
                    screen.blit(walls.wallDict['HWD1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HWD2':
                    screen.blit(walls.wallDict['HWD2'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HWD3':
                    screen.blit(walls.wallDict['HWD3'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HWD4':
                    screen.blit(walls.wallDict['HWD4'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'WRO1':
                    screen.blit(walls.wallDict['WRO1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'WKS1':
                    screen.blit(walls.wallDict['WKS1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'LOVE':
                    screen.blit(walls.wallDict['LOVE'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'KOT1':
                    screen.blit(walls.wallDict['GraffitiKot'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'KOCH':
                    screen.blit(walls.wallDict['GraffitiKocham'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'PACY':
                    screen.blit(walls.wallDict['GraffitiPacyfka'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GRG1':
                    screen.blit(walls.wallDict['GraffitiGirl1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GRG2':
                    screen.blit(walls.wallDict['GraffitiGirl2'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == ',,,,':
                    screen.blit(walls.wallDict['Lawn'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'TREE':
                    screen.blit(walls.wallDict['Tree'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEPI':
                    screen.blit(walls.wallDict['HedgePion'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEPO':
                    screen.blit(walls.wallDict['HedgePoziom'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEPD':
                    screen.blit(walls.wallDict['HedgePrawyDol'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEPG':
                    screen.blit(walls.wallDict['HedgePrawaGora'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HELG':
                    screen.blit(walls.wallDict['HedgeLewaGora'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HELD':
                    screen.blit(walls.wallDict['HedgeLewyDol'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEXX':
                    screen.blit(walls.wallDict['HedgeCross'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEXD':
                    screen.blit(walls.wallDict['HedgeCrossDol'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEXG':
                    screen.blit(walls.wallDict['HedgeCrossGora'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEXL':
                    screen.blit(walls.wallDict['HedgeCrossLewa'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEXP':
                    screen.blit(walls.wallDict['HedgeCrossPrawa'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEHE':
                    screen.blit(walls.wallDict['HedgeHeHe'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEEL':
                    screen.blit(walls.wallDict['HedgeEndLewa'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HEEP':
                    screen.blit(walls.wallDict['HedgeEndPrawa'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'bbbb':
                    screen.blit(items.itemDict['Bag1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == '$$$$':
                    screen.blit(objects.objectDict['Door1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == '$1$1':
                    screen.blit(objects.objectDict['Door1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == '$2$2':
                    screen.blit(objects.objectDict['Door1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'dpdp':
                    screen.blit(objects.objectDict['Futryna1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'G0G0':
                    screen.blit(objects.objectDict['Krata1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'G1G1':
                    screen.blit(objects.objectDict['Krata1o'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'MMMM':
                    screen.blit(objects.objectDict['ModemOff'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'M1M1':
                    screen.blit(objects.objectDict['ModemOn'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'PPPP':
                    screen.blit(items.itemDict['Phone1m'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'WWWW':
                    screen.blit(items.itemDict['Wallet1small'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CCCC':
                    screen.blit(items.itemDict['Cigarette1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'PoPo':
                    screen.blit(items.itemDict['Pojara'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GaGa':
                    screen.blit(items.itemDict['Ganja1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'JoJo':
                    screen.blit(items.itemDict['Joint'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'PIWF':
                    screen.blit(items.itemDict['PiwoFull'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'PIWE':
                    screen.blit(items.itemDict['PiwoEmpty'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CIGA':
                    screen.blit(items.itemDict['Fajki'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CIG1':
                    screen.blit(items.itemDict['Fajki'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'PuPu':
                    screen.blit(items.itemDict['Pucha'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'MAKU':
                    screen.blit(items.itemDict['Mak'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'QQQQ' or self.board_list[y][x] == 'STA1':
                    screen.blit(objects.objectDict['Wyjscie1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == '@@@@':
                    screen.blit(items.itemDict['Key2'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == '@1@1':
                    screen.blit(items.itemDict['Key1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == '@2@2':
                    screen.blit(items.itemDict['Key2'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CaCa':
                    screen.blit(items.itemDict['Czapa1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'toto':
                    screen.blit(objects.objectDict['Kibel1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'ClCl':
                    screen.blit(objects.objectDict['Szafa1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'tvtv':
                    screen.blit(objects.objectDict['TV1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CRUU':
                    screen.blit(objects.objectDict['Crusher'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'ZAPA':
                    screen.blit(objects.objectDict['Lighter'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CROW':
                    screen.blit(items.itemDict['Crowbar'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CRO1':
                    screen.blit(items.itemDict['Crowbar'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'RECY':
                    screen.blit(objects.objectDict['Recycle'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'KOLO':
                    screen.blit(objects.objectDict['Kolo'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'JUNK':
                    screen.blit(objects.objectDict['Junkie'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'JUNB':
                    screen.blit(objects.objectDict['JunkieBez'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'SLUT':
                    screen.blit(objects.objectDict['Slut'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'FATM':
                    screen.blit(objects.objectDict['Fatman'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CYGA':
                    screen.blit(objects.objectDict['Boss'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'BIKE':
                    screen.blit(objects.objectDict['Bike'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'LASK':
                    screen.blit(objects.objectDict['Laska'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'LABE':
                    screen.blit(objects.objectDict['LaskaBez'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'NAP1':
                    screen.blit(signs.signDict['KoloNapis1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'NAP2':
                    screen.blit(signs.signDict['JunkieNapis1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'NAP3':
                    screen.blit(signs.signDict['SlutNapis1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'NAP4':
                    screen.blit(signs.signDict['JubyNapis1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'NAP5':
                    screen.blit(signs.signDict['CyganNapis1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'NAP6':
                    screen.blit(signs.signDict['SkejtNapis1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'NAP7':
                    screen.blit(signs.signDict['LaskaNapis1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'NAP8':
                    screen.blit(signs.signDict['GrabarzNapis1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == '10zl':
                    screen.blit(signs.signDict['10zl'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == '05zl':
                    screen.blit(signs.signDict['5zl'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == '20zl':
                    screen.blit(signs.signDict['20zl'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'SKLE':
                    screen.blit(objects.objectDict['Sklep'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'SKOP':
                    screen.blit(objects.objectDict['SklepOpen'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'SKBR':
                    screen.blit(objects.objectDict['SklepBroken'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'TRGF':
                    screen.blit(objects.objectDict['TrashGreen'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'TRGE':
                    screen.blit(objects.objectDict['TrashGreenEmpty'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'TRSF':
                    screen.blit(objects.objectDict['TrashSilver'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'TRSE':
                    screen.blit(objects.objectDict['TrashSilverEmpty'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'TRYF':
                    screen.blit(objects.objectDict['TrashYellow'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'TRYE':
                    screen.blit(objects.objectDict['TrashYellowEmpty'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'TRRE':
                    screen.blit(objects.objectDict['TrashRedEmpty'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'TRRF':
                    screen.blit(objects.objectDict['TrashRed'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'BUEM':
                    screen.blit(items.itemDict['BucketEmpty'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HYDR':
                    screen.blit(objects.objectDict['Hydrant'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'POPP':
                    screen.blit(objects.objectDict['Poppy'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'COFF':
                    screen.blit(objects.objectDict['Coffin'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'URNN':
                    screen.blit(objects.objectDict['Urn'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'URNS':
                    screen.blit(objects.objectDict['Urns'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'SEKA':
                    screen.blit(items.itemDict['Sekator'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'ZNIC':
                    screen.blit(objects.objectDict['ZniczSklep'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CAR1':
                    screen.blit(objects.objectDict['Car'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'GRAB':
                    screen.blit(objects.objectDict['Grabarz'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'AGAT':
                    screen.blit(objects.objectDict['Agata'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'BOTT':
                    screen.blit(items.itemDict['Bottle'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'HERO':
                    screen.blit(items.itemDict['Heroina'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'IGNO':
                    screen.blit(items.itemDict['Strzykawka'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'IGPu':
                    screen.blit(items.itemDict['StrzykawkaEmpty'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'BURN':
                    screen.blit(objects.objectDict['Burner'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'EVER':
                    screen.blit(items.itemDict['Niesmiertelnik'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CPU1':
                    screen.blit(objects.objectDict['Cpun1'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CPU2':
                    screen.blit(objects.objectDict['Cpun2'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'CKEY':
                    screen.blit(items.itemDict['CarKeys'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] == 'END1':
                    screen.blit(signs.signDict['TemporaryEnd'], (x * cell_size, y * cell_size))
                elif self.board_list[y][x] in self.EMPTY_CELLS:
                    pass
                if x == hero_position[0] and y == hero_position[1]:
                    if self.board_list[y][x] == '@@@@' and self.board_list[y][x + 1] == 'BrBr':
                        screen.blit(hero.heroDict['LudzikCrowRight'], (x * cell_size, y * cell_size))
                    elif self.board_list[y][x] == '@@@@' and self.board_list[y][x - 1] == 'BrBr':
                        screen.blit(hero.heroDict['LudzikCrowLeft'], (x * cell_size, y * cell_size))
                    elif self.level == 0 and 'bag' not in bag.bag_dict:
                        screen.blit(hero.heroDict['Ludzik1'], (x * cell_size, y * cell_size))
                    else:
                        if 'cap' not in bag.bag_dict:
                            screen.blit(hero.heroDict['Ludzik1B'], (x * cell_size, y * cell_size))
                        else:
                            screen.blit(hero.heroDict['Ludzik1BC'], (x * cell_size, y * cell_size))