import pygame
import sys

pygame.init()
pygame.font.init()

# Экран
size = dlina, visota = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pygame by Valeria')

# Игрок
square_color = (15, 247, 220)
square_size = dlina1, visota1 = 60, 15
square_speed = 5
square = pygame.Rect(10, visota - 50, dlina1, visota1)

# Мяч
mat_color = (255, 255, 255)
mat_x = visota // 2
mat_y = dlina // 2
mat_size = 10
mat_speed_y = 4
mat_speed_x = - 4
mat = pygame.Rect(mat_x, mat_y, mat_size, mat_size)
# жизнь, очки
life = 3
ok = 0

# Кирпичи
kurpnth_1_color = (214, 114, 47)
kurpnth_size_x = 30
kurpnth_size_y = 10
kurpnth_x = 15
kurpnth_y = 5
onstyp = 3
list_kur = []
for y in range(kurpnth_y):
    for x in range(kurpnth_x):
        x_cor = x * (kurpnth_size_x + onstyp) + onstyp
        y_cor = y * (kurpnth_size_y + onstyp) + onstyp
        otr = pygame.Rect(x_cor, y_cor, kurpnth_size_x, kurpnth_size_y)
        list_kur.append(otr)


def draw_text(place, text, size, x, y):
    font = pygame.font.Font('arial.ttf', size)
    text_place = font.render(text, True, (250,250,250))
    text_rect = text_place.get_rect()
    text_rect.midtop = (x, y)
    place.blit(text_place, text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Мяч
    mat.y += mat_speed_y
    mat.x += mat_speed_x


    # Экран, платформа, мяч
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, square_color, square)
    pygame.draw.ellipse(screen, mat_color, mat)
    for i in list_kur:
        pygame.draw.rect(screen, kurpnth_1_color, i)

    # Отрисовка жизней
    draw_text(screen, 'Жизни: ' + str(life), 18, (dlina // 2), visota - 50)
    draw_text(screen, "Очки: " + str(ok), 18, (dlina // 2), 200)

    pygame.display.flip()

    # Обработка клавиш

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        square[0] -= square_speed
        if square[0] <= 0:
            square[0] = visota - 10
    if keys[pygame.K_d]:
        square[0] += square_speed
        if square[0] >= visota:
            square[0] = 20

    if mat.colliderect(square):
        mat_speed_y = - mat_speed_y


    # кирпичи
    for i in list_kur:
        if mat.colliderect(i):
            mat_speed_y = - mat_speed_y
            list_kur.remove(i)
            ok += 1
            break

    # Движение мяча
    if mat.left <= 0 or mat.right >= dlina:
        mat_speed_x = - mat_speed_x
    if mat.top <= 0:
        mat_speed_y = - mat_speed_y
    if mat.bottom >= visota:
        mat.y = visota // 2
        mat.x = dlina // 2
        life -= 1
        if life == 0:
            life = 'Игра окончена'
            mat_speed_x = 0
            mat_speed_y = 0



    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()