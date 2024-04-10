import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Crossy Road")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Игровые параметры
cracker_size = 50
cracker_pos = [WIDTH // 2, HEIGHT - cracker_size * 2]
cracker_speed = 10

cracker_img = pygame.image.load('images/cracker_s.png')
cracker_rect = cracker_img.get_rect()
cracker_rect.x = WIDTH // 2
cracker_rect.y = HEIGHT - cracker_size * 2

enemy_size = 50
enemy_speed = 5
enemy_img = pygame.image.load('images/glass_of_milk_s.png')
enemy_rect = enemy_img.get_rect()
enemy_rect.x = random.randint(0, WIDTH - enemy_size)
enemy_rect.y = 0
enemies = [enemy_rect.x, enemy_rect.y]

bg_image = pygame.image.load('images/cracker_bg_01_s.jpg')

# Функция отрисовки объектов
def draw_objects():
    WIN.blit(bg_image, (0, 0))

    WIN.blit(cracker_img, cracker_rect)

    for enemy in enemies:
        WIN.blit(enemy_img, enemy_rect)

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    # Отображение фоновой картинки

    clock.tick(30)

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
        if enemy_rect.y < HEIGHT:
            enemy_rect.y += enemy_speed
        else:
            enemy_rect.x = random.randint(0, WIDTH - enemy_size)
            enemy_rect.y = 0
        if enemy_rect.y + enemy_size > cracker_rect.y and cracker_rect.x < enemy_rect.x + enemy_size and cracker_rect.x + cracker_size > enemy_rect.x:
            enemies.remove(enemy)

    draw_objects()
    pygame.display.update()

pygame.quit()