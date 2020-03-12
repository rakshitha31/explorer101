import unittest
import random
import time

matrix = [
    [1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,1,0,0,0],
    [1,0,1,0,1,0,1,0,0,1],
    [0,0,1,0,0,0,0,1,1,0],
    [1,0,0,1,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,1],
    [0,1,1,0,1,0,0,1,1,1],
    [1,1,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0]
]

#matrix=[[random.randint(1,10) for i in range(10)]for j in range(10)]
print(matrix)
N=10
#matrix= [[random.randint(0,1) for i in range(N)] for j in range(N)]
#print(matrix)
zeros={3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
count=0

def count_squence(matrix):
 
    count=0
    for i in range(10):
        for j in range(10):
            if(matrix[i][j]==0):
                count+=1
            else:
                if(count in zeros):
                    zeros[count]+=1
                count = 0 
    
        if(count in zeros):
            zeros[count]+=1
        print(zeros)   
        count=0
        for k in zeros:
            zeros[k]=0
    end= time.time()
    return zeros

