

def binomialCoeff(n , k):
    if k==0 or k ==n :
        res =  1
    else:
        res = binomialCoeff(n-1 , k-1) + binomialCoeff(n-1 , k)
    return res



n = 5
k = 2
print ("Value of C(%d,%d) is (%d)" %(n , k , binomialCoeff(n , k)))
 
