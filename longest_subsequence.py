#Finding the longest common subsequence between two strings recurseively and using DP
#subsequece is a sequence of characters with same relative order 
#Algorithm - if letters match, 1+ value of diagonal; if not, max(top cell and left cell values)

#Using recursion 
def longest_subsequence_recursion(str1, str2, len1, len2):
    if( len1==0 or len2==0 ):
        return 0
    elif(str1[len1-1] == str2[len2-1]):
        return (1+ longest_subsequence_recursion(str1, str2, len1-1, len2-1))
    else:
        return max( longest_subsequence_recursion(str1, str2, len1-1, len2),
        longest_subsequence_recursion(str1, str2, len1, len2-1))

#using DP 
#Basically a matrix to store previous results of every copmared length between str1 and str2 instead of just returning the values as done in recursion
def longest_subsequence_dynamic(str1, str2 , len1, len2):
    storage= [[0 for i in range(len1+1)]for j in range(len2+1)]
    for i in range(1,len(storage)):
        for j in range(1,len(storage[0])):
            if(str1[j-1] == str2[i-1]):
                storage[i][j]=(1 + storage[i-1][j-1])
            else:
                storage[i][j] = max(storage[i-1][j], storage[i][j-1])
            
    return storage[-1][-1]

                
if __name__ == "__main__":
    str1 = "abcdaf"
    str2 = "acbcf"

    ans_rec = longest_subsequence_recursion(str1, str2, len(str1), len(str2))
    print("From recursion ", ans_rec)

    ans_dp = longest_subsequence_dynamic( str1, str2, len(str1), len(str2) )
    print("From DP ", ans_dp)

