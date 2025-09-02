lst = [2, 3,4 ,5,6]
newlst = iter(lst)
print(next(newlst))
print(next(newlst))
for i in newlst:
    print(i)