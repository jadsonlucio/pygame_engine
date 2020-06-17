from .widget import Widget


class Frame(Widget):
    def __init__(self, master, posx, posy, width, height, background_color):
        self.background_color = background_color
        super().__init__(master, posx, posy, width, height)

    def on_init(self):
        self.fill(self.background_color)
