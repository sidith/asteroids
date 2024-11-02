import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    print("Starting asteroids!")
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill((100, 100, 100))
        pg.display.flip()


if __name__ == "__main__":
    main()
