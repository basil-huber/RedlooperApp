import pygame

from redlooper_app.gui.looper_widget import LooperWidget

SCREEN_RES = (480, 320)
CENTER = (int(SCREEN_RES[0] / 2), int(SCREEN_RES[1] / 2))
FPS = 10


def main():

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_RES, 0, 32)
    lpw = LooperWidget(screen, color=(255,0,0), center=CENTER, radius=100, linewidth=20)
    print('running')
    lpw.run(FPS)


if __name__ == '__main__':
    main()
