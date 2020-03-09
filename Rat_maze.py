#Rat's maze problem where he rat must navigate from source to destination through open pathways
N = 5
maze = [
    [0,1,0,1,1],
    [0,0,0,0,0],
    [1,0,1,0,1],
    [0,0,1,0,0],
    [1,0,0,1,0]
]

dest=[3,4]
sol=[[0 for i in range(N)]for j in range(N)]

def Mazy(row, col, path, num):
    if(row==dest[0] and col==dest[1]):
        maze[3][4]=99
        print("Length of path is :", path)
        for x in range(N):
            for y in range(N):
                print(maze[x][y], end=" ")
            print()
        return True
    else:
        if(row>=0 and row<N and col>=0 and col<N and maze[row][col]==0 and maze[row][col]!=99):
            maze[row][col]=99
            if(Mazy(row-1, col,path, num)):
                return True
            if(Mazy(row,col-1, path, num)):
                return True
            if(Mazy(row+1,col,path, num)):
                return True
            if(Mazy(row, col+1, path, num)):
                return True
            maze[row][col]=0
            return False
    
    

if(Mazy(0,0,1,0)==False):
    print("No path")

