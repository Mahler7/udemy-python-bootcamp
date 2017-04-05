x = 25

def printer():
    x = 50
    return 50

print(x)
print(printer())

name = 'This is a global name'
def greet():
    name = 'Sammy'
    def hello():
        print('Hello', name)
    hello()
greet()

y = 50

def func(y):
    print('y is:', y)
    y = 2
    print('changed local y to:', y)
func(y)
print('y is still:', y)

def func():
    global y
    print('y is global:', y)
    y = 2
    print('changed global y to:', y)
print('before calling func() y is:', y)
func()
print('value of y outside func() is changed to:', y)
