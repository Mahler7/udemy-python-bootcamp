def fahrenheit(T):
    return (9.0 / 5) * T + 32

temp = [0, 22.5, 40, 100]

conversions = list(map(fahrenheit, temp)) #must use list in Python 3
print(conversions)

lambda_conversion = list(map(lambda T: (9.0 / 5) * T + 32, temp))
print(lambda_conversion)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

multiple_lists = list(map(lambda x,y,z: x + y + z, a, b, c))
print(multiple_lists)

negatives = list(map(lambda num: num * -1, a))
print(negatives)


