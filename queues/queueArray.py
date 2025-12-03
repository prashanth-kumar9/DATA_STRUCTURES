def maxofw(arr1, w):
    c=0
    b=[]
    for i in range(len(arr1)-w+1):
        for j in range(w):
            if arr1[i+j]>c:
                c=arr[i+j]
        b.append(c)
    return b

arr=[1, 3, -1, -3, 5, 3, 6, 7]
w=3
result=maxofw(arr, w)
print(result)
                