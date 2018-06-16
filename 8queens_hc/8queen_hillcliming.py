import initial
import search
import board
local=1
board_max=input("請輸入皇后數目:")
board_max=int(board_max)
zeroboard =[[0]*board_max for i in range(0,board_max)]
collision=[0]*board_max
queen_locat = [0]*board_max
while (local>=1):

    local=0
    zeroboard=initial.init(zeroboard,queen_locat, board_max)                  #棋盤初始化
    print('此為初始化後的棋盤')
    for j in range(0,board_max):
        print(zeroboard[j],'\n')
    print('----------------------------------\n')

    for max in range(0,8):
        for row in range(0,board_max):
            for col in range(0,board_max):
                collision[col]=search.calc_collision(row,col,zeroboard, board_max)
            zeroboard=board.exchange(zeroboard, queen_locat, collision, row, board_max)                 #做棋盤交換

    print('此為交換後的棋盤')
    for j in range(0, board_max):
        print(zeroboard[j], '\n')
    print('----------------------------------\n')

    for row in range(0, board_max):                     #最後檢查
            if search.calc_collision(row, queen_locat[row], zeroboard, board_max) != 0:
                local+=1






