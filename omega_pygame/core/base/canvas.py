from omega_pygame.core.pygame_api import pygame


class Canvas(pygame.Surface):
    def __init__(self, width, height):
        super().__init__((width, height))

    def override_surface(self, surface):
        surf_rect = surface.get_rect()
        width, height = surf_rect.size
        # self._resize(width, height)
        self.blit(surface, (0, 0))

    @property
    def array2d(self):
        return pygame.surfarray.array2d(self)

    def blit_array(self, array):
        pygame.surfarray.blit_array(self, array)

    def draw_line(self, x0, y0, x1, y1, color, width=1):
        pygame.draw.line(self, color, (x0, y0), (x1, y1), width)

    def draw_rect(self, x, y, width, height, color, fill=0):
        pygame.draw.rect(self, color, (x, y, width, height), fill)

    def _resize(self, width, height):
        super(Canvas, self).__init__((width, height))

