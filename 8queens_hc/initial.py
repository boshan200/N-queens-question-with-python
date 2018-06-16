import random



def init(zeroboard, queen_locat, queen_num):
    #這裡要把棋盤清空
    for i in range(0,queen_num):
        for j in range(0,queen_num):
            zeroboard[i][j] =0

    for row in range(0, queen_num):
        rand_col = random.randint(0, queen_num-1)
        zeroboard[row][rand_col]=1
        queen_locat[row]=rand_col
    return zeroboard
