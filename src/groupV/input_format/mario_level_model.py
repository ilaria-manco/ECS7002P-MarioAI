#start and end of the level
MARIO_START = 'M'
MARIO_EXIT = 'F'
EMPTY = '-'

# game tiles symbols
GROUND = 'X'
PYRAMID_BLOCK = '#'
NORMAL_BRICK = 'S'
COIN_BRICK = 'C'
LIFE_BRICK = 'L'
SPECIAL_BRICK = 'U'
SPECIAL_QUESTION_BLOCK = '@'
SPECIAL_QUESTION_BLOCK_ALT = '?'
COIN_QUESTION_BLOCK = '!'
COIN_QUESTION_BLOCK_ALT = 'Q'
COIN_HIDDEN_BLOCK = '2'
LIFE_HIDDEN_BLOCK = '1'
USED_BLOCK = 'D'
COIN = 'o'
PIPE = 't'
PIPE_FLOWER = 'T'
BULLET_BILL = '*'
PLATFORM_BACKGROUND = '|'
PLATFORM = '%'

# enemies that can be in the level
GOOMBA = 'g'
GOOMBA_WINGED = 'G'
RED_KOOPA = 'r'
RED_KOOPA_WINGED = 'R'
GREEN_KOOPA = 'k'
GREEN_KOOPA_WINGED = 'K'
SPIKY = 'y'
SPIKY_WINGED = 'Y'

# array of all tiles
all_tiles = [MARIO_START,
             MARIO_EXIT,
             EMPTY,
             GROUND,
             PYRAMID_BLOCK,
             NORMAL_BRICK, COIN_BRICK, LIFE_BRICK, SPECIAL_BRICK,
             SPECIAL_QUESTION_BLOCK, SPECIAL_QUESTION_BLOCK_ALT,
             COIN_QUESTION_BLOCK, COIN_QUESTION_BLOCK_ALT,
             COIN_HIDDEN_BLOCK, LIFE_HIDDEN_BLOCK,
             USED_BLOCK,
             COIN,
             PIPE, PIPE_FLOWER,
             BULLET_BILL,
             PLATFORM_BACKGROUND, PLATFORM,
             GOOMBA, GOOMBA_WINGED,
             RED_KOOPA, RED_KOOPA_WINGED,
             GREEN_KOOPA, GREEN_KOOPA_WINGED,
             SPIKY, SPIKY_WINGED]

# map tiles to integers
tiles_to_int_mapping = dict((c, i) for i, c in enumerate(all_tiles))