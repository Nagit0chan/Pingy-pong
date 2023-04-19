from pygame import *
FPS = 60

win_w = 700
win_h = 500
window = display.set_mode((win_w, win_h))
display.set_caption('Pingy_pong')
background = transform.scale(image.load('forest.jpg'), (win_w, win_h))

mixer.init()
mixer.music.load('kanet_vniz.ogg')
mixer.music.set_volume(0.02)
mixer.music.play(-1)

font.init()
font1 = font.SysFont('Arial', 24)
font2 = font.SysFont('Arial', 40)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), player_size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 35 0:
            self.rect.y += self.speed

player1 = Player('sirok.jpg', 60, 175, 7, (50, 150))
player2 = Player('sirok.jpg', 590, 175, 7, (50, 150))

clock = time.Clock()
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background, (0, 0))

    if not finish:
        player1.reset()
        player1.update_l()

        player2.reset()
        player2.update_r()

    clock.tick(FPS)
    display.update()
