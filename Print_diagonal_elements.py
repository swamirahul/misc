Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

For Example:
If the matrix is    

1 2 3
4 5 6
7 8 9
The output should Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
i.e print the elements of array diagonally.

Note: The input array given is in single line and you have to output the answer in one line only.

 

Input:

The first line contains an integer T, depicting total number of test cases. 
Then following T lines contains an integer N depicting the size of square matrix and next line followed by the value of array.


Output:

Print the elements of matrix diagonally in separate line.


Constraints:

1 ≤ T ≤ 30
1 ≤ N ≤ 20
0 ≤ A[i][j] ≤ 9


Example:

Input:
2
2
1 2 3 4
3
1 2 3 4 5 6 7 8 9
Output:
1 2 3 4
1 2 4 3 5 7 6 8 9
#code

def sumarrary(somelist,tempsum):
    sumlist=[]
    for x in somelist:
        if x[0]+x[1]==tempsum:
            sumlist.append(x)
    return sumlist
def finacal(matrixlist,N):
    matrix=[]
    finallist=[]
    ## One line code to Generate matrix from list elements
    matrix=[matrixlist[i:i+N] for i in range(0, len(matrixlist), N)]
    # Generate all combination of index eg. for 2X2 matrix [1,1] [1,2] [2,1] [2,2]
    # for 3X3 matrix 
    for i in range(1,N+1):
        for j in range(1,N+1):
            finallist.append([i,j])
    
    newfinallist=[]
    newfinallistarray=""
    
    # This is the heart of the problem return the index whose sum is 
    # first diagonal element sum 2 [1,1]
    # second diagonal element sum 3 [1,2] [2,1]
    # third diagonal element sum 4 [2,2]
    
    
    for i in range(2,N+N+1):
        newfinallist.extend(sumarrary(finallist,i))
        
    for x in newfinallist:
        newfinallistarray=newfinallistarray+str(matrix[x[0]-1][x[1]-1])+" "
    return newfinallistarray.strip()

T=int(input().rstrip().split()[0])
while T>0:
    N=int(input().rstrip().split()[0])
    matrixlist = []
    matrixlist=[int(x) for x in input().split()]
    print(finacal(matrixlist,N))
    T=T-1



