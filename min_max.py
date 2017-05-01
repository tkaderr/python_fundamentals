def min_max(arr):
    max_val=arr[0]
    min_val=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>max_val:
            max_val=arr[i]
        if arr[i]<min_val:
            min_val=arr[i]
    print (max_val)
    print (min_val)

min_max([1,2,0,4])
