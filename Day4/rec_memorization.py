memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        res = 1
    else:
        res = fib(n-1) + fib(n-2)
    memo[n] = res
    print(memo)
    print(res)
    return res

print(fib(5))