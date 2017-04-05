import math
import string

#Write a function that computes the volume of a sphere given its radius. def vol(rad): pass

def vol(radius):
    return (4 / 3) * math.pi * (radius ** 3)
print(vol(5))

#Write a function that checks whether a number is in a given range (Inclusive of high and low) def ran_check(num,low,high): pass

def ran_check(num, low, high): 
    for i in (range(low, high)):   
        if i == num:
            return 'Number is in the range'
            break
    else:
        return 'Number is not in the range'

print(ran_check(4,1,11))
print(ran_check(25,5,15))


#If you only wanted to return a boolean: def ran_bool(num,low,high): pass

def ran_check(num, low, high): 
    for i in (range(low, high)):   
        if i == num:
            return True
            break
    else:
        return False

print(ran_check(4,1,11))
print(ran_check(25,5,15))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters. Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?' 33lc 4uc def up_low(s):pass

def up_low(s):
    upper_letters = 0
    lower_letters = 0
    for i in s.split():
        for j in i:
            if j.isupper():
                upper_letters = upper_letters + 1
            elif j.islower():
                lower_letters = lower_letters + 1
    print('The number of uppercase letters:', upper_letters)
    print('The number of lowercase letters:', lower_letters)

string = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(string)


#Write a Python function that takes a list and returns a new list with unique elements of the first list. Sample List : [1,1,1,1,2,2,3,3,3,3,4,5] def unique_list(l): pass

def unique_list(l):
    setter = set(l)
    lister = list(setter)
    return lister

array = [1,1,1,1,2,2,3,3,3,3,4,5]
print(unique_list(array))

#Write a Python function to multiply all the numbers in a list. Sample List : [1, 2, 3, -4] def multiply(numbers): pass

def multiply(numbers):
    total = 1
    for i in numbers:
        total = total * i

    return total

array2 = [1, 2, 3, -4]
print(multiply(array2))

#Write a Python function that checks whether a passed string is palindrome or not. def palindrome(s):pass

def palindrome(s):
    reverse_string = s[::-1]
    if s == reverse_string:
        print('This is a palindrome')
    else:
        print('This is not a palindrome')

palindrome('racecar')
palindrome('hello')

#Write a Python function to check whether a string is pangram or not. Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog" import string def ispangram(str1, alphabet=string.ascii_lowercase): pass
def ispangram(str1, alphabet):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())
    
    

print(ispangram("The quick brown fox jumps over the lazy dog", 'abcdefghijklmnopqrstuvwxyz'))
print(ispangram("Hey there", 'abcdefghijklmnopqrstuvwxyz'))

