# list Comprehension
lst = [i*i for i in range(20) if i%2==0]
print(lst)

# generator expression
lst = (i for i in range(20) if i%2==0)
for i in lst:
    print(i, end='-')

count = (i for i in range(1, 101))
print(count)
for i in count:
    print(i)

    if i == 30:
        break