def printFunc(n, r=0):
    """if n == 0 or n==1: # this is the terminating base case
        return 1
    else:
        #print (n)
        return n * printFunc(n-1) # recursive call to itself again"""
    if n==0 or n == 1:
        return r
    temp=n%10
    r=temp*10+r
    printFunc(n/10,r)
    
x=printFunc(4004)
print(x)
'''list1=[1,3, 4,5,6,9]
print(list1.pop())
print(list1)
print(len(list1))'''