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
lose1 = font2.render('PLAYER 1 LOSE!', True, (180, 0 , 0))
lose2 = font2.render('PLAYER 2 LOSE!', True, (180, 0 , 0))

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
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size):
        super().__init__(player_image, player_x, player_y, player_speed, player_size)
        self.speed_x = player_speed
        self.speed_y = player_speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

player1 = Player('sirok.jpg', 70, 175, 7, (50, 150))
player2 = Player('sirok.jpg', 580, 175, 7, (50, 150))
ball = Ball('gym_teacher.jpg', 150, 225, 3, (50, 50))


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

        ball.reset()
        ball.update()

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed_x *= -1

        if ball.rect.y > 450 or ball.rect.y < 0:
            ball.speed_y *= -1

        if ball.rect.x < 50:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > 650:
            finish = True
            window.blit(lose2, (200, 200))

        clock.tick(FPS)
        display.update()
