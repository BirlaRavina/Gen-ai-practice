mul = lambda x, y:x*y
print(mul(3,4))

def fun(n):
    return lambda x: x*n
newfun = fun(3)
print(newfun(2))

# Provide an example of a lambda function that sorts a list of tuples by the second value.
lst = [(1,3), (2,2), (2,1)]
print(lst[0][1])
print(sorted(lst, key = lambda x: x[1]))