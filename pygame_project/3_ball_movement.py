import os
import pygame
##############################################
#기본 최기화 (반드시 해야 하는 것들)
pygame.init() #초기화, 반드시 수행되어야 함

#화면 크기 설정
screen_width = 640 #가로 크기
screen_height = 480 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Pang")

# FPS
clock = pygame.time.Clock()
###############################################

#1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트 등)
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") #image의 폴더 위치 반환

#배경 만들기
background = pygame.image.load(os.path.join(image_path,"background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이 위에 캐릭터를 두기 위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - character_height 

character_to_x = 0
character_speed = 5

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한 번에 여러 발 발사 가능
weapons = []
weapon_speed= 10

#공 만들기(4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

#공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] #index 0,1,2,3 에 해당하는 값

#공들
balls = []

#최초 발생하는 큰 공 추가
balls.append({
    "pos_x": 50, #공의 X좌표
    "pos_y": 50, #공의 Y좌표
    "img_idx": 0, #공의 이미지 인덱스
    "to_x": 3,#x축 이동 방향, -3이면 왼쪽으로, 3이면 오른쪽으로
    "to_y": -6, #y축 이동 방향
    "init_spd_y": ball_speed_y[0] #y 최초 속도
})

running = True 
while running:
    dt = clock.tick(30) #게임화면 초당 프레임 수

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생했는지 확인
            running = False #게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: #무기발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    #경계값 처리(캐릭터가 화면 밖으로 벗어나지 않게 함)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #무기 위치 조정
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons if w[1] > 0] #무기 위치를 위로 올려줌

    #천장에 닿은 무기 없애기 -> 무기 위치 조정 항목에 추가
    # weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 4.충돌 처리 

    # 5. 화면에 그리기
    # screen.blit 순서대로 그려지므로 배경 -> 무기 -> 스테이지 -> 캐릭터 순으로 출력되도록 조정 2021.08.24(화) AM09:18
    screen.blit(background, (0,0))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면 다시 그리기

pygame.time.delay(2000)

pygame.quit()