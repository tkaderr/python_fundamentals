# Multiples

#Part 1
for i in range(0,1001):
    print(i)

#Part2
for i in range(5,1000001):
    if i%5!=0:
        continue
    else:
        print(i)

# Sum list
def sum_list(arr):
    sum_val=arr[0]
    for i in range(1,len(arr)):
        sum_val=sum_val+arr[i]
    print sum_val

sum_list([1,2,3])

#Average list
def average_list(arr):
    sum_list=arr[0]
    for i in range(1,len(arr)):
        sum_list=sum_list+arr[i]
    return sum_list/len(arr)
