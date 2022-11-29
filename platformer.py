import pygame

pygame.init()

WINDOW_SIZE = (800, 800)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("platformer")

clock = pygame.time.Clock()
FPS = 60

move_right = False
move_left = False
on_ground = False

run = True

game_map = [
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','2','2','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['2','0','0','0','0','0','0','0','0','2'],
    ['1','2','2','2','2','2','2','2','2','1'],
    ['1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1'],
    ]
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, gravity):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('img/player.png')
        self.image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.gravity = gravity

    def move(self, moving_right, moving_left, on_ground):
        dx = 0
        
        if moving_right:
            dx = self.speed
        if moving_left:
            dx = -self.speed
        if on_ground:
            dy = 0
        else:
            dy = 5

        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self):
        screen.blit(self.image, self.rect)

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(image)
       self.image = pygame.transform.scale(self.image, (width, height))
       self.x = x
       self.y = y
       self.rect = self.image.get_rect()
    
    def draw(self):
        screen.blit(self.image, self.rect)
        self.rect.x = self.x
        self.rect.y = self.y

class TileMap():
    def __init__(self, game_map):
        self.x = 0
        self.y = 0
        self.width = screen.get_width() / len(game_map[0])
        self.height = screen.get_height() / len(game_map)
        self.tilemap = []
        self.dx = self.width
        self.dy = self.height
        self.tile = None
        for i in range(len(game_map)):
            self.tilerow = []
            self.x = 0
            for j in range(len(game_map[0])):
                if game_map[i][j] == '2':
                    self.tile = Tile('img/grass.png', self.x, self.y, self.width, self.width)
                if game_map[i][j] == '1':
                    self.tile = Tile('img/dirt.png', self.x, self.y, self.width, self.width)
                if game_map[i][j] == '0':
                    self.tile = None
                self.tilerow.append(self.tile)
                self.x += self.dx
            self.tilemap.append(self.tilerow)
            self.y += self.dy
    
    def draw(self):
        for i in range(len(self.tilemap)):
            for j in range(len(self.tilemap[0])):
                if self.tilemap[i][j] != None:
                    self.tilemap[i][j].draw()

def draw_background():
    screen.fill((144,201,120))

player = Player(200, 200, 2, 2)
tilemap = TileMap(game_map)

while run:
    draw_background()
    tilemap.draw()
    player.draw()
    player.move(move_right, move_left, on_ground)

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
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
