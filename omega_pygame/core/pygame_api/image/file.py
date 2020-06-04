from omega_pygame.core.pygame_api import pygame


def load_image(img_path):
    pygame.image.load(img_path)


__all__ = ["load_image"]