def name_of_function():
    pass

name_of_function()

def my_addition_func(arg1, arg2):
    """
    Here is my docstring.
    """
    print(arg1 + arg2)

my_addition_func(1, 2)

def say_hello(name):
    print('hello', name)

say_hello('Jose')

def add_num(num1, num2):
    return num1 + num2

print(add_num(2,3))

def is_prime(num):
    """
    INPUT: A Number
    OUTPUT: A print statement that tells you if a number is prime.
    """
    for n in range(2, num):
        if num % n == 0:
            print(n, 'Not Prime')
            break
    else:
        print(num, 'The number is prime')        

is_prime(13)

