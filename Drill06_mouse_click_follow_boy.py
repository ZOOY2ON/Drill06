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
point_x, point_y = TUK_WIDTH // 2, TUK_HEIGHT // 2 #캐릭터 이동 목표 좌표
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
    global point_x,point_y

    if len(click) == 0:
        pass
    else:
        hand.draw(point_x,point_y)

    if len(click) >= 0:
        for n in range(len(click)):
            hand.draw(click[n][0], click[n][1])
    else:
        pass

def point_check():
    global point_x, point_y

    if len(click) > 0:
        point_x, point_y = click[0]
    else:
        pass

def character_move():
    global move_x, move_y
    global point_x, point_y

    x1, y1 = move_x, move_y
    x2, y2 = point_x, point_y

    for i in range(0, 100+1, 4):
        t = i/100
        move_x = (1 - t) * x1 + t * x2
        move_y = (1 - t) * y1 + t * y2
        #print(move_x, move_y)
        Draw()

def Draw():
    global frame
    global mouse_x, mouse_y

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    mouse_draw()
    hand.draw(mouse_x, mouse_y)
    character.clip_draw(frame * 100, bottom, 100, 100, move_x, move_y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

def bottom_check():
    global bottom
    global move_x, point_x

    if move_x < point_x:
        bottom = 100
    else:
        bottom = 0

# === main ===
while running:

    clear_canvas()

    if len(click) > 0 and move_x == point_x and move_y == point_y:
        point_check()
        bottom_check()
        if len(click) > 0:
            # 다녀온 좌표를 제거
            del click[0]
    else:
        character_move()

    handle_events()

close_canvas()