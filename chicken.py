# 원래 계획했던 방향과 프로젝트 진행 방향이 달라져서 보류
import pygame
import random

# 1 게임 초기화
pygame.init()

# 2 게임창 옵션
Screen_Width = 1280  # 가로 크기
Screen_Height = 720  # 세로 크기
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Lay Egg!")

# 3 FPS
Clock = pygame.time.Clock()
Count = 0  # 운동횟수
Target_Count = 1 #random.randrange(1, 5)  # 닭의 수 = 알의 수(랜덤으로 1~4)

# 배경이미지 불러오기
BackGround = pygame.image.load("Pink.png").convert_alpha()
BackGround = pygame.transform.scale(BackGround, (1280, 720))

# 닭 1마리
Chicken_1 = pygame.image.load("one_chicken.png").convert_alpha()
Chicken_1 = pygame.transform.scale(Chicken_1, (1280, 720))

# 닭 2마리
Chicken_2 = pygame.image.load("two_chicken.png").convert_alpha()
Chicken_2 = pygame.transform.scale(Chicken_2, (1280, 720))

# 닭 4마리
Chicken_4 = pygame.image.load("four_chicken.png").convert_alpha()
Chicken_4 = pygame.transform.scale(Chicken_4, (1280, 720))

# 알 부화 모습
Egg_1 = pygame.image.load("egg_1_1.png").convert_alpha()  # 처음 단계
Egg_2 = pygame.image.load("egg_1_1.png").convert_alpha()
Egg_3 = pygame.image.load("egg_1_1.png").convert_alpha()
Egg_4 = pygame.image.load("egg_1_1.png").convert_alpha()
BrokenEgg = pygame.image.load("egg_1_2.png").convert_alpha()  # 중간 단계
Chick = pygame.image.load("egg_1_3.png").convert_alpha()  # 부화 완료

Egg_1 = pygame.transform.scale(Egg_1, (300, 237))
Egg_2 = pygame.transform.scale(Egg_2, (300, 237))
Egg_3 = pygame.transform.scale(Egg_3, (300, 237))
Egg_4 = pygame.transform.scale(Egg_4, (300, 237))
BrokenEgg = pygame.transform.scale(BrokenEgg, (300, 237))
Chick = pygame.transform.scale(Chick, (300, 237))

Egg_1_Size = Egg_1.get_rect().size  # 이미지 크기를 구해옴
Egg_1_Width = Egg_1_Size[0]  # 캐릭터의 가로크기
Egg_1_Height = Egg_1_Size[1]  # 캐릭터의 세로크기
Egg_1_x_pos = (Screen_Width / 2) - (Egg_1_Width / 2)  # 화면 가로의 중간위치
Egg_1_y_pos = -800  # 화면 세로 가장 상단

Egg_2_Size = Egg_2.get_rect().size  # 이미지 크기를 구해옴
Egg_2_Width = Egg_2_Size[0]  # 캐릭터의 가로크기
Egg_2_Height = Egg_2_Size[1]  # 캐릭터의 세로크기
Egg_2_x_pos = (Screen_Width / 2) - (Egg_2_Width / 2) - 150  # 화면 가로의 중간위치
Egg_2_y_pos = -800  # 화면 세로 가장 상단

Egg_3_Size = Egg_3.get_rect().size  # 이미지 크기를 구해옴
Egg_3_Width = Egg_3_Size[0]  # 캐릭터의 가로크기
Egg_3_Height = Egg_3_Size[1]  # 캐릭터의 세로크기
Egg_3_x_pos = (Screen_Width / 2) - (Egg_3_Width / 2) + 150  # 화면 가로의 중간위치
Egg_3_y_pos = -800  # 화면 세로 가장 상단

Egg_4_Size = Egg_4.get_rect().size  # 이미지 크기를 구해옴
Egg_4_Width = Egg_4_Size[0]  # 캐릭터의 가로크기
Egg_4_Height = Egg_4_Size[1]  # 캐릭터의 세로크기
Egg_4_x_pos = (Screen_Width / 2) - (Egg_4_Width / 2)  # 화면 가로의 중간위치
Egg_4_y_pos = -800  # 화면 세로 가장 상단

BrokenEgg_Size = BrokenEgg.get_rect().size  # 이미지 크기를 구해옴
BrokenEgg_Width = BrokenEgg_Size[0]  # 캐릭터의 가로크기
BrokenEgg_Height = BrokenEgg_Size[1]  # 캐릭터의 세로크기
BrokenEgg_x_pos = (Screen_Width / 2) - (BrokenEgg_Width / 2)  # 화면 가로의 중간위치
BrokenEgg_y_pos = -800  # 화면 세로 가장 상단

Chick_Size = Chick.get_rect().size  # 이미지 크기를 구해옴
Chick_Width = Chick_Size[0]  # 캐릭터의 가로크기
Chick_Height = Chick_Size[1]  # 캐릭터의 세로크기
Chick_x_pos = (Screen_Width / 2) - (Chick_Width / 2)  # 화면 가로의 중간위치
Chick_y_pos = -800  # 화면 세로 가장 하단

# 폰트 정의
Game_Font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트, 크기)

# 배경음악 및 효과음 가져오기
Music = pygame.mixer.Sound("Hey_So_Jungle.mp3")

# 이벤트 루프
Crashed = False  # 게임이 진행중인가?
Yes = True
Check = 0
while not Crashed:
    dt = Clock.tick(30)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            Crashed = True  # 게임이 진행중이 아님
            break
        #pygame.mixer.Sound.play(Music)

        if event.type == pygame.KEYUP:
            Yes = True

        if event.type == pygame.KEYDOWN:  # 키가 눌렸는지 확인
            if event.key == pygame.K_DOWN:  # 아랫쪽 방향키
                if Yes == True:
                    Yes = False
                    if Count == 0:
                        Count += 1
                    elif Count == 1:
                        Count += 1
                    elif Count == 2:
                        Count += 1
                    elif Count == 3:
                        Count += 1
                    elif Count == 4:
                        Count += 1
                    else:
                        Count = 0

    Screen.blit(BackGround, (0, 0))  # 배경 그리기

    if Count >= 1:
        if Egg_1_y_pos <= Screen_Height:
            Egg_1_y_pos += 80
            if Egg_1_y_pos >= Screen_Height - 237:  # 237 = 알의 세로 크기
                Egg_1_y_pos = Screen_Height - 237

    if Count >= 2:
        if Egg_2_y_pos <= Screen_Height:
            Egg_2_y_pos += 50
            if Egg_2_y_pos >= Screen_Height - 237:
                Egg_2_y_pos = Screen_Height - 300

    if Count >= 3:
        if Egg_3_y_pos <= Screen_Height:
            Egg_3_y_pos += 100
            if Egg_3_y_pos >= Screen_Height - 237:
                Egg_3_y_pos = Screen_Height - 300

    if Count >= 4:
        if Egg_4_y_pos <= Screen_Height:
            Egg_4_y_pos += 100
            if Egg_4_y_pos >= Screen_Height - 237 - 237:
                Egg_4_y_pos = Screen_Height - 237 - 237

    if Target_Count == Count:
        if Egg_1_y_pos == Screen_Height - 237:
            if Check == 0:
                pygame.time.delay(1000)
                Egg_1 = pygame.image.load("egg_1_2.png").convert_alpha()
                Egg_1 = pygame.transform.scale(Egg_1, (300, 237))
                Check += 1
            elif Check == 1:
                pygame.time.delay(1000)
                Egg_1 = pygame.image.load("egg_1_3.png").convert_alpha()
                Egg_1 = pygame.transform.scale(Egg_1, (300, 237))

    if Target_Count == 1:
        Screen.blit(Chicken_1, (0, 0))
        Screen.blit(Egg_1, (Egg_1_x_pos, Egg_1_y_pos))

    elif Target_Count == 2:
        Screen.blit(Chicken_2, (0, 0))
        Screen.blit(Egg_1, (Egg_1_x_pos, Egg_1_y_pos))
        Screen.blit(Egg_2, (Egg_2_x_pos, Egg_2_y_pos))

    elif Target_Count == 4:
        Screen.blit(Chicken_4, (0, 0))
        Screen.blit(Egg_1, (Egg_1_x_pos, Egg_1_y_pos))
        Screen.blit(Egg_2, (Egg_2_x_pos, Egg_2_y_pos))
        Screen.blit(Egg_3, (Egg_3_x_pos, Egg_3_y_pos))
        Screen.blit(Egg_4, (Egg_4_x_pos, Egg_4_y_pos))

    pygame.display.update()
pygame.time.delay(5000)  # 5초 정도 대기 (ms)
pygame.quit()
