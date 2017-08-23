


// Returns the count of ways we can sum  S[0...m-1] coins to get sum n
def count( S[],  m,  n )

    // If n is 0 then there is 1 solution (do not include any coin)
    if (n == 0)
        return 1;
     
    // If n is less than 0 then no solution exists
    if (n < 0)
        return 0;
 
    // If there are no coins and n is greater than 0, then no solution exist
    if (m <=0 && n >= 1)
        return 0;
 
    // count is sum of solutions (i) including S[m-1] (ii) excluding S[m-1]
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] );







#							C({1,2,3}, 5)                     
#                           /                \
#                         /                   \              
#             C({1,2,3}, 2)                 C({1,2}, 5)
#            /     \                        /         \
#           /        \                     /           \
#C({1,2,3}, -1)  C({1,2}, 2)        C({1,2}, 3)    C({1}, 5)
#               /     \            /    \            /     \
#             /        \          /      \          /       \
#    C({1,2},0)  C({1},2)   C({1,2},1) C({1},3)    C({1}, 4)  C({}, 5)
#                   / \      / \       / \        /     \    
#                  /   \    /   \     /   \      /       \ 
#                .      .  .     .   .     .   C({1}, 3) C({}, 4)
#                                               /  \
#                                              /    \  
#                                             .      .


def count(S, m, n):

    table = [[0 for x in range(m)] for x in range(n+1)]

    for i in range(m):
        table[0][i] = 1
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
 
            # total count
            table[i][j] = x + y
 
    return table[n][m-1]