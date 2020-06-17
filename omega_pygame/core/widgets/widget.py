from ..base.entity_base.canvas_entity import CanvasEntity


class Widget(CanvasEntity):
    def __init__(self, master, posx, posy, width, height):
        super().__init__(master, posx, posy, width, height)
