import time
import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Crossy Road")
life = 1
font = pygame.font.Font(None, 28)

class Enemy:
    def __init__(self, size, speed, path, x, y):
        self.size = size
        self.speed = speed
        self.img = pygame.image.load(path)
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(x, WIDTH - self.size)
        self.rect.y = y

# Игровые параметры
cracker_size = 50
cracker_pos = [WIDTH // 2, HEIGHT - cracker_size * 2]
cracker_speed = 10

cracker_img = pygame.image.load('images/cracker_s.png')
cracker_rect = cracker_img.get_rect()
cracker_rect.x = WIDTH // 2
cracker_rect.y = HEIGHT - cracker_size * 2

enemy_coffee = Enemy(50, 5, 'images/glass_of_coffee_s.png', 200, 0)
enemy_milk = Enemy(50, 7, 'images/glass_of_milk_s.png', 300, 0)
enemy_tea = Enemy(50, 10, 'images/glass_of_tea_s.png', 400, 0)
enemy_water = Enemy(50, 15, 'images/glass_of_water_s.png', 500, 0)

enemies = [enemy_coffee, enemy_milk, enemy_tea, enemy_water]

bg_image = pygame.image.load('images/cracker_bg_01_s.jpg')


# Основной игровой цикл
clock = pygame.time.Clock()
running = True
start_time = pygame.time.get_ticks()
target_timer = 0

# Функция отрисовки объектов
def draw_objects():
    WIN.blit(bg_image, (0, 0))
    WIN.blit(cracker_img, cracker_rect)

    for enemy in enemies:
        WIN.blit(enemy.img, enemy.rect)

    text_score = font.render("life: " + str(life), True, (255, 255, 255))
    WIN.blit(text_score, (10, 10))
    text_time = font.render("Time: " + "{:.2f}".format(target_timer/1000), True, (255, 255, 255))
    WIN.blit(text_time, (600, 10))

while running:
    # Отображение фоновой картинки

    clock.tick(30)
    target_timer = pygame.time.get_ticks() - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and cracker_rect.x - cracker_speed > 0:
        cracker_rect.x -= cracker_speed
    if keys[pygame.K_RIGHT] and cracker_rect.x + cracker_size + cracker_speed < WIDTH:
        cracker_rect.x += cracker_speed
    if keys[pygame.K_UP] and cracker_rect.y - cracker_speed > 0:
        cracker_rect.y -= cracker_speed
    if keys[pygame.K_DOWN] and cracker_rect.y + cracker_size + cracker_speed < WIDTH:
        cracker_rect.y += cracker_speed

    for enemy in enemies:
        if enemy.rect.x < WIDTH:
            enemy.rect.x += enemy.speed
        else:
            enemy.rect.y = random.randint(0, WIDTH - enemy.size)
            enemy.rect.x = 0
        # if enemy.rect.y + enemy.size > cracker_rect.y and cracker_rect.x < enemy.rect.x + enemy.size and cracker_rect.x + cracker_size > enemy.rect.x:
        #    enemies.remove(enemy)
        if enemy.rect.colliderect(cracker_rect):
            life =- 1
            if life < 0:
                print(f"End! Time: " + "{:.2f}".format(target_timer/1000))
                time.sleep(10)
            else:
                text_score = font.render("life: " + str(life), True, (255, 255, 255))
                WIN.blit(text_score, (10, 10))
            enemies.remove(enemy)

    draw_objects()
    pygame.display.update()

pygame.quit()