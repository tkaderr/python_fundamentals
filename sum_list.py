def sum_list(arr):
    sum_val=arr[0]
    for i in range(1,len(arr)):
        sum_val=sum_val+arr[i]
    print sum_val

sum_list([1,2,3])
