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

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5
enemies = [enemy_pos]

enemy_img = pygame.image.load('images/glass_of_milk_s.png')
enemy_rect = enemy_img.get_rect()

# Функция отрисовки объектов
def draw_objects():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, (cracker_pos[0], cracker_pos[1], cracker_size, cracker_size))

    for enemy in enemies:
        pygame.draw.rect(WIN, BLACK, (enemy[0], enemy[1], enemy_size, enemy_size))

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and cracker_pos[0] - cracker_speed > 0:
        cracker_pos[0] -= cracker_speed
    if keys[pygame.K_RIGHT] and cracker_pos[0] + cracker_size + cracker_speed < WIDTH:
        cracker_pos[0] += cracker_speed

    for enemy in enemies:
        if enemy[1] < HEIGHT:
            enemy[1] += enemy_speed
        else:
            enemy[0] = random.randint(0, WIDTH - enemy_size)
            enemy[1] = 0
        if enemy[1] + enemy_size > cracker_pos[1] and cracker_pos[0] < enemy[0] + enemy_size and cracker_pos[0] + cracker_size > enemy[0]:
            enemies.remove(enemy)

    draw_objects()
    pygame.display.update()

pygame.quit()