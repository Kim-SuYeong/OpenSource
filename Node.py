# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:53:36 2021
Modifyed on Fri May   14 10:31 2021

@author: USER
"""

import cv2 as cv
import pygame
import random
import sys

BLACK = (0, 0, 0)
BLUE = (0, 199, 254)
GREEN = (35, 226, 11)
PINK = (251, 64, 174)

COLORS = [BLUE, GREEN, PINK]

# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

######################################################################
# 화면 크기 설정
Screen_Width = 1280  # 가로 크기
Screen_Height = 720  # 세로 크기
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
######################################################################
# 화면 타이틀 설정
pygame.display.set_caption("방구석 트레이너")  # 게임 이름

lunge1 = pygame.image.load('Rhythm/Upper_Pose/lunge2.png').convert_alpha()
lunge1_Size = lunge1.get_rect().size
lunge1_Width = lunge1_Size[0]
lunge1_Height = lunge1_Size[1]
lunge1 = pygame.transform.scale(lunge1, (int(lunge1_Width / 1.5), int(lunge1_Height / 1.5)))

lunge2 = pygame.image.load('Rhythm/Upper_Pose/lunge1.png').convert_alpha()
lunge2_Size = lunge2.get_rect().size
lunge2_Width = lunge2_Size[0]
lunge2_Height = lunge2_Size[1]
lunge2 = pygame.transform.scale(lunge2, (int(lunge2_Width / 1.5), int(lunge2_Height / 1.5)))

bigclap1 = pygame.image.load('Rhythm/Upper_Pose/bigclap1.png').convert_alpha()
bigclap1_Size = bigclap1.get_rect().size
bigclap1_Width = bigclap1_Size[0]
bigclap1_Height = bigclap1_Size[1]
bigclap1 = pygame.transform.scale(bigclap1, (int(bigclap1_Width / 1.5), int(bigclap1_Height / 1.5)))

bigclap2 = pygame.image.load('Rhythm/Upper_Pose/bigclap2.png').convert_alpha()
bigclap2_Size = bigclap2.get_rect().size
bigclap2_Width = bigclap2_Size[0]
bigclap2_Height = bigclap2_Size[1]
bigclap2 = pygame.transform.scale(bigclap2, (int(bigclap2_Width / 1.5), int(bigclap2_Height / 1.5)))

# 노드 관련
list_Node = [[lunge2, lunge1], [bigclap1, bigclap2]]

Pose_Index = -1
Node_Index = -1


# for i in range(len(list_Node)):
#     list_Node[i] = pygame.transform.scale(list_Node[i], (247, 511))

def MakeNode(isLeft, Index1=0, Index2=0):
    NodeRect = list_Node[Index1][Index2].get_rect()
    NodeRect.top = 150

    NodeRect.right = Screen_Width + list_Node[Index1][Index2].get_width()
    if isLeft:
        NodeRect.left = 0 - list_Node[Index1][Index2].get_width()

    return [list_Node[Index1][Index2], NodeRect, isLeft]


def Func_ChangeBackground(Color):
    # Bg == Blue
    BgColor[3] += 1

    if Color == 0:
        BgColor[0] -= int(abs((PINK[0] - BLUE[0]) / 13))
        BgColor[1] += int(abs((PINK[1] - BLUE[1]) / 13))
        BgColor[2] += int(abs((PINK[2] - BLUE[2]) / 13))


    # Bg == GREEN
    elif Color == 1:
        BgColor[0] += int(abs((BLUE[0] - GREEN[0]) / 13))
        BgColor[1] += int(abs((BLUE[1] - GREEN[1]) / 13))
        BgColor[2] -= int(abs((BLUE[2] - GREEN[2]) / 13))


    # Bg == PINK
    elif Color == 2:
        BgColor[0] += int(abs((GREEN[0] - PINK[0]) / 13))
        BgColor[1] -= int(abs((GREEN[1] - PINK[1]) / 13))
        BgColor[2] += int(abs((GREEN[2] - PINK[2]) / 13))

    if BgColor[3] >= 12:
        for i in range(3):
            BgColor[i] = COLORS[Color][i]
        BgColor[3] = 0
        return 0

    return 1


# OpenCV 기본 초기화
cap = cv.VideoCapture(0)
######################################################################
# FPS
Clock = pygame.time.Clock()
######################################################################
# 배경 색상 관련 변수 및 상수
Background_Delay = 3000
Background_Time = 0
Background_Color = 0
Background_MAX = 3
Background_Change = 0
BgColor = [0, 199, 254, 0]

# 배경 왼/오른쪽/가운데 이미지 불러오기
Background_Middle = pygame.image.load("Rhythm/Smartphone.png").convert_alpha()
Background_Middle = pygame.transform.scale(Background_Middle, (545, 808))

Background_Laft = pygame.image.load("Rhythm/SmartphoneLeftScreen.png").convert_alpha()
Background_Laft = pygame.transform.scale(Background_Laft, (405, 607))

Background_Right = pygame.image.load("Rhythm/SmartphoneRightScreen.png").convert_alpha()
Background_Right = pygame.transform.scale(Background_Right, (410, 607))

BlackScreen = pygame.image.load("Rhythm/BlackScreen.png").convert_alpha()
BlackScreen = pygame.transform.scale(BlackScreen, (1700, Screen_Height))

# 배경 위쪽의 그림자 생성
ShadowRect = pygame.image.load("Rhythm/BlackScreen.png")
ShadowRect = pygame.transform.scale(ShadowRect, (Screen_Width, 6))

# 효과음
NodeBGM = pygame.mixer.Sound('node/決定、ボタン押下2.mp3')
ScratchShortBGM = pygame.mixer.Sound('node/djscratch_short.mp3')
######################################################################
# 시간 계산
Start_Ticks = pygame.time.get_ticks()
######################################################################
Timer_Font = pygame.font.Font("Rhythm/CookieRun Regular.ttf", 30)  # 폰트 객체 생성(폰트, 크기)
Music_Font = pygame.font.Font("Rhythm/CookieRun Bold.ttf", 40)
Artist_Font = pygame.font.Font("Rhythm/CookieRun Regular.ttf", 30)
Percentage_Font = pygame.font.Font("Rhythm/CookieRun Bold.ttf", 40)
######################################################################
# 각 musicindex에 해당하는 곡과 타이밍
musicindex = 1
if musicindex == 1:
    music = "Rhythm/BGM/playing songs/昼の月(1번 곡).mp3"
    SongSection = [[6, 3000], [11, 5000], [20, 3000], [24, 2000], [28, 4000], [30, 2000], [34, 4000], [43, 3000],
                   [45, 2000], [47, 2000], [51, 4000], [53, 2000], [57, 4000], [69, 6000]]

elif musicindex == 2:
    music = "Rhythm/BGM/playing songs/swing_swing(2번 곡).mp3"
    SongSection = [[5, 2000], [9, 4000], [13, 2000], [17, 4000], [21, 2000], [41, 4000], [57, 8000], [89, 4000],
                   [105, 8000], [121, 4000], [137, 2000], [169, 4000], [185, 8000]]

elif musicindex == 3:
    music = "Rhythm/BGM/playing songs/追跡者(3번 곡).mp3"
    SongSection = [[18, 15000], [19, 2000], [22, 3000], [26, 2000], [29, 3000], [43, 14000], [49, 6000], [52, 3000],
                   [56, 4000], [63, 7000], [66, 3000], [70, 4000], [84, 7000], [92, 4000], [95, 3000], [99, 4000],
                   [105, 3000], [109, 4000], [112, 3000], [120, 8000], [127, 7000], [129, 2000], [133, 4000], [135, 2000],
                   [140, 5000], [143, 3000], [148, 5000], [154, 6000], [173, 6000], [176, 3000], [186, 5000], [190, 4000],
                   [198, 3000], [202, 4000], [214, 6000], [216, 2000], [219, 3000], [223, 4000], [232, 3000], [237, 5000],
                   [242, 5000], [250, 8000], [254, 4000], [260, 6000], [268, 4000], [271, 3000], [276, 5000], [278, 2000],
                   [290, 6000], [297, 7000], [301, 4000]]

elif musicindex == 4:
    music = "Rhythm/BGM/playing songs/Feather_of_the_Angel(4번 곡).mp3"
    SongSection = [[16, 4000], [19, 3000], [31, 4000], [34, 3000], [42, 4000], [45, 3000], [53, 4000], [56, 3000],
                   [64, 4000], [67, 3000], [71, 4000]]

elif musicindex == 5:
    music = "Rhythm/BGM/playing songs/New_Future(5번 곡).mp3"
    SongSection = [[21, 7000], [29, 8000], [33, 2000], [37, 4000], [39, 2000], [44, 5000], [47, 3000], [51, 4000],
                   [54, 3000], [58, 4000], [67, 3000], [71, 4000], [74, 3000], [82, 4000], [88, 3000], [116, 4000],
                   [119, 3000], [123, 4000], [129, 3000], [133, 4000], [136, 3000], [140, 4000], [146, 6000], [187, 7000]]

elif musicindex == 6:
    music = "Rhythm/BGM/playing songs/スターシップ・ドリーマー(6번 곡).mp3"
    SongSection = [[5, 2000], [8, 3000], [12, 2000], [15, 3000], [19, 2000], [22, 3000], [26, 2000], [32, 3000],
                   [36, 4000], [42, 3000], [46, 4000], [49, 3000], [53, 4000], [56, 3000], [64, 8000], [70, 6000],
                   [98, 7000], [104, 6000], [111, 7000], [115, 4000], [121, 3000], [125, 4000], [131, 3000], [135, 4000]]

elif musicindex == 7:
    music = "Rhythm/BGM/playing songs/Film_Clash!(7번 곡).mp3"
    SongSection = [[9, 8000], [10, 2000], [15, 5000], [18, 3000], [26, 4000], [32, 3000], [38, 6000], [44, 2000],
                   [47, 3000], [55, 4000], [58, 3000], [66, 4000], [69, 3000], [75, 6000], [77, 2000], [80, 3000]]

elif musicindex == 8:
    music = "Rhythm/BGM/playing songs/Funky_Junky(8번 곡).mp3"
    SongSection = [[19, 19000], [20, 1000], [23, 3000], [24, 1000], [27, 3000], [28, 1000], [32, 4000], [33, 1000],
                   [36, 3000], [38, 2000], [41, 3000], [53, 2000], [58, 5000], [66, 4000], [71, 5000], [79, 4000],
                   [89, 5000], [90, 1000], [93, 3000], [94, 1000], [97, 3000], [98, 1000], [102, 4000], [103, 1000],
                   [106, 3000], [112, 2000], [115, 3000], [123, 2000], [127, 4000], [132, 5000], [136, 4000], [141, 5000],
                   [149, 4000], [154, 5000], [158, 4000]]

elif musicindex == 9:
    music = "Rhythm/BGM/playing songs/Expantion(9번 곡).mp3"
    SongSection = [[12, 12000], [16, 2000], [22, 6000], [25, 3000], [33, 8000], [38, 5000], [41, 3000], [47, 6000],
                   [54, 7000], [57, 3000], [63, 6000], [70, 7000], [73, 3000], [85, 6000], [93, 4000], [95, 2000],
                   [101, 6000], [105, 4000], [111, 3000], [116, 5000], [122, 6000], [126, 4000], [131, 5000],
                   [138, 7000], [141, 3000], [147, 6000], [155, 4000], [159, 2000], [171, 4000], [175, 2000], [183, 8000]]

elif musicindex == 10:
    music = "Rhythm/BGM/playing songs/Space_Town_(Brand_New_Mix)_[Update_2016.12.30](10번 곡).mp3"
    SongSection = [[4, 4000], [9, 5000], [12, 3000], [14, 2000], [23, 3000], [27, 2000], [31, 4000], [35, 2000],
                   [39, 4000], [43, 2000], [47, 4000], [51, 2000], [55, 4000], [59, 2000], [62, 3000], [63, 1000],
                   [73, 2000], [79, 3000], [81, 2000], [87, 3000]]
    
# 배경음악
pygame.mixer.music.load(music)

SectionNum = 1
Song_Time = 0
######################################################################
Minus_Score = 0
Percentage = 100
queue_Node = []

x = 1
PlayOn = 1
TurnOn = 0
NodeOn = 0
BeatHeart = 1
OpacityLevel = 255
Crashed = False
######################################################################
while not Crashed:
    dt = Clock.tick(30)
    Elapsed_Time = (pygame.time.get_ticks() - Start_Ticks) / 1000
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            cap.release()
            cv.destroyAllWindows()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:  # 키가 눌렸는지 확인
            if event.key == pygame.K_UP:  # 위쪽 방향키
                for temp, tempRect, isLeft in queue_Node:
                    # 왼쪽 노드라면
                    if isLeft:
                        if 0 <= tempRect.left <= 377:
                            ScratchShortBGM.play()
                            queue_Node.pop(0)
                            Minus_Score -= 1

                    # 오른쪽 노드라면
                    else:
                        if 896 <= tempRect.right <= 896 + 377:
                            ScratchShortBGM.play()
                            queue_Node.pop(0)
                            Minus_Score -= 1

    ######################################################################
    # 화면 색깔 변환
    Now_Time = pygame.time.get_ticks()
    if (Now_Time > Background_Time + Background_Delay):
        Background_Time = Now_Time
        Background_Color += 1
        Background_Change = 1
        if (Background_Color >= Background_MAX):
            Background_Color = 0

    if Background_Change:
        Background_Change = Func_ChangeBackground(Background_Color)

    Screen.fill((BgColor[0], BgColor[1], BgColor[2]))

    # 그림자 생성
    # Screen.fill((0, 199, 254))
    ShadowRect.set_alpha(70)
    Screen.blit(ShadowRect, (0, 107))
    ShadowRect.set_alpha(50)
    Screen.blit(ShadowRect, (0, 105))
    ShadowRect.set_alpha(30)

    Screen.blit(ShadowRect, (0, 102))
    Screen.blit(Background_Laft, (0, 112))
    Screen.blit(Background_Right, (870, 112))

    ######################################################################

    # 화면에 노드 추가하기
    # if (float(Elapsed_Time) >= 2.8 and float(Elapsed_Time) <= 3):
    #     if TurnOn == 0:
    #         # 왼쪽 노드 추가하기
    #         if random.randrange(0, 2):
    #             queue_Node.append(MakeNode(1))
    #
    #         # 오른쪽 노드 추가하기
    #         else:
    #             queue_Node.append(MakeNode(0))
    #         ScratchShortBGM.play()
    #         TurnOn += 1

    # 노드를 중앙으로 움직이기
    for i in range(len(queue_Node)):
        # 만약 왼쪽 노드라면
        if queue_Node[i][2] == 1:
            queue_Node[i][1].left += 20

        # 만약 오른쪽 노드라면
        else:
            queue_Node[i][1].right -= 20

    # 노드를 화면에 출력하기
    for temp, tempRect, _ in queue_Node:
        Screen.blit(temp, tempRect)

    ######################################################################

    # 사용자 캠 불러오기
    _, frame = cap.read()
    frame = frame[0:480, 153:486]
    cv.imwrite('Frame.png', frame)

    py_Frame = pygame.image.load("Frame.png").convert_alpha()
    py_Frame = pygame.transform.scale(py_Frame, (478, 771))
    Screen.blit(py_Frame, (399, 111))
    Screen.blit(Background_Middle, (363, 43))

    ######################################################################
    for temp, tempRect, isLeft in queue_Node:
        # 왼쪽 노드라면
        if isLeft:
            if tempRect.left >= (1280 / 2) - (temp.get_rect().width / 2):
                queue_Node.pop(0)
                Minus_Score += 1

        # 오른쪽 노드라면
        else:
            if tempRect.right <= (1280 / 2) + (temp.get_rect().width / 2):
                queue_Node.pop(0)
                Minus_Score += 1

    if not pygame.mixer.music.get_busy():  # like this!
        if PlayOn == 1:
            pygame.mixer.music.play()
            PlayOn -= 1
        else:
            Crashed = True
        ######################################################################
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시
    Elapsed_Time = (pygame.time.get_ticks() - Start_Ticks) / 1000
    # 출력할 글자, True, 글자 색상

    Minutes = int(Elapsed_Time / 60)
    Seconds = int(Elapsed_Time % 60)

    if Seconds < 10:
        timer = Timer_Font.render(str(Minutes) + ":0" + str(Seconds), True, BLACK)
    else:
        timer = Timer_Font.render(str(Minutes) + ":" + str(Seconds), True, BLACK)

    Percentage = round((3 - Minus_Score) / 3 * 100)  # 정확도
    MusicName = Music_Font.render("swing swing", True, BLACK)  # 음악 제목
    ScoreNum = Percentage_Font.render(str(Percentage) + " %", True, BLACK)  # 점수

    Screen.blit(MusicName, (10, 45))
    Screen.blit(timer, (265, 55))
    Screen.blit(ScoreNum, (1160, 45))

    pygame.draw.rect(Screen, (0, 0, 0), [12, 10, 1256, 25], 3)  # 타이머바 틀
    pygame.draw.rect(Screen, (255, 255, 255), [15, 13, Elapsed_Time * 7.70, 19])  # 타이머바

    ######################################################################
    # 노드가 나오는 간격을 잡아주는 코드
    Elapsed_Time = (pygame.time.get_ticks() - Start_Ticks) / 1000

    if (SectionNum == 1):
        if (Elapsed_Time < SongSection[0][0]):
            Song_DelaySec = SongSection[0][1]
            SectionNum += 1


    elif (1 < SectionNum < len(SongSection) + 1):
        if (SongSection[SectionNum - 2][0] < Elapsed_Time < SongSection[SectionNum - 1][0]):
            Song_DelaySec = SongSection[SectionNum - 1][1]
        elif (Elapsed_Time == SongSection[SectionNum - 1][0]):
            SectionNum += 1
            #################################

    # 그 간격에 따라서 노드가 나오도록 설정
    Now_Time = pygame.time.get_ticks()
    if (Now_Time > Song_Time + Song_DelaySec):
        Song_Time = Now_Time
        ###################### 노드 추가 ##########################
        if Pose_Index == -1:
            Pose_Index = random.randrange(0, 2)
            Node_Index = 0

        # 왼쪽 노드 추가하기
        if random.randrange(0, 2):
            queue_Node.append(MakeNode(1, Pose_Index, Node_Index))

        # 오른쪽 노드 추가하기
        else:
            queue_Node.append(MakeNode(0, Pose_Index, Node_Index))
            Node_Index += 1

        if Node_Index == 2:
            Pose_Index = -1
        ##########################################################
    ######################################################################
    # fade out
    BlackScreen.set_alpha(OpacityLevel)
    Screen.blit(BlackScreen, (0, 0))

    if (OpacityLevel > 0):
        OpacityLevel -= 3

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
sys.exit()