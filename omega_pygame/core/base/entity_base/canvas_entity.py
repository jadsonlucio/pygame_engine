from omega_pygame.core.pygame_api import pygame
from omega_pygame.core.base.canvas import Canvas
from omega_pygame.core.base.event.event_manager import Events

from .canvas_rect import Rect
from ..geometry_managers.rect_dynamic import DynamicRect


class CanvasEntity(Canvas):
    def __init__(self, master, posx, posy, width, height):
        self.master = master
        self.children = []
        self.events = Events(self)
        self.focus_on = False
        self.mouse_on = False

        master_rect = None
        if master is not None and issubclass(type(master), CanvasEntity):
            master_rect = master.rect
            self.master.children.append(self)

        self.rect = Rect(master_rect, posx, posy, width, height, DynamicRect())
        Canvas.__init__(self, self.rect.pixel_width, self.rect.pixel_height)

        self._on_init()

    def check_size(self):
        surf_width, surf_height = self.get_rect().size
        rect_width, rect_height = self.rect.size

        if surf_width != rect_width or surf_height != rect_height:
            self._resize(rect_width, rect_height)
            self.on_init()

    def on_init(self):
        pass

    def on_render(self):
        self.master.blit(self, self.rect.pos)

    def on_loop(self):
        self.check_size()

    def _resize(self, width, height):
        super()._resize(width, height)

    def window_resize(self, event):
        return event

    def mouse_over(self, event):
        return event

    def mouse_in(self, event):
        pass

    def mouse_out(self, event):
        pass

    def mouse_up(self, event):
        return event

    def mouse_down(self, event):
        return event

    def mouse_clicked(self, event):
        return event

    def mouse_moved(self, event):
        return event

    def mouse_hold(self, event):
        return event

    def key_pressed(self, event):
        return event

    def key_hold(self, event):
        return event

    def key_up(self, event):
        return event

    def key_down(self, event):
        return event

    def on_event(self, event):
        return event

    @property
    def is_mouse_over(self):
        x, y = pygame.mouse.get_pos()
        return self.rect.point_in(x, y)

    @property
    def size(self):
        return self.width, self.height

    def _update(self, events):
        events = self.events.process_events(events)
        class_list = self.__class__.mro()
        class_list.reverse()
        for class_obj in class_list:
            if issubclass(class_obj, CanvasEntity):
                class_obj.on_loop(self)
                class_obj.on_render(self)

        for child in self.children:
            if isinstance(child, CanvasEntity):
                child._update(events)

    def _on_init(self):
        for class_obj in self.__class__.mro():
            if issubclass(class_obj, CanvasEntity):
                class_obj.on_init(self)
