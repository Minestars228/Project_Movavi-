import pygame

import random

pygame.init()

sho = 0
score = 0
space = 0
live = 3
base_live = 3

def start():
    global run1
    run1 = True
    while run1:
        screen.fill((0, 0, 0))
        screen.blit(start1 , (10 , 60))
        screen.blit(start2 , (10 , 120))
        screen.blit(start3 , (10 , 180))
        screen.blit(start4 , (10 , 240))
        screen.blit(start5 , (10 , 300))
        screen.blit(start6 , (10 , 360))
        screen.blit(start7 , (10 , 420))
        screen.blit(start8 , (10 , 480))
        screen.blit(start9 , (175 , 600))
        for event in pygame.event.get():    
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        run1 = False
        pygame.display.update()
        clock.tick(60)


def move_player():
    speed = 15
    keys = pygame.key.get_pressed()
    if player.rect.left > 0 and keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.rect.x -= speed
    if player.rect.right < SCREEN_WIDTH and keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.rect.x += speed

def move_alien():
    global live
    speed = 4
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
    global sho
    bullet = pygame.sprite.Sprite(bullets, all_sprite)
    bullet.image = bullet_image
    bullet.rect: pygame.Rect = bullet.image.get_rect()
    if sho == 0:
        bullet.rect.y = player.rect.y
        bullet.rect.x = player.rect.x
    elif sho == 1:
        bullet.rect.y = player.rect.top
        bullet.rect.x = player.rect.right - 20


def move_bullet():
    speed = 20
    for b in bullets:
        b.rect.y -= speed
        if b.rect.bottom < 0:
            b.kill()


def check_collide_shot():
    for m in aliens:
        for b in bullets:
            if pygame.sprite.collide_mask(m, b):
                b.kill()
                return m
    return None

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 900
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()


player = pygame.sprite.Sprite(all_sprite)
player.image = pygame.image.load(f'./imgs/player_{random.randint(2,3)}.png')
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

font_object_4 = pygame.font.SysFont('Arial', 50)
start1 = font_object_4.render(f'Мой проект "Космический защитник"', False, 'white')

font_object_5 = pygame.font.SysFont('Arial', 40)
start2 = font_object_5.render(f'>> Вражеские корабли летят сверху, игрок стреляет в них (одна кнопка – выстрел)', False, 'white')

font_object_6 = pygame.font.SysFont('Arial', 40)
start3 = font_object_6.render(f'>> За каждое попадание +5 очков', False, 'white')

font_object_7 = pygame.font.SysFont('Arial', 50)
start4 = font_object_7.render(f'Как Играть:', False, 'white')

font_object_8 = pygame.font.SysFont('Arial', 40)
start5 = font_object_8.render(f'>> Выстрел "ЛКМ"', False, 'white')

font_object_9 = pygame.font.SysFont('Arial', 40)
start6 = font_object_9.render(f'>> Купить жизнь "E"(ПРИ НАЛИЧИИ 15 ОЧКОВ)', False, 'white')

font_object_10 = pygame.font.SysFont('Arial', 40)
start7 = font_object_10.render(f'>> Пауза "Space"(пробел)', False, 'white')

font_object_11 = pygame.font.SysFont('Arial', 40)
start8 = font_object_11.render(f'>> Если умер можно начать заново на "T"', False, 'white')

font_object_12 = pygame.font.SysFont('Arial', 75)
start9 = font_object_12.render(f'>>Что бы начать игру нажмите "ЛКМ"<<', False, 'white')

run = True
game_end = False
start()
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
            if event.key == pygame.K_e:
                if score >= 15:
                    live += 1
                    score -= 15
            if event.key == pygame.K_t:
                game_end = False
                live = 3
                score = 0  
                pygame.display.update()  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                shot()
                if sho == 0:
                    sho = 1
                elif sho == 1:
                    sho = 0


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
            score += 5
    
        all_sprite.draw(screen)
    else:
        screen.fill('black')
        screen.blit(GameOver , (300 , 100))

    pygame.display.update()
    font_object = pygame.font.SysFont('Arial', 50)
    text = font_object.render(f"Счет: {score}", False, 'white')
    clock.tick(60)
pygame.quit()
