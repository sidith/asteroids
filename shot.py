from circleshape import CircleShape
import pygame as pg


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 5)

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255),
                       self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
