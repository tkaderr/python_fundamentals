def filter_type(argument):
    if type(argument)==int:
        if argument>=100:
            print("Thats big number")
        else:
            print("Thats a small number")
    elif type(argument)==str:
        if len(argument)>=50:
            print("Long Sentence")
        else:
            print("Short Sentence")
    elif type(argument)==list:
        if len(argument) >=10:
            print("Big List")
        else:
            print("Short List")

si=45
filter_type(si)
