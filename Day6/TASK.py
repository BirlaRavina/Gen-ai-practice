# Debugg the given Python script:
# def factorial(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n * factorial(n-2)
# def remove_duplicates(lst):
#     return list(set(lst.sort()))
# def second_largest(lst):
#     lst = list(set(lst))
#     lst.sort()
#     return lst[-2]
# print("Factorial of 5:", factorial(5))
# print("Remove duplicates:", remove_duplicates([4,2,2,8,4,6]))
# print("Second largest:", second_largest([10,20,4,20,8,10]))
# Your Tasks:
# 1.Find and explain the bugs
# 2.Fix the code so that:
# factorial(5) returns 120.
# remove_duplicates([4,2,2,8,4,6]) returns [2,4,6,8].
# second_largest([10,20,4,20,8,10]) returns 10


# QUESTION 1 
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)
print("Factorial of 5:", factorial(5))


# question 2
def remove_duplicates(lst):
    # return list(set(lst.sort()))
    print(sorted(list(set(lst))))
    return sorted(list(set(lst)))
print("Remove duplicates:", remove_duplicates([4,2,2,8,4,6]))

# question 3
def second_largest(lst):
    # lst = list(set(lst))
    new_lst = sorted(lst)
    return new_lst[-2]
print("Second largest:", second_largest([5, 5]))