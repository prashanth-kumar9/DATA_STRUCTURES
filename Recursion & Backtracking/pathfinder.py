def pathFinder(A, p, size):
    if p==(size-1, size-1):
        return [(size-1, size-1)]
    x,y=p
    if x+1<size and A[x+1][y]==1:
        a=pathFinder(A, (x+1, y), size)
        if a != None:
            print("the trace back to {} {}".format(x, y))
            return [(x,y)]+a
    if y+1<size and A[x][y+1]==1:
        b=pathFinder(A, (x, y+1), size)
        if b != None:
            print("the trace back to {} {}".format(x, y))
            return [(x,y)]+b



Matrix = [[ 1 , 1 , 1, 1 , 0], [ 0 , 1 , 0, 1 , 0], [ 0 , 1 , 0, 1 , 0], [ 0 , 1 , 0, 0 , 0], [ 1 , 1 , 1, 1 , 1] ] 
print (pathFinder(Matrix,(0,0),5))