def func1():
    return 1

print(func1())
s = "This is a global variable"

def func():
    print(locals())

print(globals())
print(globals().keys())
print(globals()['s'])

func()

def hello(name="Jose"):
    return "Hello " + name

print(hello())
greet = hello
print(greet)
print(greet())
