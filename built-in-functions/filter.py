def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

lst = range(10)
filter_function = list(filter(even_check, lst))
print(filter_function)

filter_lambda = list(filter(lambda num: num % 2 == 0, lst))
print(filter_lambda)

filter_lambda2 = list(filter(lambda num: num > 3, lst))
print(filter_lambda2)
