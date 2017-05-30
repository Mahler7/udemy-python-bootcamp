def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

l = ['a','b','c']
count = 0
for item in l:
    print(count)
    print(item)
    count += 1

for count, item in enumerate(l):
    print(count)
    print(item)

for count, item in enumerate(l):
    if count >= 2:
        break
    else:
        print(item)


