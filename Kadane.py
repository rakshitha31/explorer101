#Kadane's algorithm for maxiumum sum subarray problem


def Kadane(array):
    
    global_max = array[0]
    local_max = array[0]
       
    for i in range(1, len(array)): 
        #max of present element and sum of present element and maximum sub array sum until this element
        global_max = max(array[i], global_max + array[i] )
        #max of local max and global max
        local_max=max(local_max, global_max)
    
          
    print(local_max )
   


if __name__ == "__main__":
    array = [-2,1,-3,4,-1,2,1,-5,4]
    Kadane(array)