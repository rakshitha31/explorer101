#Knight's tour problem
#2 constraints- the new locations should be within limits of a Knight's movement, can move only within N*N matrix
N = 8

sol=[[0 for i in range(N)]for j in range(N)]
pathrow=[2, 1, -1, -2, -2, -1, 1, 2]
pathcol=[1, 2, 2, 1, -1, -2, -2, -1]
row=0
col=0
sol[1][2]=1
def isValidPath(sol, new_row, new_col):
    if(new_row>=0 and new_row<N and new_col>=0 and new_col<N and sol[new_row][new_col]==0):
        return True
    return False


def knight_tour(sol,row,col,move):
    if(move==64):
        #print path i.e solution matrix
        for i in range(N):
            for j in range(N):
                print(sol[i][j], end=" ")
            print()
        return True
    else:
        #check for other available paths
        for m in range(len(pathrow)):
            #update new location of knight
            new_row=row+pathrow[m]
            new_col=col+pathcol[m]
            #CHeck if new location is valid
            if(isValidPath(sol, new_row, new_col)):
                move=move+1
                sol[new_row][new_col]=move
                #explore other paths by recursive call to go to new path
                if(knight_tour(sol, new_row, new_col,move)):
                    return True
                #if path not valid, backtrack one step and go to other path from that location
                else:
                    move=move-1
                    sol[new_row][new_col]=0
    return False
      
knight_tour(sol,0,0,1)
