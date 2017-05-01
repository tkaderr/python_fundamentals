def average_list(arr):
    sum_list=arr[0]
    for i in range(1,len(arr)):
        sum_list=sum_list+arr[i]
    return sum_list/len(arr)
