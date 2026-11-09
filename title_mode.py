import game_framework
from pico2d import *

image = None


def init():
    global image
    image = load_image('title.png')


def finish():
    global image
    image = None


def update():
    pass


def render():
    clear_canvas()
    image.draw(400, 300, 800, 600)
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (
            event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
        ):
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            import play_mode

            game_framework.change_mode(play_mode)
            return
