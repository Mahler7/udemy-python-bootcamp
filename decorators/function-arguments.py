def hello():
    return "Hi Jose!"

def other(func):
    print("Other code goes here")
    print(func())

print(other(hello))

def new_decorator(func):
    def wrap_func():
        print("Code here before executing the func()")
        func()
        print("Code here will excute after the func()")
    return wrap_func

def func_needs_decorator():
    print("This function needs a decorator")

print(func_needs_decorator())
func_needs_decorator = new_decorator(func_needs_decorator)
print(func_needs_decorator())

@new_decorator
def func_needs_decorator():
    print("This function needs a decorator")
print(func_needs_decorator())
