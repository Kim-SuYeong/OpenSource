import pygame

# 초기화
pygame.init()
Clock = pygame.time.Clock()
Count = 0
Move = 120

# 화면
Screen_Width = 1280
Screen_Height = 720
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# 화면 타이틀 설정
pygame.display.set_caption("방구석 트레이너")  # 게임 이름

# 배경 이미지 불러오기
BackScreen = pygame.image.load("ScreenYellow.PNG").convert_alpha()
BackScreen = pygame.transform.scale(BackScreen, (1280, 720))

Left_1 = pygame.image.load("gin_tape_fan_man.png").convert_alpha()
Left_1 = pygame.transform.scale(Left_1, (300, 300))
Left_2 = pygame.image.load("gin_tape_fan_man_reflect.png").convert_alpha()
Left_2 = pygame.transform.scale(Left_2, (300, 300))
Right_1 = pygame.image.load("gin_tape_fan_woman.png").convert_alpha()
Right_1 = pygame.transform.scale(Right_1, (300, 300))
Right_2 = pygame.image.load("gin_tape_fan_woman_reflect.png").convert_alpha()
Right_2 = pygame.transform.scale(Right_2, (300, 300))

# 이미지 좌표(위치)
Left_x = 60
Left_y = Screen_Height
Right_x = 900
Right_y = Screen_Height
Left_x_2 = 0
Right_x_2 = 0

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
                if Count == 0:
                    Count += 1
                elif Count == 1:
                    Count += 1
                elif Count == 2:
                    Count += 1

    Screen.blit(BackScreen, (0, 0))

    if Count == 1:
        Left_y -= Move
        Right_y -= Move
        if Left_y == 120 and Right_y == 120:
            Left_y = 240
            Right_y = 240
            Screen.blit(Left_1, (Left_x, Left_y))
            Screen.blit(Right_1, (Right_x, Right_y))
    elif Count == 2:
        Left_x_2 = Left_x - 60
        Right_x_2 = Right_x + 60
        Screen.blit(Left_2, (Left_x_2, Left_y))
        Screen.blit(Right_2, (Right_x_2, Right_y))
    elif Count == 3:
        Left_y += Move
        Right_y += Move
        Screen.blit(Left_2, (Left_x, Left_y))
        Screen.blit(Right_2, (Right_x, Right_y))

    pygame.display.update()

pygame.time.delay(3000)
pygame.quit()

