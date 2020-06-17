from omega_pygame.core.base.entity_base import CanvasEntity
from omega_pygame.core.pygame_api.image import load_image


class Sprite(CanvasEntity):
    def __init__(self, surface, posx, posy, width, height, name=None):
        super().__init__(surface, posx, posy, width, height)
        self.name = name

    def __str__(self):
        return self.name

    def from_imgfile(self, img_path):
        surface_img = load_image(img_path)
        return Sprite(surface_img, surface_img.get_width(), surface_img.get_height())
