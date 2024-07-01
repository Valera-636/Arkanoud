import pygame
import sys
import random

pygame.init()

# Настройка окна

size = dlina, visota = 900, 900
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pygame by Valeria')

# Настройка квадрата

square_color = (15, 247, 220)
square_position = [450, 450] # x, y
square_size = 50
square_speed = 1

x1 = random.randint(50, 850)
y1 = random.randint(50, 850)
square1_color = (171, 65, 32)
square1_position = [x1, y1] # x, y
square1_size = 60

x2 = random.randint(50, 850)
y2 = random.randint(50, 850)
square2_color = (171, 65, 32)
square2_position = [x2, y2] # x, y
square2_size = 40

x3 = random.randint(50, 850)
y3 = random.randint(50, 850)
square3_color = (171, 65, 32)
square3_position = [x3, y3] # x, y
square3_size = 30

# Основные настройки программы

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Обработка клавиш

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        square_position[0] -= square_speed
    if keys[pygame.K_d]:
        square_position[0] += square_speed
    if keys[pygame.K_w]:
        square_position[1] -= square_speed
    if keys[pygame.K_s]:
        square_position[1] += square_speed

    screen.fill( (50, 64, 62) )
    pygame.draw.rect(screen, square_color, (*square_position, square_size, square_size))
    pygame.draw.rect(screen, square1_color, (*square1_position, square1_size, square1_size))
    pygame.draw.rect(screen, square2_color, (*square2_position, square2_size, square2_size))
    pygame.draw.rect(screen, square3_color, (*square3_position, square3_size, square3_size))
    pygame.display.flip()


pygame.quit()
sys.exit()





