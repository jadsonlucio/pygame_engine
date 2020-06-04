from omega_pygame.core.pygame_api import pygame
from .entity_base.canvas_entity import CanvasEntity
from omega_pygame.core.base.event import set_custom_events


class Window(CanvasEntity):
    def __init__(self, title, width, height, posX, posY, mode=pygame.DOUBLEBUF | pygame.RESIZABLE):
        self._running = False
        self.title = title
        self._display_surf = pygame.display.set_mode((width, height), mode)

        super().__init__(self._display_surf, posX, posY, width, height)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_execute(self):
        self._running = True
        while self._running:
            set_custom_events()
            events = pygame.event.get()
            self._update(events)

        self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()

    def on_init(self):
        pygame.init()
        self.fill((0, 0, 0))

    def on_render(self):
        pygame.display.flip()

    def window_resize(self, event):
        self.master = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
        self.rect.width, self.rect.height = event.size
