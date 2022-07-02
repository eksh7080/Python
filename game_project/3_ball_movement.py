import os
import pygame

# -----------------기본 초기화 ( 반드시 해야 하는 것들)--------------------#

pygame.init()  # 초기화 ( 반드시 필요 )

# 화면 크기 설정
screen_width = 640   # 가로 크기
screen_height = 480  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Pang") # 게임 이름

# FPS
clock = pygame.time.Clock()
#-----------------------------------------------------------------------#

#------------1. 사용자 게임 초기화 ( 배경화면, 게임 이미지 , 좌표, 폰트 등-------------------#
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # image 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_position = (screen_width / 2) - (character_width / 2)
character_y_position = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러번 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기 ( 4개 크기에 대해 따로 처리 )
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] 

# 공들
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "position_x" : 50, # 공의 x 좌표
    "position_y" : 50, # y 좌표
    "image_idx" : 0, # 공의 이미지 인덱스
    "to_x": 3,  # x축 이동방향, -3 이면 왼쪽으로, 3이면 오른쪽으로
    "to_y": -6, # y축 이동방향,
    "init_speed_y": ball_speed_y[0] # y 최초 속도
})


# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정


#------------2. 이벤트 처리 ( 키보드, 마우스 등)---------------------------------#
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False     # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_position = character_x_position + (character_width / 2) - (weapon_width / 2)
                weapon_y_position = character_y_position
                weapons.append([weapon_x_position, weapon_y_position])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    #----------3. 게임 캐릭터 위치 정의-----------------------------#

    character_x_position += character_to_x

    if character_x_position < 0:
        character_x_position = 0
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width


    # 무기 위치 조정
    # ex) 100,200 -> 180 , 160, 140...
    # ex) 500,200 -> 180, 160, 140...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 

    # 천장에 닿은 무기 없애기
    weapons = [[ w[0], w[1] ] for w in weapons if w[1] > 0]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_position_x = ball_val["position_x"]
        ball_position_y = ball_val["position_y"]
        ball_image_idx = ball_val["image_idx"]

        ball_size = ball_images[ball_image_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공 이동 위치 변경( 튕겨 나오는 효과 )
        if ball_position_x <= 0 or ball_position_x > (screen_width - ball_width):
            ball_val["to_x"] = ball_val["to_x"] * -1

        # 세로 위치
        # 스테이지에 튕겨서 올라가는 처리
        if ball_position_y >= (screen_height - stage_height - ball_height):
            ball_val["to_y"] = ball_val["init_speed_y"]
        else:  # 그 외의 모든 경우에는 속도 증가
            ball_val["to_y"] += 0.5

        ball_val["position_x"] += ball_val["to_x"]
        ball_val["position_y"] += ball_val["to_y"]

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0))

    for weapon_x_position, weapon_y_position in weapons:
        screen.blit(weapon, (weapon_x_position, weapon_y_position))

    for idx, val in enumerate(balls):
        ball_position_x = val["position_x"]
        ball_position_y = val["position_y"]
        ball_image_idx = val["image_idx"]
        screen.blit(ball_images[ball_image_idx], (ball_position_x,ball_position_y))
    screen.blit(stage, (0, (screen_height - stage_height)))
    screen.blit(character, (character_x_position, character_y_position))

    


    pygame.display.update() # 게임화면을 다시 그리기!!

# 잠시 대기
# pygame.time.delay(2000) # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()






