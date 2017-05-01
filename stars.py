#Part 1
def stars(arr):
    stars_str= ""
    letter_str=""
    temp_str=""
    for i in range (0,len(arr)):
        if type(arr[i])==str:
            letter_str=letter_str+arr[i]
            for y in range(0,len(letter_str)):
                    temp_str=temp_str+letter_str[0]
            print temp_str
            temp_str=""
            letter_str=""
        if type(arr[i])==int:
            for x in range(0,arr[i]):
                stars_str=stars_str+"*"
            print stars_str
            stars_str=""

stars([5,4,2,"cat"])
