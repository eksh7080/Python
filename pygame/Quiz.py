from cmd import PROMPT
import random
import pygame

# -----------------기본 초기화 ( 반드시 해야 하는 것들)--------------------#

pygame.init() 

# 화면 크기 설정
screen_width = 480  
screen_height = 640  
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("to Nim")

# FPS
clock = pygame.time.Clock()
#-----------------------------------------------------------------------#

#------------1. 사용자 게임 설정 ( 배경화면, 게임 이미지 , 좌표, 폰트 등-------------------#

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/LEE/Desktop/GitHubs/Python/pygame/background.png")


character = pygame.image.load("C:/Users/LEE/Desktop/GitHubs/Python/pygame/puppy.png")
character_size = character.get_rect().size  
character_width = character_size[0]    
character_height = character_size[1]   
character_x_position = (screen_width / 2) - (character_width / 2) - 5   
character_y_position = screen_height - character_height

# 이동할 좌표

to_x = 0
to_y = 0

# 이동 속도
character_speed = 1


ddong = pygame.image.load("C:/Users/LEE/Desktop/GitHubs/Python/pygame/poop.png")
ddong_size = ddong.get_rect().size 
ddong_width = ddong_size[0]   
ddong_height = ddong_size[1]   
ddong_x_position = random.randint(0, screen_width - ddong_width)  
ddong_y_position = 0
ddong_speed = 10


# 폰트 정의
game_font = pygame.font.Font(None, 40)  

# 총 시간
total_time = 0

# 시작 시간
start_ticks = pygame.time.get_ticks() 

# 이벤트 루프
running = True  
while running:
    dt = clock.tick(30) 


#------------2. 이벤트 처리 ( 키보드, 마우스 등)---------------------------------#
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False     


    #----------3. 게임 캐릭터 위치 정의-----------------------------#
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT:  
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  
                to_x += character_speed

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    

    character_x_position += to_x * dt
    character_y_position += to_y * dt

    ddong_y_position += ddong_speed
    
    # if ddong_y_position > screen_height:
    #     ddong_y_position = 0
    #     ddong_x_position = random.randint(0, screen_width - ddong_width) 

    # 가로 경계값 처리
    if character_x_position < 0:
        character_x_position = 0
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width
        

    # 4. 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_position
    character_rect.top = character_y_position

    ddong_rect = character.get_rect()
    ddong_rect.left = ddong_x_position
    ddong_rect.top = ddong_y_position

    if  ddong_rect.colliderect(character_rect): 
        total_time += 1
        ddong_y_position = 0
        ddong_x_position = random.randint(0, screen_width - ddong_width) 
        if total_time == 3:
            running = False
            print("Complete!")
   

    # 5. 화면에 그리기

    screen.blit(background, (0, 0)) 
    screen.blit(character, (character_x_position, character_y_position))
    screen.blit(ddong, (ddong_x_position, ddong_y_position)) 


    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
   
    timer = game_font.render(str(total_time), True, (0,0,0))
   
    screen.blit(timer, (10, 10))


    pygame.display.update() 

pygame.time.delay(1000)

# pygame 종료
pygame.quit()






