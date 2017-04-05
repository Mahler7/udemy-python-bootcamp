#Use for, split(), and if to create a Statement that will print out words that start with 's': st = 'Print only the words that start with s in this sentence'

st = 'Print only the words that start with s in this sentence'
split_string = st.split(" ")

for word in split_string:
    if "s" in word:
        print(word)

#Use range() to print all the even numbers from 0 to 10.

array = [0,1,2,3,4,5,6,7,8,9,10]
for number in array:
    if number % 2 == 0:
        print(number)

print(range(0,11,2))

#Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

divisible = [number for number in range(1, 51) if number % 3 == 0]
print(divisible)

#Go through the string below and if the length of a word is even print "even!" st = 'Print every word in this sentence that has an even number of letters'

st2 = 'Print every word in this sentence that has an even number of letters'
string_split2 = st2.split(" ")
for word in string_split2:
    if len(word) % 2 == 0:
        print(word)

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print('FIZZBUZZ')
    elif  number % 5 == 0:
        print('BUZZ')
    elif number % 3 == 0:
        print("FIZZ")
    else:
        print(number)

#Use List Comprehension to create a list of the first letters of every word in the string below: st = 'Create a list of the first letters of every word in this string'

st3 = 'Create a list of the first letters of every word in this string' 

# for word in split_string3:
#     print(word[0])

first_letters = [word[0] for word in st3.split()]
print(first_letters)

