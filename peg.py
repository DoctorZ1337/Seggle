import vector
import commons
import images
from vector import Vector

class Peg:
    def __init__(self, position: Vector, radius: float = 10, color='blue'):
        self.position = vector.copy(position)
        self.radius = radius
        self.alive = True
        self.color = color
        if color == 'blue':
            self.image = images.peg_blue_image
            self.score = 500
        elif color == 'orange':
            self.image = images.peg_orange_image
            self.score = 1000

    def draw(self):
        top_left_position = self.position - self.radius
        commons.screen.blit(self.image, top_left_position.make_int_tuple())

    def check_collision(self, ball):
        distance = vector.dist(self.position, ball.position)
        if distance < self.radius + ball.radius:
            return True
        return False