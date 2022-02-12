from pygame import *
from random import randint

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIDTH - 80:
            self.rect.x += self.speed

    def fire(self):
        pass


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > HEIGHT:
            self.rect.x = randint(80, WIDTH - 80)
            self.rect.y = 0
            lost = lost + 1


WIDTH = 700
HEIGHT = 500
display.set_caption("Shooter")
window = display.set_mode((WIDTH, HEIGHT))
background = transform.scale(image.load('galaxy.jpg'), (WIDTH, HEIGHT))

ship = Player('rocket.png', 5, HEIGHT - 100, 80, 100, 10)

lost = 0
font1 = font.Font(None, 38)
counter = font1.render('Пропущено врагов:' + str(lost), True, (204, 0, 0))

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, WIDTH - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0))

        ship.update()
        monsters.update()
        ship.reset()
        monsters.draw(window)

        counter = font1.render('Пропущено врагов:' + str(lost), True, (204, 0, 0))
        window.blit(counter, (0, 0))

        display.update()
    time.delay(50)