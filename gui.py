import pygame
import pygame.font
import os
import sys
import traceback
import win32api
import win32con

sys.path.append(os.getcwd())
import gameArena as gameArea
from pygame.locals import *

bl = 1.5
sx1 = 290
sx2 = 290 + 50 * bl
sy1 = 30
sy2 = 30 + 20 * bl
rx1 = 290
rx2 = 290 + 50 * bl
ry1 = 90
ry2 = 90 + 20 * bl
ex1 = 290
ex2 = 290 + 50 * bl
ey1 = 150
ey2 = 150 + 20 * bl
bx1 = 290
bx2 = 290 + 50 * bl
by1 = 210
by2 = 210 + 20 * bl
rectsize = 35
start = 0
pygame.font.init()
pygame.init()


# 初始化棋盘背景
def chessboard(screen):
    background = pygame.image.load('res\象棋背景.png');
    screen.blit(background, (0, 0));


# 获取当前选中棋子的图像并赋值给png
def getchesspicture(project, picturex, picturey):
    png = pygame.image.load('res\WhiteRook.png');
    for i in project.UnitList:
        if i.x == picturex and i.y == picturey:
            if i.UnitID == 'R' and i.owner == 1:
                png = pygame.image.load('res\WhiteRook.png');
            if i.UnitID == 'R' and i.owner == 2:
                png = pygame.image.load('res\BlackRook.png');
            if i.UnitID == 'N' and i.owner == 1:
                png = pygame.image.load('res\WhiteKnight.png');
            if i.UnitID == 'N' and i.owner == 2:
                png = pygame.image.load('res\BlackKnight.png');
            if i.UnitID == 'B' and i.owner == 1:
                png = pygame.image.load('res\WhiteBishop.png');
            if i.UnitID == 'B' and i.owner == 2:
                png = pygame.image.load('res\BlackBishop.png');
            if i.UnitID == 'Q' and i.owner == 1:
                png = pygame.image.load('res\WhiteQueen.png');
            if i.UnitID == 'Q' and i.owner == 2:
                png = pygame.image.load('res\BlackQueen.png');
            if i.UnitID == 'K' and i.owner == 1:
                png = pygame.image.load('res\WhiteKing.png');
            if i.UnitID == 'K' and i.owner == 2:
                png = pygame.image.load('res\BlackKing.png');
            if i.UnitID == 'P' and i.owner == 1:
                png = pygame.image.load('res\WhitePawn.png');
            if i.UnitID == 'P' and i.owner == 2:
                png = pygame.image.load('res\BlackPawn.png');
    return png


# 刷新当前Unitlist中的棋子
def chess(screen, project):
    png = pygame.image.load('res\WhiteRook.png');
    for i in project.UnitList:
        if i.UnitID == 'R' and i.owner == 1:
            png = pygame.image.load('res\WhiteRook.png');
        if i.UnitID == 'R' and i.owner == 2:
            png = pygame.image.load('res\BlackRook.png');
        if i.UnitID == 'N' and i.owner == 1:
            png = pygame.image.load('res\WhiteKnight.png');
        if i.UnitID == 'N' and i.owner == 2:
            png = pygame.image.load('res\BlackKnight.png');
        if i.UnitID == 'B' and i.owner == 1:
            png = pygame.image.load('res\WhiteBishop.png');
        if i.UnitID == 'B' and i.owner == 2:
            png = pygame.image.load('res\BlackBishop.png');
        if i.UnitID == 'Q' and i.owner == 1:
            png = pygame.image.load('res\WhiteQueen.png');
        if i.UnitID == 'Q' and i.owner == 2:
            png = pygame.image.load('res\BlackQueen.png');
        if i.UnitID == 'K' and i.owner == 1:
            png = pygame.image.load('res\WhiteKing.png');
        if i.UnitID == 'K' and i.owner == 2:
            png = pygame.image.load('res\BlackKing.png');
        if i.UnitID == 'P' and i.owner == 1:
            png = pygame.image.load('res\WhitePawn.png');
        if i.UnitID == 'P' and i.owner == 2:
            png = pygame.image.load('res\BlackPawn.png');
        screen.blit(png, (35 * i.x, 35 * (7 - i.y)));


# 从实际点击位置中获取建系坐标
def getposfromreal(i, j):
    if (i < start + rectsize * 8 and i > start and j <= start + rectsize * 8 and j > start):
        rx = (i - start) / rectsize
        ry = (j - start) / rectsize
        return int(rx), 7 - int(ry)
    return -1, -1


# 将建系坐标转化为实际位置
def getrealfrompos(i, j):
    return start + (i) * rectsize, 35 * 7 - (start + (j) * rectsize)


# 画四个按钮
def Draw_a_button(screen):
    button_color = (255, 255, 255)
    pygame.draw.rect(screen, button_color, [sx1, sy1, sx2 - sx1, sy2 - sy1], 1)
    pygame.draw.rect(screen, button_color, [rx1, ry1, rx2 - rx1, ry2 - ry1], 1)
    pygame.draw.rect(screen, button_color, [ex1, ey1, ex2 - ex1, ey2 - ey1], 1)
    pygame.draw.rect(screen, button_color, [bx1, by1, bx2 - bx1, by2 - by1], 1)
    s_font = pygame.font.Font('res\YaHei.Consolas.1.12.ttf', 18)
    text1 = s_font.render("开始游戏", True, button_color)
    text2 = s_font.render("重新开始", True, button_color)
    text3 = s_font.render("退出游戏", True, button_color)
    text4 = s_font.render("悔棋", True, button_color)
    screen.blit(text1, (sx1, sy1))
    screen.blit(text2, (rx1, ry1))
    screen.blit(text3, (ex1, ey1))
    screen.blit(text4, (bx1, by1))


qx = -1
qy = -1  # 这是上一个按键的位置
playing = 0  # 默认1是玩家 2是电脑 0是还没开始玩
flag = 0  # flag表示当前未点击


#  棋子移动动画
def moveflash(gamearea,screen, x1, y1, x2, y2):
    png = getchesspicture(gamearea, x1, y1);
    actx1,acty1=getrealfrompos(x1,y1)
    actx2,acty2=getrealfrompos(x2,y2)
    d1=actx2-actx1;
    d2=acty2-acty1;
    while(actx1!=actx2 or acty1!=acty2):
        chessboard(screen)  # 初始化棋盘背景
        chess(screen, gamearea)  # 刷新当前棋子
        Draw_a_button(screen)  # 画四个按钮
        drawfoucs(gamearea, screen)  # 标识选中和可落子处
        screen.blit(png, (actx1, acty1));
        pygame.display.flip();
        actx1= actx1+d1/10;
        acty1= acty1+d2/10;



# 对选中棋子进行判断和处理
def handleclick(gamearea, screen, i, j):
    global qx, qy
    global playing;
    if (playing == -1 or qx == -1 or qy == -1):  # 判断是不是该玩家 如果是该玩家 并且 上次的坐标不是-1 -1
        return

    for k in gamearea.UnitList:
        if k.x == i and k.y == j:
            if (k.owner == playing):
                return

    for k in gamearea.UnitList:
        if k.x == qx and k.y == qy:
            if (k.owner == 1 + (playing) % 2):
                return
    ok = 0
    for k in gamearea.UnitList:
        if k.x == qx and k.y == qy:
            n = k.getMove(gamearea.getGridInfo())
            for d in n:
                if (d[0] == i and d[1] == j and gamearea.checkMove(qx,qy,d[0],d[1])):
                    ok = 1
    if (ok == 0):
        return
    moveflash(gamearea,screen, qx,qy,i,j)
    gamearea.moveUnit(qx, qy, i, j)

    if gamearea.isend(1 + (playing) % 2):
        gamearea.__init__()
        if playing==1:
            win32api.MessageBox(0, "游戏结束 白方获得胜利", "消息", win32con.MB_OK)
        else:
            win32api.MessageBox(0, "游戏结束 黑方获得胜利", "消息", win32con.MB_OK)
        playing=2

    playing = 1 + (playing) % 2  # 更换玩家
    print(playing)
    '''
    #gamearea.getaimove()
    #


    for k in gamearea.UnitList:
        if (k.UnitID =='K' and k.UnitID==1):
            over=0
    if(over==0):
        pass #结束
    qx=-1
    qy=-1;

    playing=0;
    '''
    # if()  #判断这一个当前位置的棋子是不是玩家的 如果是自己的直接返回
    # 开始走棋  设置当前玩家为电脑询问电脑走棋  电脑走棋 设置为玩家走棋 设置上次坐标为-1 -1,
    # 最后判断是不是游戏结束了


# 标记选中当前棋子和该棋子下一步可走的位置
def drawfoucs(gamearea, screen):
    if (qx != -1 and qy != -1):  # 这里可以标记所有的可行位置
        x, y = getrealfrompos(qx, qy)
        focus_color = (255, 0, 0)
        pygame.draw.rect(screen, focus_color, Rect(x, y, 34, 34), 2)
        focus_color = (0, 255, 0)
        for k in gamearea.UnitList:
            if k.x == qx and k.y == qy:
                d = k.getMove(gamearea.getGridInfo())
                for n in d:
                    if gamearea.checkMove(qx, qy, n[0], n[1]):
                        x, y = getrealfrompos(n[0], n[1])
                        pygame.draw.rect(screen, focus_color, Rect(x, y, 34, 34), 2)


def main():
    # 创建一个窗口
    global playing
    screen = pygame.display.set_mode([380, 280])
    game1 = gameArea.ChessArena()  # 对象game1
    # 设置窗口标题
    pygame.display.set_caption("国际象棋")
    chessboard(screen)  # 初始化棋盘背景
    global qx
    global qy
    playing = 1
    while True:
        chessboard(screen)  # 初始化棋盘背景
        chess(screen, game1)  # 刷新当前棋子
        Draw_a_button(screen)  # 画四个按钮
        drawfoucs(game1, screen)  # 标识选中和可落子处
        pygame.display.flip()
        for event in pygame.event.get():
            # 点击x则关闭窗口
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:  # 当鼠标摁下
                x, y = event.pos[0], event.pos[1]
                if (x > sx1 and x < sx2 and y > sy1 and y < sy2):
                    playing = 1
                if (x > rx1 and x < rx2 and y > ry1 and y < ry2):
                    playing = 1
                    qx, qy = -1, -1
                    del game1
                    game1 = gameArea.ChessArena()
                if (x > ex1 and x < ex2 and y > ey1 and y < ey2):
                    exit(0)
                if (x > bx1 and x < bx2 and y > by1 and y < by2):
                    if (game1.canBack):
                        game1.backLastMove();
                        playing = 1 + (playing) % 2  # 更换玩家
                a, b = getposfromreal(x, y);
                handleclick(game1, screen, a, b)
                if (a >= 0 and a < 8 and b >= 0 and b < 8):
                    qx, qy = a, b
                print(qx, qy)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()