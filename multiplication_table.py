def mult_table():
    for i in range (0,13):
        string=""
        for x in range (0,13):
            string=string+str(i*x)
        print (string)

mult_table()
