# Write a Python program to reverse a list without using built-in reverse() or slicing.
def reverse_str(s):
    st = ''
    for i in s:
        st = i+st
    print("reverse string: ", st)
reverse_str("hello world")

print('\n *****************************************')

# Q2. String Manipulation
# Given a string:
# s = "hello world"
# Write code to:
# Count the number of vowels.
# Print the string with each word capitalized ("Hello World").
def manipulate_str(s):
    vowel = 'aeiouAEIOU'
    c = 0
    for i in s:
        if i in vowel:
            c+=1
    print("number of vowels: ", c)
    print("capitalized string: ", s.upper())
manipulate_str("hello world")

print('\n *****************************************')
# Q3. Functions
# Write a function factorial(n) using recursion.
# Test it for n = 5.
def factorial(n):
    fac = 1
    if n == 0 or n == 1:
        return fac
    else: 
        for i in range(1, n+1):
            fac = fac * i
    print("factorial of 5 is : ",fac)
factorial(5)

print('\n *****************************************')

# Q4. File Handling
# Write a program that:
# Reads a file data.txt.
# Counts how many times each word appears.
# Prints the result in descending order of frequency.
def file_handling():
    with open('data.txt', 'r') as f:
        content = f.read()
        dct = {}
        for i in content.split():
            if i not in dct:
                dct[i] = 1
            else: 
                dct[i]+=1
        res = sorted(dct.items(), reverse= True)
        print(res)


file_handling()
 
print('\n *****************************************')

# Q5. OOP (Object-Oriented Programming)
# Create a class BankAccount with:
# Attributes: account_number, balance.
# Methods: deposit(amount), withdraw(amount), display_balance().
# Create an object and test all methods.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        self.balance-=amount
    def display(self):
        print("total amount: ", self.balance)

obj = BankAccount(233455, 200)
obj.deposit(500)   # 200+500 = 700
obj.display()
obj.withdraw(100) #700-100 = 600
obj.deposit(200)
obj.display()

print('\n *****************************************')

# Q6. Sets & Dictionaries
# You have a list of numbers with duplicates:
# nums = [1, 2, 2, 3, 4, 4, 5]
# Write a program to:
# Remove duplicates.
# Count frequency of each number using a dictionary.
def remove_dupl(nums):
    newlst = list(set(nums))
    print("remove duplicates:", newlst)

def freq_numbers(nums):
    dct = {}
    for i in nums:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i]+=1

    print("frequency number: ", dct)
nums = [1, 2, 2, 3, 4, 4, 5]
remove_dupl(nums)
freq_numbers(nums)

print('\n *****************************************')
# Q7. Lambda & Map/Filter/Reduce
# Given a list of numbers [1, 2, 3, 4, 5, 6],
# Use filter to get even numbers.
# Use map to square each number.
# Use reduce to calculate the product of all numbers.
from functools import reduce
def fun(num):
    even_nums = filter(lambda x: x%2 == 0, num)
    square_nums = map(lambda x: x**2, num)
    prod_nums = reduce(lambda x, y: x*y, num)
    print("list of even numbers", list(even_nums),'\n', "list of squares", list(square_nums), '\n',"product of numbers", prod_nums)

num =  [1, 2, 3, 4, 5, 6]
fun(num)

print('\n *****************************************')

# Q8. Exception Handling
# Write a program that asks the user for two numbers and divides them.
# Handle the case when the denominator is zero and when the input is not a number.
def exp_handling():
    a, b = input("enter two numbers: ").split()
    try:
        res = int(a)/int(b)
        print(res)
    except ZeroDivisionError:
        print("zero division error")
    except Exception as e:
        print(e)

exp_handling()

print('\n *****************************************')

# Q9. Generators
# Write a generator function even_numbers(n) that yields even numbers up to n.
# Example: list(even_numbers(10)) → [2, 4, 6, 8, 10].
def even_numbers(n):
    for i in range(1, n+2):
        if i%2 == 0:
            yield i
lst = list(even_numbers(10))
print("even number's list",lst)

print('\n *****************************************')
# Q10. Real-World Style
# You are given a list of employees with their department:
# employees = [
#     ("Alice", "HR"),
#     ("Bob", "IT"),
#     ("Charlie", "Finance"),
#     ("David", "IT"),
#     ("Eva", "HR")

# ]
# Write a Python program to group employees by department and print results like:
# HR: Alice, Eva
# IT: Bob, David
# Finance: Charl
def group_emp(emp):
    dct = {}
    for i in range(len(emp)):
        if emp[i][1] not in dct:
            dct[emp[i][1]] = [emp[i][0]]
        else:
            dct[emp[i][1]].append(emp[i][0])
    print(dct)
employees = [
    ("Alice", "HR"),
    ("Bob", "IT"),
    ("Charlie", "Finance"),
    ("David", "IT"),
    ("Eva", "HR"),
    ('abc')
]
group_emp(employees)
        
def add(a):
    if a%2 == 0:
        return a
l = [2,3,4,5]
res = filter(add, l)
print(list(res))