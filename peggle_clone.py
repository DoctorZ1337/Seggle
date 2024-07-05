import commons
import pygame
import vector
import states
import entities
from vector import Vector
from states import GameState, MenuState, PlayState
from ball import Ball
from peg import Peg

def update():
    entities.update_balls()

def draw():
    commons.screen.fill((50, 50, 50))
    entities.draw_pegs()
    entities.draw_balls()
    draw_score()

def draw_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {commons.score}', True, (255, 255, 255))
    commons.screen.blit(text, (20, 20))

pygame.init()
commons.screen = pygame.display.set_mode((commons.screen_w, commons.screen_h))
pygame.display.set_caption("Peggle Clone")

icon_image = pygame.image.load("res/images/icons/ball.png").convert_alpha()
icon_image.set_colorkey((255, 0, 255))
pygame.display.set_icon(icon_image)

# Создаем мишени
for i in range(20):
    color = 'blue' if i % 2 == 0 else 'orange'
    entities.pegs.append(Peg(Vector(i * 100 + 100, 300), color=color))
    entities.pegs.append(Peg(Vector(i * 200 + 200, 400), color=color))
    entities.pegs.append(Peg(Vector(i * 100 + 100, 500), color=color))
    entities.pegs.append(Peg(Vector(i * 200 + 200, 600), color=color))

app_running = True
delta_time = 0.0
clock = pygame.time.Clock()
mouse_position = (0, 0)

while app_running:
    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                app_running = False
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                entities.balls.append(Ball(Vector(event.pos[0], event.pos[1]), vector.random_vector() * 300))

    update()
    draw()
    pygame.display.flip()
    commons.delta_time = 0.001 * clock.tick(144)

pygame.quit()