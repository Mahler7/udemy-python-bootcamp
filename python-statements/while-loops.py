x = 0
while x < 10:
    print('x is currently:', x)
    x += 1
else: 
    print("All Done")

y = 0
while y < 10:
    print('y is currently:', y)
    print('y is still less than 10, adding 1 to y')
    y += 1
    if y == 3:
        print("y = 3")
    else:
        print('continuing ...')
        continue

z = 0
while z < 10:
    print('z is currentlz:', z)
    print('z is still less than 10, adding 1 to z')
    z += 1
    if z == 3:
        print("z = 3")
        break
    else:
        print('continuing ...')
        