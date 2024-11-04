import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    _ = pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pg.time.Clock()
    dt = 0

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    _ = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((100, 100, 100))
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.collides_with(player):
                print("Game Over")
                return
            for s in shots:
                if a.collides_with(s):
                    a.split()
        for d in drawable:
            d.draw(screen)
        pg.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
