from omega_pygame.core.pygame_api import pygame


class Canvas(pygame.Surface):
    def __init__(self, width, height):
        super().__init__((width, height))

    def override_surface(self, surface):
        surf_rect = surface.get_rect()
        super(Canvas, self).__init__(surf_rect.size, masks=pygame.mask.from_surface(surface))

    @property
    def array2d(self):
        return pygame.surfarray.array2d(self)

    def blit_array(self, array):
        pygame.surfarray.blit_array(self, array)

    def _resize(self, width, height):
        super(Canvas, self).__init__((width, height))

