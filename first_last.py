
def first_last(arr):
    newarr=[]
    print("first value is {} and the last value is {}".format(arr[0],arr[len(arr)-1]))
    newarr.append(arr[0])
    newarr.append(arr[len(arr)-1])
    print(newarr)

first_last([1,2,3,4])
