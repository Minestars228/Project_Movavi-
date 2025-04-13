import pygame

import random

pygame.init()

print('Мой проект "Космический защитник"')
print('>> Вражеские корабли летят сверху, игрок стреляет в них (одна кнопка – выстрел).\n>> За каждое попадание +5 очков.')

score = 0
space = 0
live = 3
base_live = 3

def move_player():
    speed = 15
    keys = pygame.key.get_pressed()
    if player.rect.left > 0 and keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.rect.x -= speed
    if player.rect.right < SCREEN_WIDTH and keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.rect.x += speed

def move_alien():
    speed = 5
    for m in aliens:
        m.rect.y += speed
        if m.rect.top > SCREEN_HEIGHT:
            m.rect.x = random.randint(0, SCREEN_WIDTH - m.rect.width)
            m.rect.y = random.randint(-1000 , -100)

def check_collide_aliens():
    for m in aliens:
        if pygame.sprite.collide_mask(player , m):
            return m
    return None

def shot():
    bullet = pygame.sprite.Sprite(bullets, all_sprite)
    bullet.image = bullet_image
    bullet.rect: pygame.Rect = bullet.image.get_rect()
    bullet.rect.y = player.rect.y
    bullet.rect.x = player.rect.x

def move_bullet():
    speed = 20
    for b in bullets:
        b.rect.y -= speed


def check_collide_shot():
    global score
    res = pygame.sprite.groupcollide(aliens, bullets,False,False, collided=pygame.sprite.collide_mask)
    if res:
        score += 5
    return res

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 900
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()


player = pygame.sprite.Sprite(all_sprite)
player.image = pygame.image.load('./imgs/player_2.png')
player.rect: pygame.Rect = player.image.get_rect()

player.rect.centerx = SCREEN_WIDTH // 2
player.rect.centery = SCREEN_WIDTH // 2

bullet_image = pygame.image.load('./imgs/bullet.png')

for i in range(1,4):
    m = pygame.sprite.Sprite(all_sprite, aliens)
    m.image = pygame.image.load(f'./imgs/alien_{i}.png')
    m.rect = m.image.get_rect()
    m.rect.top = 5000

font_object_1 = pygame.font.SysFont('Arial', 50)
text = font_object_1.render(f"Счет: {score}", False, 'white')

font_object_2 = pygame.font.SysFont('Arial', 200)
GameOver = font_object_2.render(f"Game Over", False, 'white')

font_object_3 = pygame.font.SysFont('Arial', 50)
lives = font_object_3.render(f"Жизни: {live}", False, 'white')

run = True
game_end = False
while run:

    screen.fill((0, 0, 64))

    lives = font_object_3.render(f"Жизни: {live}", False, 'white')

    screen.blit(text , (10 , 0))
    screen.blit(lives , (10 , 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space += 1
            if event.key == pygame.K_f:
                if score >= 15:
                    live += 1
                    score -= 15
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                shot()

    move_bullet()
    if live <= 0:
        game_end = True
    if not game_end:
        if space % 2 == 0:
            move_player()
            move_alien()
        m = check_collide_aliens()
        l = check_collide_shot()
        if m:
            m.rect.centery = 5000
            live -= 1
        if l:
            l.rect.centery = 5000
    
        all_sprite.draw(screen)
    else:
        screen.fill('black')
        screen.blit(GameOver , (300 , 100))

    pygame.display.update()
    font_object = pygame.font.SysFont('Arial', 50)
    text = font_object.render(f"Счет: {score}", False, 'white')
    clock.tick(60)
pygame.quit()