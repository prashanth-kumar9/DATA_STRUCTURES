# recursion.py
# Basic recursion examples


def printFunc(n): 
 if n == 0:     # this is the terminating base case 
    return 0 
 else: 
    print (n) 
    return printFunc(n-1)         # recursive call to itself again 
print(printFunc(4))