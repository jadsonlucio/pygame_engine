from .settings import __version__
from omega_pygame.core.base.window import Window
from omega_pygame.core.base.entity_base import CanvasEntity


def click(widget, event):
    widget.fill((255, 0, 0))


class Editor(Window):
    def __init__(self):
        super().__init__(f"Editor level v{__version__}", 1280, 720, 0, 0)
        self.options = CanvasEntity(self, 0, 0, 0.2, 1.0)
        self.options.fill((255, 255, 255))
        self.options.events.bind("mouse_over", click)

    def mouse_clicked(self, event):
        return event
