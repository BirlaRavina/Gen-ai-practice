hash_table = [None]*10
def hash_fun(name):
    sum_char = 0
    for char in name:
        sum_char += ord(char)
    index = sum_char %10
    return index


def add_value(name):
    index = hash_fun(name)
    hash_table[index] = name

def conatin_value(value):
    index = hash_fun(value)
    return hash_table[index] == value, index

add_value("Bob")
add_value("Dos")
res, index = conatin_value("Dos")
print("contain value with index ",res, index)
print(hash_table)


# lst = [[]]*10
lst = [[], [], [], [], [], [], [], [], [], []]
def hash_fun2(value):
    sum_char = 0
    for char in value:
        sum_char+=ord(char)
    index = sum_char%10
    print(index)
    return index

def add_value2(name):
    index = hash_fun2(name)
    lst[index].append(name)

def conatin_value2(value):
    index = hash_fun2(value)
    return value in lst[index]
add_value2("Bob")
add_value2("boB")
add_value2("abc")
print(conatin_value2("boB"))
print(lst)