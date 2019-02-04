""" conditional.py file is for the practice purpose on the 'if, elif, else' topics.
    So, we are going to create function that should return True if
    2 or more of the parameters are equal, and false if none of them are equal to any of the others.
"""


def condition(a, b, c):
    if (int(a) == int(b) or int(b) == int(c) or int(c) == int(a)):       
        print (True)
    else:
        print (False)


condition(1,"2",3)
condition(4,"2",4)
condition(1,"1",1)


