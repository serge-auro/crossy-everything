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
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size * 2]
player_speed = 10

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5
enemies = [enemy_pos]

# Функция отрисовки объектов
def draw_objects():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, (player_pos[0], player_pos[1], player_size, player_size))

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
    if keys[pygame.K_LEFT] and player_pos[0] - player_speed > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] + player_size + player_speed < WIDTH:
        player_pos[0] += player_speed

    for enemy in enemies:
        if enemy[1] < HEIGHT:
            enemy[1] += enemy_speed
        else:
            enemy[0] = random.randint(0, WIDTH - enemy_size)
            enemy[1] = 0
        if enemy[1] + enemy_size > player_pos[1] and player_pos[0] < enemy[0] + enemy_size and player_pos[0] + player_size > enemy[0]:
            enemies.remove(enemy)

    draw_objects()
    pygame.display.update()

pygame.quit()