def compare_str(arr,char):
    arrnew=[]
    for i in arr:
        for x in range(0,len(i)):
            if i[x]==char:
                arrnew.append(i)
                break
    print arrnew


l = ['hello','world','my','name','is','Anna']
char = 'o'

compare_str(l,char)
