import pygame

pygame.init()

WINDOW_SIZE = (800, 640)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("platformer")

clock = pygame.time.Clock()
FPS = 60

move_right = False
move_left = False

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('img/player.png')
        self.image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
    
    def move(self, moving_right, moving_left):
        dx = 0
        dy = 0
        
        if moving_right:
            dx = self.speed
        if moving_left:
            dx = -self.speed

        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self):
        screen.blit(self.image, self.rect)

class TileGrid:
    def __init__(self):
        grid = [
            [0,0,0,0,0]
            [0,0,0,0,0]
            [1,1,1,1,1]
        ]
        

def draw_background():
    screen.fill((144,201,120))

player = Player(200, 200, 2)

run = True
while run:
    draw_background()
    player.draw()
    player.move(move_right, move_left)

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
