# 2021.5,15 (19:22) 운동 메뉴 선택
# 슬라이드쇼 효과 및 fade in - 김수영

import pygame

# 초기화
pygame.init()
Count = 0  # Count = 1 => 상체, Count = 2 => 하체, Count = 3 => 전신
Clock = pygame.time.Clock()
Background_Delay = 3000
Background_Time = 0
OpacityLevel = -255

# 화면
Screen_Width = 1280
Screen_Height = 720
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# 화면 타이틀 설정
pygame.display.set_caption("방구석 트레이너")

# 배경 이미지 불러오기
BackScreen = pygame.image.load("Background.png").convert_alpha()
BackScreen = pygame.transform.scale(BackScreen, (1280, 720))

UpBlue = pygame.image.load("Block1.png").convert_alpha()
UpBlue = pygame.transform.scale(UpBlue, (769, 750))

DownBlue = pygame.image.load("Block2.png").convert_alpha()
DownBlue = pygame.transform.scale(DownBlue, (1330, 253))

Crowd = pygame.image.load("Crowd.png").convert_alpha()
Crowd = pygame.transform.scale(Crowd, (886, 550))

SongBlock = pygame.image.load("SongBlock.png").convert_alpha()
SongBlock = pygame.transform.scale(SongBlock, (360, 360))

Prev = pygame.image.load("PrevButton.png").convert_alpha()
Prev = pygame.transform.scale(Prev, (150, 97))

Next = pygame.image.load("NextButton.png").convert_alpha()
Next = pygame.transform.scale(Next, (150, 97))

Exit = pygame.image.load("ExitButton.png").convert_alpha()
Exit = pygame.transform.scale(Exit, (84, 86))

BodyFont = pygame.image.load("BodyFont.png").convert_alpha()
BodyFont = pygame.transform.scale(BodyFont, (326, 225))

TopFont = pygame.image.load("TopFont.png").convert_alpha()
TopFont = pygame.transform.scale(TopFont, (326, 225))

BottomFont = pygame.image.load("BottomFont.png").convert_alpha()
BottomFont = pygame.transform.scale(BottomFont, (326, 225))

# DB = DownBlue, UB = UpBlue, SB = SongBlock
DB_Level_1_x = -20
DB_Level_1_y = 1.2*Screen_Height + 120
DB_Level_2_x = -20
DB_Level_2_y = Screen_Height/2 + 170

UB_Level_1_x = Screen_Width/2 - 365
UB_Level_1_y = Screen_Height
UB_Level_2_x = Screen_Width/2 - 365
UB_Level_2_y = Screen_Height/70 - 20

Crowd_Level_1_x = Screen_Width/2 - 420
Crowd_Level_1_y = Screen_Height
Crowd_Level_2_x = Screen_Width/2 - 420
Crowd_Level_2_y = Screen_Height/2 - 20

SB_x = Screen_Width/2 - 154
SB_y = Screen_Height/2 - 275

Prev_x = UB_Level_1_x - 150
Prev_y = Screen_Height/2 - 150

Next_x = UB_Level_1_x + 750
Next_y = Screen_Height/2 - 150

Exit_x = Screen_Width/2 - 630
Exit_y = Screen_Height/2 - 360

Font_x = Crowd_Level_2_x + 280
Font_y = 1.5*Crowd_Level_2_y + 30

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
            if event.key == pygame.K_RIGHT:
                OpacityLevel = -255
                Move_y = 0
                DB_Level_1_x = -20
                DB_Level_1_y = 1.2 * Screen_Height + 120
                UB_Level_1_x = Screen_Width / 2 - 365
                UB_Level_1_y = Screen_Height
                Crowd_Level_1_x = Screen_Width / 2 - 420
                Crowd_Level_1_y = Screen_Height
                Now_Time = pygame.time.get_ticks()
                if Now_Time > Background_Time + Background_Delay:
                    Background_Time = Now_Time
                if Count == 0:
                    Count += 1
                elif Count == 1:
                    Count += 1
                elif Count == 2:
                    Count += 1
                elif Count == 3:
                    Count = 1

    Screen.blit(BackScreen, (0, 0))
    Screen.blit(DownBlue, (DB_Level_1_x, DB_Level_1_y))
    Screen.blit(UpBlue, (UB_Level_1_x, UB_Level_1_y))
    Screen.blit(Crowd, (Crowd_Level_1_x, Crowd_Level_1_y))

    if Count == 1:
        SongBlock.set_alpha(OpacityLevel)
        Screen.blit(SongBlock, (SB_x, SB_y))
        Prev.set_alpha(OpacityLevel)
        Screen.blit(Prev, (Prev_x, Prev_y))
        Next.set_alpha(OpacityLevel)
        Screen.blit(Next, (Next_x, Next_y))
        TopFont.set_alpha(OpacityLevel)
        Screen.blit(TopFont, (Font_x, Font_y))
        Exit.set_alpha(OpacityLevel)
        Screen.blit(Exit, (Exit_x, Exit_y))

        if OpacityLevel <= 250:
            OpacityLevel += 18.5

        Move_y += 3.5
        if DB_Level_1_y > DB_Level_2_y:
            DB_Level_1_y -= 0.9*Move_y

        if UB_Level_1_y > UB_Level_2_y:
            UB_Level_1_y -= 1.4*Move_y

        if Crowd_Level_1_y > Crowd_Level_2_y:
            Crowd_Level_1_y -= 0.46*Move_y

    if Count == 2:
        SongBlock.set_alpha(OpacityLevel)
        Screen.blit(SongBlock, (SB_x, SB_y))
        Prev.set_alpha(OpacityLevel)
        Screen.blit(Prev, (Prev_x, Prev_y))
        Next.set_alpha(OpacityLevel)
        Screen.blit(Next, (Next_x, Next_y))
        BottomFont.set_alpha(OpacityLevel)
        Screen.blit(BottomFont, (Font_x, Font_y))
        Exit.set_alpha(OpacityLevel)
        Screen.blit(Exit, (Exit_x, Exit_y))

        if OpacityLevel <= 250:
            OpacityLevel += 18.5

        Move_y += 3.5

        if DB_Level_1_y > DB_Level_2_y:
            DB_Level_1_y -= 0.9 * Move_y

        if UB_Level_1_y > UB_Level_2_y:
            UB_Level_1_y -= 1.4 * Move_y

        if Crowd_Level_1_y > Crowd_Level_2_y:
            Crowd_Level_1_y -= 0.46 * Move_y

    if Count == 3:
        SongBlock.set_alpha(OpacityLevel)
        Screen.blit(SongBlock, (SB_x, SB_y))
        Prev.set_alpha(OpacityLevel)
        Screen.blit(Prev, (Prev_x, Prev_y))
        Next.set_alpha(OpacityLevel)
        Screen.blit(Next, (Next_x, Next_y))
        BodyFont.set_alpha(OpacityLevel)
        Screen.blit(BodyFont, (Font_x, Font_y))
        Exit.set_alpha(OpacityLevel)
        Screen.blit(Exit, (Exit_x, Exit_y))

        if OpacityLevel <= 250:
            OpacityLevel += 18.5

        Move_y += 3.5

        if DB_Level_1_y > DB_Level_2_y:
            DB_Level_1_y -= 0.9 * Move_y

        if UB_Level_1_y > UB_Level_2_y:
            UB_Level_1_y -= 1.4 * Move_y

        if Crowd_Level_1_y > Crowd_Level_2_y:
            Crowd_Level_1_y -= 0.46 * Move_y

    pygame.display.update()

pygame.time.delay(3000)
pygame.quit()
