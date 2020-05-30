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

#BAG:
bag = Bag(board, lowBoard, hero)

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


#MOVE/STEP/ACTION FUNCTION - CORE OF THE GAME PLOT:
steps = Steps(board, lowBoard, bag) #keeps action/hero-steps method (game plot).
recycler = Recycler(board, lowBoard, bag) #exchange trash into goods for buy in store.

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
        steps.pay_off_Cygan(new_pos_x, new_pos_y)
    if bnp == 'AGAT': #she takes car keys and let you escape; she can buy cigarrete box.
        pass
        steps.flirt_with_Agata(new_pos_x, new_pos_y)
    if bnp == 'CPU1' or bnp == 'CPU2': #junkies who takes heroine for cash and leave everlast and empty syringe.
        pass
        steps.deal_with_heroine_junkie(new_pos_x, new_pos_y)
    if bnp == 'GRAB': #second boss - takes all everlasts and leaves car keys.
        pass
        steps.meet_the_gravedigger(new_pos_x, new_pos_y)
    if bnp == 'CKEY': #car key.
        bag.add_to_Bag('carkeys', 1)
        lowBoard.add_to_inventory('CKEY', 1)
    if bnp == 'BUEM' and bag.bag_dict['money'] >= 20: #empty bucket.
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


#GAME LOOP:
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
    board.draw_board(cell_size, screen, walls, items, objects, signs, hero, hero_position, bag)
    lowBoard.draw_lowBoard(cell_size, screen, items, signs, board, inv)
    bag.emptyBag(font, screen)

    pygame.display.flip()
    clock.tick(60)
