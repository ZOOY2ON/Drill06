from pico2d import *

#이미지 및 배경 설정
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

#변수 선언
move_x, move_y = TUK_WIDTH // 2, TUK_HEIGHT // 2 #캐릭터 이동 좌표
hand_x, hand_y = TUK_WIDTH // 2, TUK_HEIGHT // 2 #마우스 이동 좌표
click_x, click_y = TUK_WIDTH // 2, TUK_HEIGHT // 2 #마우스 클릭 좌표
click = [(TUK_WIDTH // 2, TUK_HEIGHT // 2)]

running = True
frame, bottom = 0, 0 #스프라이트 시트 clip


# === main ===
print(click[0][0])
print(click[0][1])