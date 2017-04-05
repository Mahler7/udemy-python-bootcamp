l = []
for letter in 'word':
    l.append(letter)

print(l)

k = [letter for letter in 'word']
print(k)

j = [x**2 for x in range(0,11)]
print(j)

i = [number for number in range(11) if number % 2 == 0]
print(i)

celsius = [0,10,20.1,34.5]
fahrenheit = [temp * (9/5) + 32 for temp in celsius]
print(fahrenheit)

h = [x**2 for x in [x**2 for x in range(11)]]
print(h)
