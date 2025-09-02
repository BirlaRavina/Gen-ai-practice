import time
def decorate(fun):
    def new_fun():
        print("this function adds two numbers")
        start = time.time()
        res = fun(3,5)
        print(res)
        end = time.time()
        print(f"addition is done {end-start:.4f}")
    return new_fun

@decorate
def fun(a, b):
    return (a+b)
fun()