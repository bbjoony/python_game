import random
import pygame
##############################################
#기본 최기화 (반드시 해야 하는 것들)
pygame.init() #초기화, 반드시 수행되어야 함

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock()
###############################################

#1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트 등)
background = pygame.image.load("/Users/devsiters/PythonWorkspace/pygame_basic/background.png")

character = pygame.image.load("/Users/devsiters/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#이동 위치
to_x = 0
character_speed = 10

#폭탄 만들기
bomb = pygame.image.load("/Users/devsiters/PythonWorkspace/pygame_basic/enemy.png")
bomb_size = bomb.get_rect().size
bomb_width = bomb_size[0]
bomb_height = bomb_size[1]
bomb_x_pos = random.randint(0, screen_width - bomb_width)
bomb_y_pos = 0
bomb_speed = 10

running = True 
while running:
    dt = clock.tick(30) #게임화면 초당 프레임 수

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생했는지 확인
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    bomb_y_pos += bomb_speed
    if bomb_y_pos > screen_height:
        bomb_y_pos = 0
        bomb_x_pos = random.randint(0, screen_width - bomb_width)

    # 4.충돌 처리 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    bomb_rect = bomb.get_rect()
    bomb_rect.left = bomb_x_pos
    bomb_rect.top = bomb_y_pos

    if character_rect.colliderect(bomb_rect):
        print("충돌했어요! 게임을 끝냅니다.")
        running = False 

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(bomb, (bomb_x_pos, bomb_y_pos))

    pygame.display.update() #게임화면 다시 그리기

pygame.time.delay(2000)

pygame.quit()