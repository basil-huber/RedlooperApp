from enum import Enum

import pygame

from redlooper_app.gui.widgets import TimerWidget


class State(Enum):
    PAUSED = 0
    PLAYING = 1
    RECORDING = 2


class LooperWidget(TimerWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = State.PAUSED

    def set_loop_position(self, loop_position_s):
        self.set_time_elapsed(loop_position_s)

    def set_loop_length(self, loop_length_s):
        self.set_duration(loop_length_s)

    def set_state(self, state: State):
        self.state = state

    def draw(self):
        self.surface.fill((0, 0, 0))

        symbol_center = (self._bounding_box[0] - 10, self._bounding_box[1] - 10)
        if self.state == State.RECORDING:
            pygame.draw.circle(self.surface, (255, 0, 0), symbol_center, 10)
        elif self.state == State.PLAYING:
            pygame.draw.polygon(self.surface, (0, 255, 0), [(symbol_center[0]-10, symbol_center[1]-8) ,(symbol_center[0]-10, symbol_center[1]+8), (symbol_center[0]+10, symbol_center[1])])
        else:
            pygame.draw.rect(self.surface, (255, 255, 255), (symbol_center[0]-10, symbol_center[1]-10, 5, 20))
            pygame.draw.rect(self.surface, (255, 255, 255), (symbol_center[0] + 5, symbol_center[1] - 10, 5, 20))

        super().draw()

    def run(self, framerate):
        fpsClock = pygame.time.Clock()
        while True:
            self.draw()
            pygame.display.update()
            fpsClock.tick(framerate)
