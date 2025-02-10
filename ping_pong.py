from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < window_height - 80:
            self.rect.y += self.speed

background_color = (160, 255, 255)
window_height = 500
window_width = 600
window = display.set_mode((window_width, window_height))
window.fill(background_color)

game = True
finish = False
clock = time.Clock()
fps = 60

player_left = Player('a3.png', 30, 200, 4, 50, 150)
player_right = Player('a3.png', 520, 200, 4, 50, 150)
ball = GameSprite('a2.png', 200, 200, 4, 50, 50)

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 Loses', True, (255, 255, 255))
lose2 = font1.render('Player 2 Loses', True, (255, 255, 255))

speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(background_color)
        player_left.update_l()
        player_right.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_left, ball) or sprite.collide_rect(player_right, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > window_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = False
        if ball.rect.x > window_width:
            finish = True
            window.blit(lose2, (200, 200))
            game = False
        
        player_left.reset()
        player_right.reset()
        ball.reset()
    display.update()
    clock.tick(fps)