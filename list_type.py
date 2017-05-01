def list_type(arr):
    str_count=0
    int_count=0
    sum_val=0
    str_arr=" "
    for i in arr:
        if type(i)==str:
            str_count+=1
            str_arr=str_arr+" "+i
        if type(i)==int:
            int_count+=1
            sum_val=sum_val+i
    if str_count>0 and int_count==0:
        print("The array is string type")
    elif int_count>0 and str_count==0:
        print("The array is int type")
    else:
        print("The array is mixed type")
    print(str_arr)
    print(sum_val)

l = ['magical','unicorns',53]
list_type(l)
