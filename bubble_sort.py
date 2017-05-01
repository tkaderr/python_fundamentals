# def bubble_sort(arr):
#     print arr
#     counter=len(arr)
#     while counter>=0:
#         for i in range(0,counter-1):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#         print arr
#         counter=counter-1
#     print arr

#bubble_sort([4,3,,3,1,7,5])


def bubble_sort(arr):
    print arr
    sortedd=False
    while not sortedd:
        sortedd=True
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                sortedd=False
    print arr

bubble_sort([4,3,3,1,7,5])
