""" conditional.py file is for the practice purpose on the 'if, elif, else' topics.
    So, we are going to create function that should return True if
    2 or more of the parameters are equal, and false if none of them are equal to any of the others.
"""

#print('a')
print('a:')
a = input()

print('b:')
b = input()

print('c:')
c = input()

def condition(a, b, c):
    if (a == b or b == c or c == a):
        #if (a == "" or b == "" or c == ""):
        a = int()
        b = int()
        c = int()
        print (True)
    elif (a == b and b == c and c == a):
        #if (a == "" or b == "" or c == ""):
        a = int()
        b = int()
        c = int()
        print (True)
    else:
        print (False)


condition(a,b,c)
