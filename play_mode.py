from types import SimpleNamespace

from pico2d import *
from sdl2 import SDL_GetKeyboardState, SDL_GetScancodeFromKey

import game_framework
import game_world
import title_mode
from boy import Boy
from grass import Grass


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
        boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
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
    global boy

    game_world.clear()
    boy = None
