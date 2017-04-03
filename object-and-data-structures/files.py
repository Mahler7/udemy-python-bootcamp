f = open('test.txt')
print_file = f.read()
f.seek(0)
f.readlines()
print(print_file)

g = open('test2.txt', 'w+')
g.write("This is a new line")
printg = g.read()
print(printg)


