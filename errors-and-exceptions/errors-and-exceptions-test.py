###Problem 1 Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('The data type is not correct.')

###Problem 2 Handle the exception thrown by the code below by using **try** and **except** blocks. Then use a **finally** block to print 'All Done.'

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('There is a zero division error here')
finally: 
    print('All done')


###Problem 3 Write a function that asks for an integer and prints the square of it. Use a while loop with a try,except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            squared = int(input('Please enter a number to be squared: '))
            print(squared ** 2)
        except:
            print('You must enter an integer')
            continue
        else:
            print('Integer entered')
            break

ask()