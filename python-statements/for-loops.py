l = [1,2,3,4,5]

for element in l:
    print(element)

for element in l:
    print('something')

for num in l:
    if num % 2 == 0:
        print(num)
for num in l:
    if num % 2 == 0:
        print('even number')
    else:
        print('odd number')

list_sum = 0
for num in l:
    list_sum = list_sum + num

print(list_sum)

s = 'this is a string'
for letter in s:
    print(letter)

tup = (1,2,3,4,5)

for t in tup:
    print(t)

t = [(2,4),(6,8),(10,12)]
for tup in t:
    print(tup)

for (t1, t2) in t:
    print(t1)

d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)

for k, v in d.items():
    print(k)
    print(v)



