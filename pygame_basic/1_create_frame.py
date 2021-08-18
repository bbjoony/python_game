import pygame

pygame.init() #초기화, 반드시 수행되어야 함

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
pygame.display.set_mode((screen_width, screen_height))

#게임 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#이벤트 루프
running = True #게임이 진행 중인지 확인
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생했는지 확인
                running = False

#Pygame 종료
pygame.quit()