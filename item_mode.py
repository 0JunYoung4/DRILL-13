from pico2d import get_canvas_height, get_canvas_width, load_image


class ItemMode:
    def __init__(self):
        self.image = load_image('item_select.png')
        self.is_open = False

    def toggle(self):
        self.is_open = not self.is_open

    def draw(self):
        if self.is_open:
            x = get_canvas_width() - self.image.w // 2 - 12
            y = get_canvas_height() - self.image.h // 2 - 12
            self.image.draw(x, y)
