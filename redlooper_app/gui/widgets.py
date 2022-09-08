import math
from typing import Tuple

import pygame


class ArcSegmentLoadingBar:
    def __init__(self, surface, color, center: Tuple[int, int], radius: int, linewidth: int):
        print(color)
        self.surface = surface
        self.color = color
        self.radius = radius
        self.angle = 0
        self.linewidth = linewidth
        self.loading_fraction = 0

        self._bounding_box = (0, 0, 0, 0)
        self._angle_start = 0
        self._angle_end = 0
        self._filling = True

        self.set_center(center[0], center[1])

    def set_loading_percentage(self, loading_fraction):
        if loading_fraction < self.loading_fraction:
            self._filling = not self._filling  # change from filling to emptying or vice-versa
        self.loading_fraction = loading_fraction

        angle = loading_fraction * 2 * math.pi

        if self._filling:
            self._angle_start = math.pi - angle
            self._angle_end = math.pi
        elif self.loading_fraction > 0:
            self._angle_start = math.pi
            self._angle_end = math.pi - angle
        else:
            self._angle_start = 0
            self._angle_end = 2 * math.pi

    def draw(self):
        pygame.draw.arc(self.surface, self.color, self._bounding_box, self._angle_start, self._angle_end,
                        self.linewidth)

    def set_center(self, x, y):
        self._bounding_box = (x - self.radius, y - self.radius, 2 * self.radius, 2 * self.radius)


class TimerWidget(ArcSegmentLoadingBar):
    def __init__(self, surface, color, center: Tuple[int, int], radius: int, linewidth: int, duration_s=0,
                 counting_mode='up'):
        super().__init__(surface, color, center, radius, linewidth)
        self.duration_s = duration_s
        self.counting_mode = counting_mode

        if counting_mode == 'up':
            self.time_elapsed_s = 0
        else:
            self.time_elapsed_s = self.duration_s

        self.font = pygame.font.SysFont(None, 48)
        self.sysfont = pygame.font.get_default_font()

    def set_time_elapsed(self, time_s):
        self.time_elapsed_s = time_s

        if self.duration_s == 0:
            loading_fraction = 0
        elif self.counting_mode == 'up':
            loading_fraction = self.time_elapsed_s / self.duration_s
        else:
            loading_fraction = (self.duration_s - self.time_elapsed_s) / self.duration_s

        self.set_loading_percentage(loading_fraction)

    def set_duration(self, duration_s):
        self.duration_s = duration_s

    def draw(self):
        time_str = self.time_to_string(self.time_elapsed_s)
        text = self.font.render(time_str, True, (255, 255, 255))

        self.surface.blit(text, (100, 100))
        super().draw()

    @staticmethod
    def time_to_string(time_s) -> str:
        return f'{int(time_s / 60):02d}:{int(time_s % 60):02d}.{int(time_s*100 % 100):02d}'
