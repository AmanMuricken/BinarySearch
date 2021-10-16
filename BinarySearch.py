def binarySearch(arr,start,end,x):
    if end>=start:
        mid = start+(end-start)//2
        if arr[mid]==x:
            return mid

        elif arr[mid]>x:
            return binarySearch(arr,start,mid-1,x)
        else:
            return binarySearch(arr,mid+1,end,x)
    else:
        return -1

arr = [0,1,2,3,6,10,12,15,20,25]
print(arr)
x = int(input("Which element do u want:"))
result = binarySearch(arr,0,len(arr)-1,x)

if result!=-1:
    print("The element found at that position:",result)
else:
    print("the element not found")