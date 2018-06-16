
def calc_collision(row,col,zeroboard, queen_num):      #沒有改變棋盤
    collision=0
    for rr in range(1,queen_num):
        if (row+rr)<queen_num:
            if zeroboard[row+rr][col]==1:
                collision+=1
        if (row + rr)<queen_num and(col+rr) < queen_num:
            if zeroboard[row+rr][col+rr]==1:
                collision += 1
        if (row - rr) >= 0 and (col + rr) < queen_num:
            if zeroboard[row-rr][col+rr]==1:
                collision += 1
        if (row + rr) < queen_num and (col - rr) >= 0:
            if zeroboard[row+rr][col-rr]==1:
                collision += 1
        if (row - rr) >= 0:
            if zeroboard[row-rr][col]==1:
                collision += 1
        if (row - rr) >= 0 and (col - rr) >= 0:
            if zeroboard[row-rr][col-rr]==1:
                collision += 1
    return collision