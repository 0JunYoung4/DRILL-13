from types import SimpleNamespace

from pico2d import *
from sdl2 import SDL_GetKeyboardState, SDL_GetScancodeFromKey

import game_framework
import game_world
import title_mode
from ball import LARGE_BALL_SIZE, SMALL_BALL_SIZE
from boy import Boy
from grass import Grass
from item_mode import ItemMode


ITEM_BALL_SIZES = {
    SDLK_0: None,
    SDLK_1: SMALL_BALL_SIZE,
    SDLK_2: LARGE_BALL_SIZE,
    SDLK_KP_0: None,
    SDLK_KP_1: SMALL_BALL_SIZE,
    SDLK_KP_2: LARGE_BALL_SIZE,
}


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode

            game_framework.push_mode(pause_mode)
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_mode.toggle()
            continue
        if (event.type == SDL_KEYDOWN and item_mode.is_open
                and event.key in ITEM_BALL_SIZES):
            boy.ball_size = ITEM_BALL_SIZES[event.key]
            continue
        boy.handle_event(event)


def init():
    global boy, item_mode

    boy = Boy()
    item_mode = ItemMode()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    item_mode.draw()
    update_canvas()

def pause():
    global paused_at

    paused_at = get_time()


def resume():
    boy.idle_started_at += get_time() - paused_at

    keyboard = SDL_GetKeyboardState(None)
    for key in tuple(boy.pressed_keys):
        if not keyboard[SDL_GetScancodeFromKey(key)]:
            boy.handle_event(SimpleNamespace(type=SDL_KEYUP, key=key))


def finish():
    global boy, item_mode

    game_world.clear()
    boy = None
    item_mode = None
