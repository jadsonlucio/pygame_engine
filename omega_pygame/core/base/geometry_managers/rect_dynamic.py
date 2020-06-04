def relative_value(value, percentage):
    if isinstance(percentage, int):
        return percentage
    else:
        return int(value * percentage)


class DynamicRect:
    def __init__(self, center_in=False):
        self.center_in = center_in

    def __call__(self, rect):
        if rect.master_rect is not None:
            pixel_posx = relative_value(rect.master_rect.pixel_posx, rect.posx)
            pixel_posy = relative_value(rect.master_rect.pixel_posy, rect.posy)
            pixel_width = relative_value(rect.master_rect.pixel_width, rect.width)
            pixel_height = relative_value(rect.master_rect.pixel_height, rect.height)
        else:
            pixel_posx = rect.posx
            pixel_posy = rect.posy
            pixel_width = rect.width
            pixel_height = rect.height

        # print(pixel_posx, pixel_posy, pixel_width, pixel_height)

        return pixel_posx, pixel_posy, pixel_width, pixel_height
