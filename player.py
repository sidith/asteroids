from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame as pg


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    def draw(self, screen):
        pg.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def move(self, dt):
        dir = pg.Vector2(0, 1)
        dir.rotate_ip(self.rotation)
        dir *= PLAYER_SPEED * dt
        self.position += dir

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_e]:  # up
            self.move(dt)
        if keys[pg.K_d]:  # down
            self.move(-dt)
        if keys[pg.K_s]:  # left
            self.rotate(-dt)
        if keys[pg.K_f]:  # right
            self.rotate(dt)

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
