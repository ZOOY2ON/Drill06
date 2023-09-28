from pico2d import *

#이미지 및 배경 설정
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
hide_cursor()

#변수 선언
move_x, move_y = TUK_WIDTH // 2, TUK_HEIGHT // 2 #캐릭터 이동 좌표
mouse_x, mouse_y = TUK_WIDTH // 2, TUK_HEIGHT // 2 #마우스 이동 좌표
click_x, click_y = TUK_WIDTH // 2, TUK_HEIGHT // 2 #마우스 클릭 좌표
click = [(TUK_WIDTH // 2, TUK_HEIGHT // 2)]

running = True
frame, bottom = 0, 0 #스프라이트 시트 clip

def handle_events():
    global running
    global mouse_x, mouse_y
    global click_x, click_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            click_x, click_y = event.x, TUK_HEIGHT - 1 - event.y
            click.append((click_x,click_y))
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y

def mouse_draw():
    global mouse_x, mouse_y

    hand.draw(mouse_x,mouse_y)

    for n in range (len(click)):
        hand.draw(click[n][0],click[n][1])

# === main ===
while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    mouse_draw()
    update_canvas()
    handle_events()

close_canvas()