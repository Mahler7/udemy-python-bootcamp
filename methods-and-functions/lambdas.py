def square(num):
    result = num ** 2
    return result

print(square(2))

def square(num):
    return num ** 2

print(square(3))

def square(num): return num ** 2
print(square(4))

#lambdas
square_lambda = lambda num: num**2
print(square_lambda(10))

even = lambda num: num % 2 == 0
print(even(4))

first = lambda str: str[0]
print(first('hello'))

rev = lambda s: s[::-1]
print(rev('hello'))

adder = lambda x, y: x + y
print(adder(3,4))

len_check = lambda item: len(item)
print(len_check('how many chars does this string have?'))


