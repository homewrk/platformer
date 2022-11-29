import pygame

pygame.init()

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("platformer")

display = pygame.Surface((300, 200))

clock = pygame.time.Clock()
FPS = 60

move_right = False
move_left = False

run = True

TILE_SIZE = pygame.image.load('img/grass.png').get_width()

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]
            
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, gravity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/player.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.gravity = gravity

    def move(self, moving_right, moving_left, hit_list):
        
        collision_type = {
            'top': False,
            'bottom': False,
            'right': False,
            'left': False
        }

        dx = 0
        dy = 0
        if moving_right:
            dx = 5
        if moving_left:
            dx = -5

        for tile in hit_list:
            if dx > 0:
                self.rect.right = tile.left
                collision_type['right'] = True
            elif dx < 0:
                self.rect.left = tile.right
                collision_type['left'] = True

        for tile in hit_list:
            if dy > 0:
                self.rect.bottom = tile.top
                collision_type['bottom'] = True
            elif dy < 0:
                self.rect.top = tile.bottom
                collision_type['top'] = True
        if collision_type['right'] == True or collision_type['left'] == True: 
            dx = 0
        else: 
            self.rect.x += dx

        if collision_type['bottom'] == True:
            dy = 5
            self.rect.y += dy
        else:
            dy = 0

    def draw(self):
        display.blit(self.image, self.rect)

# OLD TILE SYSTEM:
# class Tile(pygame.sprite.Sprite):
#     def __init__(self, image, x, y, width, height):
#        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.image.load(image)
#        self.image = pygame.transform.scale(self.image, (width, height))
#        self.x = x
#        self.y = y
#        self.rect = self.image.get_rect()
    
#     def draw(self):
#         display.blit(self.image, self.rect)
#         self.rect.x = self.x
#         self.rect.y = self.y

# class TileMap():
#     def __init__(self, game_map):
#         self.x = 0
#         self.y = 0
#         self.width = display.get_width() / len(game_map[0])
#         self.height = display.get_height() / len(game_map)
#         self.tilemap = []
#         self.dx = self.width
#         self.dy = self.height
#         self.tile = None
#         for i in range(len(game_map)):
#             self.tilerow = []
#             self.x = 0
#             for j in range(len(game_map[0])):
#                 if game_map[i][j] == '2':
#                     self.tile = Tile('img/grass.png', self.x, self.y, self.width, self.width)
#                 if game_map[i][j] == '1':
#                     self.tile = Tile('img/dirt.png', self.x, self.y, self.width, self.width)
#                 if game_map[i][j] == '0':
#                     self.tile = None
#                 self.tilerow.append(self.tile)
#                 self.x += self.dx
#             self.tilemap.append(self.tilerow)
#             self.y += self.dy
    
#     def draw(self):
#         for i in range(len(self.tilemap)):
#             for j in range(len(self.tilemap[0])):
#                 if self.tilemap[i][j] != None:
#                     self.tilemap[i][j].draw()

def draw_background():
    display.fill((144,201,120))


class TileMap():
    def __init__(self, game_map):
        self.game_map = game_map
    
    def draw_tiles(self):
        self.tile_rects = []
        y = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                if tile == '2':
                    display.blit(pygame.image.load('img/grass.png'), (x * TILE_SIZE, y * TILE_SIZE))
                if tile == '1':
                    display.blit(pygame.image.load('img/dirt.png'), (x * TILE_SIZE, y * TILE_SIZE))
                if tile != '0':
                    self.tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y += 1

    def collision_test(self, rect):
        hit_list = []
        for tile in self.tile_rects:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

tilemap = TileMap(game_map)
player = Player(100, 100, 2, 2)

while run:
    draw_background()
    tilemap.draw_tiles()
    player.draw()
    hit_list = tilemap.collision_test(player.rect)
    player.move(move_right, move_left, hit_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
