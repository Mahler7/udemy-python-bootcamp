def zip(*iterables):
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

lst = range(1,11)
print(list(zip(lst)))

x = [1,2,3]
y = [4,5,6]
z = [4,5,6,7,8]

tuple_list = list(zip(x,y))
print(tuple_list)

a = [1,2,3,4,5]
b = [2,2,10,1,1]

for pair in list(zip(a, b)):
    print(max(pair))

#removes tuple, and puts in list
remove_tuple = list(map(lambda pair: max(pair), list(zip(a,b))))
print(remove_tuple)

uneven = list(zip(x,z))
print(uneven)

d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

dic_list_keys = list(zip(d1,d2))
print(dic_list_keys)

dic_list_values = list(zip(d1.values(), d2.values()))
print(dic_list_values)

def switcharoo(d1,d2):
    dout = {}
    for d1key,d2val in list(zip(d1, d2.values())):
        dout[d1key] = d2val
    return dout

print(switcharoo(d1,d2))