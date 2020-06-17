import random
from omega_pygame.core.base.window import Window
from omega_pygame.core.widgets.frame import Frame
import logging


def mouse_out(block, event):
    block.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


def grid(window):
    for cont in range(100):
        x, y = cont % 10, cont//10
        background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        block = Frame(window, x*0.1, y*0.1, 0.1, 0.1, background_color)
        block.events.bind("mouse_over", mouse_out)


if __name__ == "__main__":
    logging.debug("Criando window")
    window = Window("teteste", 500, 500, 0, 0)
    logging.debug("window criada")
    logging.debug("Criando grid")
    grid(window)
    logging.debug("grid criado")
    # screen.bind("ds", key_pressed)
    window.on_execute()
