
def exchange(zeroboard,locat,collision, row, queen_num):
    best=collision[0]
    new_locat=0
    for i in range(0,queen_num):
        if collision[i]<=best:
            best=collision[i]
            new_locat=i
    zeroboard[row][locat[row]]=0
    zeroboard[row][new_locat] = 1
    locat[row]=new_locat

    return zeroboard

