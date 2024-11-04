from shot import Shot
import pygame as pg
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.cooldown = PLAYER_SHOT_COOLDOWN
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

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pg.Vector2(0, 1)
        shot.velocity.rotate_ip(self.rotation)
        shot.velocity *= PLAYER_SHOT_SPEED

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
        if keys[pg.K_SPACE]:
            if self.cooldown >= PLAYER_SHOT_COOLDOWN:
                self.shoot()
                self.cooldown = 0

        self.cooldown += dt

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
