import random
import time
import numpy as np
N=8

#g=[[random.randint(0,1) for i in range(N)] for j in range(N)]
#g=[[0,1,1,0],[0,1,1,1],[1,0,0,1],[0,0,1,0]]
g=np.array([[0,1,1,1,1,0,0,0],[1,0,0,0,0,1,0,0],[1,0,0,0,0,1,0,0],[1,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0],[0,1,1,0,0,0,0,1],[0,0,0,1,1,0,0,1],[0,0,0,0,0,1,1,0]])
s=0

marked=[False for i in range(N)]
#print(g)
#print(marked)

def bfs(g,s):
    queue=[]
    queue.append(s)
    marked[s]=True   
    while queue:
        #print(queue)
        val=queue.pop(0)
        print(val)
        for i in range(N):
            #print(matrix[i],end=" ")
            #print(marked[i])
            if (g[val][i]==1 and marked[i]==False):
                queue.append(i)
                #print(queue)
                marked[i]=True
                

start=time.time()        
bfs(g,s)
print("Time taken: ",time.time()-start)