import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/42648.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения прицела
cursor_img = pygame.image.load("img/cursor.png")
pygame.mouse.set_visible(False)  # Скрываем системный курсор мыши

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target_speed_x = 2  # Скорость по оси X
target_speed_y = 2  # Скорость по оси Y

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменная для подсчета попаданий
hits = 0

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_speed_x = -target_speed_x  # Изменение направления движения по оси X
                target_speed_y = -target_speed_y  # Изменение направления движения по оси Y
                hits += 1  # Увеличиваем счетчик попаданий

    # Обработка столкновений с границами окна
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Обновление координат цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Отрисовка цели
    screen.blit(target_img, (target_x, target_y))

    # Отрисовка курсора мыши (прицела)
    screen.blit(cursor_img, pygame.mouse.get_pos())

    # Отрисовка счетчика попаданий
    text = font.render("Попаданий: " + str(hits), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()

    pygame.time.delay(10)  # Задержка движения цели

pygame.quit()
