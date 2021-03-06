import pygame

# 초기화
pygame.init()
Clock = pygame.time.Clock()
Count = 0
Background_Delay = 3000
Background_Time = 0

# 화면
Screen_Width = 1280
Screen_Height = 720
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# 화면 타이틀 설정
pygame.display.set_caption("방구석 트레이너")  # 게임 이름

# 배경 이미지 불러오기
BackScreen = pygame.image.load("ScreenYellow.PNG").convert_alpha()
BackScreen = pygame.transform.scale(BackScreen, (1280, 720))

Left = pygame.image.load("Cheerleader1.png").convert_alpha()
Left = pygame.transform.scale(Left, (660, 580))
Right = pygame.image.load("Cheerleader2.png").convert_alpha()
Right = pygame.transform.scale(Right, (660, 580))

# 이미지 좌표(위치)
Level_1_Left_x = Screen_Width/2-330-900
Level_1_Left_y = Screen_Height
Level_1_Right_x = Screen_Width/2-330+900
Level_1_Right_y = Screen_Height

Level_2_Left_x = Screen_Width/2-330-330
Level_2_Left_y = 300
Level_2_Right_x = Screen_Width/2-330+330
Level_2_Right_y = 300

Move_Right_x = 0
Move_Right_y = 0
Move_Left_x = 0
Move_Left_y = 0
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
                elif Count == 1 and Now_Time > 5000:
                    Count += 1
                elif Count == 2 and Now_Time > 7000:
                    Count += 1
                elif Count == 3 and Now_Time > 9000:
                    Count += 1

    Screen.blit(BackScreen, (0, 0))
    Screen.blit(Left, (Level_1_Left_x, Level_1_Left_y))
    Screen.blit(Right, (Level_1_Right_x, Level_1_Right_y))

    if Count == 1:
        Move_Right_x -= 2.5
        Move_Right_y -= 2
        Move_Left_x += 2.5
        Move_Left_y -= 2
        if Level_1_Right_x > Level_2_Right_x and Level_1_Left_x < Level_2_Left_x and Level_1_Right_y > Level_2_Right_y and Level_1_Left_y > Level_2_Left_y:
            Level_1_Right_x += Move_Right_x
            Level_1_Right_y += Move_Right_y
            Level_1_Left_x += Move_Left_x
            Level_1_Left_y += Move_Left_y

    elif Count == 2:
        Left = pygame.image.load("Cheerleader2.png").convert_alpha()
        Right = pygame.image.load("Cheerleader1.png").convert_alpha()

    elif Count == 3:
        Left = pygame.image.load("Cheerleader1.png").convert_alpha()
        Right = pygame.image.load("Cheerleader2.png").convert_alpha()
        Move_Right_y = 0
        Move_Left_y = 0

    elif Count == 4:
        Move_Right_y -= 2
        Move_Left_y -= 2
        Level_1_Right_y -= Move_Right_y
        Level_1_Left_y -= Move_Left_y

    pygame.display.update()

pygame.time.delay(3000)
pygame.quit()
