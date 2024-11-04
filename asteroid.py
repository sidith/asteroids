from circleshape import CircleShape
import pygame as pg
import random
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255),
                       self.position, self.radius, 2)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("boom")
        else:
            theta = random.uniform(20, 50)
            alpha = self.velocity.rotate(theta)
            beta = self.velocity.rotate(-theta)
            new_rad = self.radius - ASTEROID_MIN_RADIUS

            aster_a = Asteroid(self.position.x, self.position.y, new_rad)
            aster_a.velocity = alpha * 1.2

            aster_b = Asteroid(self.position.x, self.position.y, new_rad)
            aster_b.velocity = beta * 1.2
        self.kill()

    def update(self, dt):
        self.position += self.velocity * dt
