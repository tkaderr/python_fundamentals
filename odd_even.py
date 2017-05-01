# def odd_even():
#     for i in range(1,2001):
#         if i%2==0:
#             print"{} is even".format(i)
#         else:
#             print"{} is odd".format(i)
# odd_even()

# def multiplier(arr,num):
#     for i in range(0,len(arr)):
#         arr[i]=arr[i]*num
#     return arr
#
# a = [2,4,10,16]
# b=multiplier(a,5)
# print b

def layered_multiples(arr,num):
    newarr=[]
    for i in range(0,len(arr)):
        arr[i]=arr[i]*num
    print arr
    for x in range(0,len(arr)):
        for y in range(0,arr[x]):
            newarr.append(1)
        arr[x]=newarr
        newarr=[]
    print arr

a = [2,4,5]
layered_multiples(a,3)
