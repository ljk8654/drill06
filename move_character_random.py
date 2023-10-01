import turtle
import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    global point_x_count, point_y_count, points
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONUP:
            point_x[point_x_count],point_y[point_y_count] = event.x, TUK_HEIGHT - 1 - event.y
            point_x_count += 1
            point_y_count += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

running = True
point_x = [0 for i in range(1000)]
point_y = [0 for i in range(1000)]
point_x_count = 0
point_y_count = 0
point_x_start, point_y_start = 0, 0
x, y = 0, 0 #이동하는 위치
x1, y1 = TUK_WIDTH//2, TUK_HEIGHT//2 #원래 위치
frame = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for i in range(point_x_start, point_x_count + 1):
        arrow.clip_draw(0, 0, 50, 52, point_x[i], point_y[i])
    update_canvas()
    if point_x_count > 0:

        if point_x_count == point_x_start:
            clear_canvas()
            TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            for i in range(point_x_start, point_x_count):
                arrow.clip_draw(0, 0, 50, 52, point_x[i], point_y[i])
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x1, y1)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.1)
            handle_events()
        else:
            for i in range(0, 100 + 1, 5):
                t = i / 100
                x = (1 - t) * x1 + t * point_x[point_x_start]
                y = (1 - t) * y1 + t * point_y[point_y_start]
                clear_canvas()
                TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
                for i in range(point_x_start, point_x_count + 1):
                    arrow.clip_draw(0, 0, 50, 52, point_x[i], point_y[i])
                if point_x[point_x_start] > x:
                    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
                elif point_x[point_x_start] < x:
                    character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100,100)
                update_canvas()
                frame = (frame + 1) % 8
                delay(0.1)
                handle_events()
            x1 = point_x[point_x_start]
            y1 = point_y[point_y_start]
            point_x_start += 1
            point_y_start += 1

    elif point_x_count == 0:
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        for i in range(point_x_start, point_x_count):
            arrow.clip_draw(0, 0, 50, 52, point_x[i], point_y[i])
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)
        handle_events()