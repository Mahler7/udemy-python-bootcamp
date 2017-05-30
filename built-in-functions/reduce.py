import functools

lst = [47, 11, 42, 13]
add = functools.reduce(lambda x,y: x + y, lst)
print(add)

lst2 = [34,23,24,24,100,2333,2,11]
max_find = lambda a,b: a if (a > b) else b
print(functools.reduce(max_find, lst2))