import numpy as np


class Rect:
    def __init__(self, master_rect, posx, posy, width, height, geometry_manager):
        self.master_rect = master_rect
        self.geometry_manager = geometry_manager

        self._posx = posx
        self._posy = posy
        self._width = width
        self._height = height

        posx, posy, width, height = self.geometry_manager(self)

        self._pixel_posx = posx
        self._pixel_posy = posy
        self._pixel_width = width
        self._pixel_height = height

        self.childrens = []

        if isinstance(master_rect, Rect):
            master_rect.childrens.append(self)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._update()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._update()

    @property
    def posx(self):
        return self._posx

    @posx.setter
    def posx(self, value):
        self._posx = value
        self._update()

    @property
    def posy(self):
        return self._posy

    @posy.setter
    def posy(self, value):
        self._posy = value
        self._update()

    @property
    def pixel_width(self):
        return self._pixel_width

    @property
    def pixel_height(self):
        return self._pixel_height

    @property
    def pixel_posx(self):
        return self._pixel_posx

    @property
    def pixel_posy(self):
        return self._pixel_posy

    @property
    def pos(self):
        return np.array([self.pixel_posx, self.pixel_posy])

    @property
    def size(self):
        return np.array([self.pixel_width, self.pixel_height])

    def abspos(self):
        if isinstance(self.master_rect, Rect):
            return np.array([self.master_rect.abspos + self.pos])
        else:
            return self.pos

    def point_in(self, x, y):
        pixel_posx, pixel_posy = self.pixel_posx, self.pixel_posy
        pixel_width, pixel_height = self._pixel_width, self.pixel_height
        return (pixel_posx + pixel_width) >= x >= pixel_posx and (pixel_posy + pixel_height) >= y >= pixel_posy

    def _update(self):
        posx, posy, width, height = self.geometry_manager(self)
        self._pixel_posx = posx
        self._pixel_posy = posy
        self._pixel_width = width
        self._pixel_height = height
        self._update_childrens()

    def _update_childrens(self):
        for children in self.childrens:
            children._update()
