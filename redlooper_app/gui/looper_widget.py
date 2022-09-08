from enum import Enum

import pygame

from redlooper_app.gui.widgets import TimerWidget


class LooperWidget(TimerWidget):
    class Mode(Enum):
        PLAYING = 0
        RECORDING = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_loop_position(self, loop_position_s):
        self.set_time_elapsed(loop_position_s)

    def set_loop_length(self, loop_length_s):
        self.set_duration(loop_length_s)

    def set_mode(self, mode):
        pass

    def draw(self):
        self.surface.fill((0, 0, 0))
        super().draw()

    def run(self, framerate):
        fpsClock = pygame.time.Clock()
        while True:
            self.draw()
            pygame.display.update()
            fpsClock.tick(framerate)
