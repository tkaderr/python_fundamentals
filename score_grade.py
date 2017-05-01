# import random
#
# def score_grade():
#     counter=10
#     while counter<0:
#     score = random.randint(60,101)
#     if score>=60 and score<=69:
#         print("Score: {}; Your grade is D".format(score))
#     elif score>=70 and score<=79:
#         print("Score: {}; Your grade is C".format(score))
#     elif score>=80 and score<=89:
#         print("Score: {}; Your grade is B".format(score))
#     elif score>=90 and score<=100:
#         print("Score: {}; Your grade is A".format(score))
#     counter-=counter
#
# score_grade()


import random

def grade(reps):
    print "Scores and Grades"
    for x in range(0, reps):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: ", score,"; Your grade is D"
        elif score >= 70 and score <= 79:
            print "Score: ", score, "; Your grade is C"
        elif score >= 80 and score <= 89:
            print "Score: ", score, "; Your grade is B"
        elif score >= 90 and score <= 100:
            print "Score: ", score, "; Your grade is A"
        else:
            print "You failed"
    print "End of the program.  Bye!"

grade(10)
