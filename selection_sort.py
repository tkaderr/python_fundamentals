def selection_sort(arr):
    counter=len(arr)
    counter_range=0
    while counter>0:
        min_val=arr[counter_range]
        for i in range(counter_range,len(arr)):
            if arr[i]<min_val:
                min_val=arr[i]
                index=i
        arr[counter_range],arr[index]=arr[index],arr[counter_range]
        counter=counter-1
        counter_range=counter_range+1
        index=counter_range
        print "{}:the counter is {}".format(arr,counter_range)
    print arr

selection_sort([4,3,3,1,7,5])
