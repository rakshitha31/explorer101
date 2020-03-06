#Number of queens
print ("Enter the number of queens")
N = int(input())

#chesssol
#NxN matrix with all elements 0
sol = [[0 for i in range(N)]for j in range(N)]

def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if sol[i][k]==1 or sol[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if sol[k][l]==1:
                    return True
    return False

def N_queen(n):
    #if n is 0, solution found
    if n==0:
        for x in range(N):
            for y in range(N):
                print(sol[x][y], end=" ")
            print()
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(is_attack(i,j))) and (sol[i][j]!=1):
                sol[i][j] = 1
                #recursion
                #wether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True
                sol[i][j] = 0

    return False

N_queen(N)
