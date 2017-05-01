# def compare_arr(arr1,arr2):
#     counter=0
#     if len(arr1)!=len(arr2):
#         print("The arrays are not the same")
#     else:
#         for i in range (0,len(arr1)):
#             if arr1[i]==arr2[i]:
#                 continue
#             else:
#                 counter+=counter
#         if counter==0:
#             print "The arrays are the same"
#         else:
#             print "The arrays are not the same"
#
#
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']
#
# compare_arr(list_one,list_two)

def compare_arr(arr1,arr2):
    if arr1==arr2:
        print "The arrays are the same"
    else:
        print "The arrays are not the same"
