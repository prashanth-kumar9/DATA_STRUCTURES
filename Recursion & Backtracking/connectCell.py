def getValAt(cA, ci, cj, L, H):
    if (ci< 0 or ci >= L or cj< 0 or cj >= H): 
        return 0 
    else: 
        return cA[ci][cj]
def findMaxSize(mA, ri, cj,L, H, size):
    global ContArray
    global maxSize
    if ri>L or cj>H:
        return
    
    ContArray[ri][cj]=1
    size=size+1
    if size>maxSize:
        maxSize=size
        print(maxSize)
    tmpArray=[[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    for i in range (0,7):
        print("loop", i)
        ni=ri+tmpArray[i][0]
        nj=cj+tmpArray[i][1]
        val=getValAt(mA, ni, nj, L, H)
        if val>0 and ContArray[ni][nj]==0 :
            print("check")
            findMaxSize(mA, ni, nj, L, H, size)
        
    return
def maxConnectCell(A,r, c):
    global size
    global maxSize
    global ContArray
    for i in range(0,r):
        for j in range(0,c):
            if A[i][j]==1:
                findMaxSize(A,i,j,r, c,size)
                return maxSize
    
zarr=[[1,1,0,0,0],[1,1,0,0,0],[0,1,0,0,1],[0,1,0,0,0],[0,1,0,1,1]] 
rmax = 5
colmax =  5 
maxSize=0 
size=0 
ContArray=rmax*[colmax*[0]] 
print ("Number of maximum 1s are ") 
print (maxConnectCell(zarr, rmax, colmax)) 