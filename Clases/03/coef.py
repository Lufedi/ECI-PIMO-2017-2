 C(n, k) = C(n-1, k-1) + C(n-1, k)
 C(n, 0) = C(n, n) = 1



 def binomialCoeff(n , k):
 	if k==0 or k ==n :
    	return 1
    # Recursive Call
    return binomialCoeff(n-1 , k-1) + binomialCoeff(n-1 , k)

n = 5
k = 2
print ("Value of C(%d,%d) is (%d)" %(n , k , binomialCoeff(n , k)))
 



        					 C(5, 2)
                    /                      \
           C(4, 1)                           C(4, 2)
            /   \                          /           \
       C(3, 0)   C(3, 1)             C(3, 1)               C(3, 2)
                /    \               /     \               /     \
         C(2, 0)    C(2, 1)      C(2, 0) C(2, 1)          C(2, 1)  C(2, 2)
                   /        \              /   \            /    \
               C(1, 0)  C(1, 1)      C(1, 0)  C(1, 1)   C(1, 0)  C(1, 1)



# A Dynamic Programming based Python Program that uses table C[][]
# to calculate the Binomial Coefficient
 
# Returns value of Binomial Coefficient C(n, k)
def binomialCoef(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]
 
    # Calculate value of Binomial Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
 
            # Calculate value using previosly stored values
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
 
    return C[n][k]
 
# Driver program to test above function
n = 5
k = 2
print("Value of C[" + str(n) + "][" + str(k) + "] is "
      + str(binomialCoef(n,k)))
 
# This code is contributed by Bhavya Jain

