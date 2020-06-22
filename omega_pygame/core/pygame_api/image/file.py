from omega_pygame.core.pygame_api import pygame


def load_image(img_path):
    return pygame.image.load(img_path)


def save_image(surface, img_path):
    pygame.image.save(surface, img_path)


__all__ = ["load_image", "save_image"]
