import pygame

# 초기화
pygame.init()
Count = 0
Clock = pygame.time.Clock()
Background_Delay = 3000
Background_Time = 0

# 화면
Screen_Width = 1280
Screen_Height = 720
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# 화면 타이틀 설정
pygame.display.set_caption("방구석 트레이너")

# 배경 이미지 불러오기
BackScreen = pygame.image.load("ScreenYellow.PNG").convert_alpha()
BackScreen = pygame.transform.scale(BackScreen, (1280, 720))

Fan = pygame.image.load("Fancafe1.png").convert_alpha()
Fan = pygame.transform.scale(Fan, (780, 560))

Level_1_x = Screen_Width
Level_1_y = 250
Level_2_x = Screen_Width/2-140
Level_2_y = 250

Move_x = 0
Move_y = 3.5

# 이벤트
# Now_Time = pygame.time.get_ticks()
Crashed = False
Yes = True
while not Crashed:
    dt = Clock.tick(30)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            Crashed = True
            break

        if event.type == pygame.KEYUP:
            Yes = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Now_Time = pygame.time.get_ticks()
                if Now_Time > Background_Time + Background_Delay:
                    Background_Time = Now_Time
                if Count == 0 and Now_Time > 3000:
                    Count += 1
                elif Count == 1 and Now_Time > 4000:
                    Count += 1
                elif Count == 2 and Now_Time > 6000:
                    Count += 1
                elif Count == 3 and Now_Time > 7000:
                    Count += 1

    Screen.blit(BackScreen, (0, 0))
    Screen.blit(Fan, (Level_1_x, Level_1_y))
    if Count == 1:
        Move_x += 3.5
        if Level_1_x > Level_2_x:
            Level_1_x -= Move_x

    if Count == 2:
        Level_1_y = Level_2_x/2 - 90
        Level_1_x = Level_2_x/2 + 200
        Fan = pygame.image.load("Fancafe2.png").convert_alpha()
        Fan = pygame.transform.scale(Fan, (830, 595))

    if Count == 3:
        Level_1_y = Level_2_x/2
        Level_1_x = Level_2_x / 2 + 220
        Fan = pygame.image.load("Fancafe1.png").convert_alpha()

    if Count == 4:
        Move_y -= 3.5
        Level_1_y -= Move_y

    '''
    Move_y = 0
    
    if Count == 4:
        Move_y -= 3.5
        Level_1_y -= Move_y
    '''
    pygame.display.update()

pygame.time.delay(3000)
pygame.quit()
