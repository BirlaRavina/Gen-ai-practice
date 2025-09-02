from doctest import testmod

def fac(n):
    '''
    varifing the process of finding factorial
    >>> fac(5)
    120
    '''
    i = 1
    res = 1
    while n>=i:
        res = res*i
        i+=1

    return res

if __name__ == '__main__':
    testmod(name ='fac', verbose = False) 

def addNumbers(a, b):
    '''
    adding two numbers
    >>> addNumbers(20, 45)
    65
    >>> addNumbers(30, 20)
    50
    '''
    return a+b
if __name__ == '__main__':
    testmod(name='addNumbers', verbose=False)