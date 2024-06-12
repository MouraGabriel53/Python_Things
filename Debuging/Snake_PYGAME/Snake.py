# pip install pygame

import pygame
import time
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
width, height = 700, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
Yellow = (255, 255, 0)
Blue = (0, 0, 255)
Green = (0, 128, 0)

# Parâmetros do jogo
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

# Fontes
font_style = pygame.font.SysFont(None, 35)

def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [x, y])

def gameLoop():
    game_over = False
    x, y = width // 2, height // 2
    dx, dy = 0, 0
    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block

        x += dx
        y += dy

        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        win.fill(Yellow)
        pygame.draw.rect(win, Green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        for block in snake_list:
            pygame.draw.rect(win, Blue, [block[0], block[1], snake_block, snake_block])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    message("Você perdeu! Pressione Q para sair ou R para reiniciar", Green, width // 25, height // 2)
    pygame.display.update()
    time.sleep(2)

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = False
                if event.key == pygame.K_r:
                    gameLoop()

    pygame.quit()

gameLoop()