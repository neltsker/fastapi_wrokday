import random

board1 =  [[],[]]
board2 =  [[],[]]
def get_shot():
    pass
def give_shot():
    pass

def set_warships(board):
    i,j = random.randin(0,9), random.randin(0,9)
    while r<20:
        if board[i][j]==0:
            board[i][j]=1
            r+=1
            i,j = random.randin(0,9), random.randin(0,9)
        else:
            i,j = random.randin(0,9), random.randin(0,9)


def showboard():
    pass            

def game():
    for i in range(10):
        for j in range(10):
            board1[i][j]=0
            board2[i][j]=0
    set_warships(board1)
    
    
    

def main():
    pass


