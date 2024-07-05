import commons
import vector
import images
import pygame
import entities  # Добавим этот импорт

from vector import Vector
from enum import Enum
from pygame.locals import *


class BallType(Enum):
    DEFAULT = 0


class Ball:
    def __init__(self, position: Vector, velocity: Vector = Vector(0, 0), radius: float = 8,
                 ball_type: BallType = BallType.DEFAULT, image: pygame.Surface = None):

        self.position = vector.copy(position)
        self.velocity = vector.copy(velocity)
        self.radius = radius
        self.diameter = radius * 2.0
        self.ball_type = BallType(ball_type)
        self.image = image if image else images.ball_default
        self.bounding_box = Rect(0, 0, 1, 1)
        self.alive = True

    def update(self):
        self.velocity.y += commons.delta_time * commons.gravity
        self.position += self.velocity * commons.delta_time
        self.check_screen_collisions()
        self.check_peg_collisions()

    def draw(self):
        top_left_position = self.position - self.radius
        commons.screen.blit(self.image, top_left_position.make_int_tuple())

    def check_screen_collisions(self):
        if self.position.x < self.radius or self.position.x > commons.screen_w - self.radius:
            self.velocity.x = -self.velocity.x
        if self.position.y < self.radius:
            self.velocity.y = -self.velocity.y
        elif self.position.y > commons.screen_h + self.radius:
            self.alive = False

    def check_peg_collisions(self):
        for peg in entities.pegs:
            if peg.check_collision(self):
                self.velocity = vector.reflect(self.velocity, vector.normalize(self.position - peg.position))
                peg.alive = False
                commons.score += peg.score