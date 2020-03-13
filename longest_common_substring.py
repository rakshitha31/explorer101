#Longest common substring
#Algorithm- if letters match, diagonal value+1;else 0

#Recusive 
def rec(str1, str2, len1, len2, count):
    if( len1==0 or len2==0 ):
        return count
    if(str1[len1-1]== str2[len2-2]):
        count = rec(str1, str2, len1-1, len2-1, count+1)
    count = max(count, max( rec(str1, str2, len1-1, len2,0), rec( str1, str2, len1, len2-1,0)))

    return count

#Dynamic programming
def dyn(str1, str2,len1, len2):
    storage= [[0 for i in range(len1+1)]for j in range(len2+1)]
    max=0
    for i in range(1, len(storage)):
        for j in range(1, len(storage[0])):
            if(str1[j-1] == str2[i-1]):
                storage[i][j]= storage[i-1][j-1]+1
            else:
                storage[i][j]=0
            if(storage[i][j] > max):
                max= storage[i][j]
               
    return max
if __name__ == "__main__":
    str1 = "abcdaf"
    str2="zbcdf"

    ans1= rec(str1, str2, len(str1), len(str2), 0)
    print("From recursion", ans1)

    ans2=  dyn(str1, str2, len(str1), len(str2))
    print("From DP", ans2)
