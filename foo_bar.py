def foo_bar():
    for i in range(100,120):
        for x in range(2,i):
            if i%x==0:
                prime_count=0
                break
            else:
                prime_count=1
        for x in range(2,i):
            if x*x==i:
                perfect_count=1
                break
            else:
                perfect_count=0
        if prime_count==1 and perfect_count==1:
            print "{} is foobar".format(i)
        if prime_count==1 and perfect_count==0:
            print "{} is foo".format(i)
        if prime_count==0 and perfect_count==1:
            print "{} is bar".format(i)
        prime_count=0
        perfect_count=0

foo_bar()
