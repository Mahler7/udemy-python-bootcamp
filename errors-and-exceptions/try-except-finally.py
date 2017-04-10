try:
    2 + 's'
except TypeError:
    print('There was a type error')
finally:
    print("Finally was printed")

try:
    f = open('testfile', 'w')
    f.write('Test write this')
except:
    print('Error in writing to the file')
else:
    print('File write was a success')

try:
    f = open('testfile', 'r')
    f.write('Test write this')
except:
    print('Error in writing to the file')
finally:
    print('Always execute finally code blocks!')

def askint():
    try:
        val = int(input('Please enter an integer: '))
    except:
        print("You didn't enter an integer.")
        val = int(input('Please try again: '))
    finally:
        print('Finally block executed.')
    print(val)

askint()

def askint2():
    while True:
        try:
            val = int(input('Please enter an integer: '))
        except:
            print("You didn't enter an integer.")
            continue
        else:
            print('Correct that is an integer.')
            break
        finally:
            print('Finally block executed.')
        print(val)

askint2()
