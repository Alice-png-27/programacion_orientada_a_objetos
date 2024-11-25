import pygame
pygame.init()

WIDTH_INIT = 1000
HEIGHT_INIT = 900
WIDTH, HEIGHT = 800,720

screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)
pygame.display.set_caption('Two-Player Pygame Chess!')
# These are the classic variables that we need to use for every game in 'pygame'. The 'WIDTH' and 'HEIGHT' correspond to the size of the screen that will pop up.
# The 'screen' variable is the place where we're going to draw everything that happens during the game.


# Even as the font is the same we put three different sizes. Why? Most probably for aesthetic purposes

timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
# The 'selection' variable appears to just be an arbitrary number that will change depending on what we select.
valid_moves = []

def calcular_escala():
    scale_x = screen.get_width() / WIDTH_INIT
    scale_y = screen.get_height() / HEIGHT_INIT
    return min(scale_x, scale_y)  # Escala uniforme para evitar distorsión
def escalar(valor):
    return int(valor * calcular_escala())
def cargar_imagen(file, width, height):
    image = pygame.image.load(file)
    return pygame.transform.scale(image, (escalar(width), escalar(height)))
def obtener_fuente(tamaño):
    return pygame.font.Font('freesansbold.ttf', escalar(tamaño))

SMALL_FONT = obtener_fuente(20)
MEDIUM_FONT = obtener_fuente(40)
BIG_FONT = obtener_fuente(50)

# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = cargar_imagen("images/black_queen.png", 80, 80)

black_queen_small = cargar_imagen("images/black_queen.png", 45, 45)
# While it doesn't appear as an option to tab, to link a file to the method '.load()' I just need to put the name of the folder next to a ...
# ... slash (/) and the file name and extension.

black_king = cargar_imagen("images/black_king.png", 80, 80)
black_king_small = cargar_imagen("images/black_king.png", 45, 45)

black_rook = cargar_imagen("images/black_rook.png", 80, 80)
black_rook_small = cargar_imagen("images/black_rook.png", 45, 45)


black_bishop = cargar_imagen("images/black_bishop.png", 80, 80)
black_bishop_small = cargar_imagen("images/black_bishop.png", 45, 45)


black_knight = cargar_imagen("images/black_knight.png", 80, 80)
black_knight_small = cargar_imagen("images/black_knight.png", 45, 45)


black_pawn = cargar_imagen("images/black_pawn.png", 65, 65)
black_pawn_small = cargar_imagen("images/black_pawn.png", 45, 45)


white_queen = cargar_imagen("images/white_queen.png", 80, 80)
white_queen_small = cargar_imagen("images/white_queen.png", 45, 45)


white_king = cargar_imagen("images/white_king.png", 80, 80)
white_king_small = cargar_imagen("images/white_king.png", 45, 45)


white_rook = cargar_imagen("images/white_rook.png", 80, 80)
white_rook_small = cargar_imagen("images/white_rook.png", 45, 45)


white_bishop = cargar_imagen("images/white_bishop.png", 80, 80)
white_bishop_small = cargar_imagen("images/white_bishop.png", 45, 45)


white_knight = cargar_imagen("images/white_knight.png", 80, 80)
white_knight_small = cargar_imagen("images/white_knight.png", 45, 45)


white_pawn = cargar_imagen("images/white_pawn.png", 65, 65)
white_pawn_small = cargar_imagen("images/white_pawn.png", 45, 45)

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
white_promotions = ['bishop', 'knight', 'rook', 'queen']
white_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False,]

small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
black_promotions = ['bishop', 'knight', 'rook', 'queen']
black_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False,]

small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# check variables/ flashing counter
counter = 0
winner = ''
game_over = False
white_ep = (escalar(100), escalar(100))
black_ep = (escalar(100), escalar(100))
# Again, two nonsense values.
white_promote = False
black_promote = False
promo_index = 100
