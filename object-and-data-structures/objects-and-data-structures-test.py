###NUMBERS
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
numbers1 = ((100 / 10) ** 2 - 50) * 2 + 0.25
print(numbers1)
#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

#What is the value of the expression 4 * (6 + 5)
numbers2 = 4 * (6 + 5)
print(numbers2)

#What is the value of the expression 4 * 6 + 5 
numbers3 = 4 * 6 + 5
print(numbers3)

#What is the value of the expression 4 + 6 * 5 
numbers4 = 4 + 6 * 5
print(numbers4)

#What is the type of the result of the expression 3 + 1.5 + 4?
print("Floating Number")

#What would you use to find a number’s square root, as well as its square?
print('number**0.5 = square_root, number**2 = square')

###STRINGS
#Given the string 'hello' give an index command that returns 'e'.
string1 = 'hello'[1]
print(string1)

#Reverse the string 'hello' using indexing:
string2 = 'hello'[::-1]
print(string2)

#Given the string hello, give two methods of producing the letter 'o' using indexing.
string3 = 'hello'[-1]
string4 = 'hello'[4:]
print(string3)
print(string4)

###LISTS
#Build this list [0,0,0] two separate ways.
list1 = [0,0,0]
list2 = []
list2.append(0)
list2.append(0)
list2.append(0)
print(list1)
print(list2)

#Reassign 'hello' in this nested list to say 'goodbye' item in this list: l = [1,2,[3,4,'hello']]
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

#Sort the list l2 = [3,4,5,5,6]
list4 = [3,4,5,5,6]
list4.sort()
print(list4)

###DICTIONARIES
#Using keys and indexing, grab the 'hello' from the following dictionaries:

# d = {'simple_key':'hello'}
dictionary1 = {'simple_key':'hello'}
value_return1 = dictionary1['simple_key']
print(value_return1)

# d = {'k1':{'k2':'hello'}}
dictionary2 = {'k1':{'k2':'hello'}}
value_return2 = dictionary2['k1']['k2']
print(value_return2)

# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
dictionary3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
value_return3 = dictionary3['k1'][0]['nest_key'][1]
print(value_return3)

# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
dictionary4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
value_return4 = dictionary4['k1'][2]['k2'][1]['tough'][2]
print(value_return4)

###TUPLES
#What is the major difference between tuples and lists?
print("Tuples are immutable, arrays are mutable")

#How do you create a tuple?
tuple1 = (1,2,3)
print(tuple1)

###SETS
#What is unique about a set?
print('Sets can only have unique values')

#Use a set to find the unique values of the list l3 = [1,2,2,33,4,4,11,22,3,3,2]
l3 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(l3))

###BOOLEANS
#What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

#2 > 3
print(2 > 3)

#3 <= 2
print(3 <= 2)

#3 == 2.0
print(3 == 2.0)

#3.0 == 3
print(3.0 == 3)

#4**0.5 != 2
print(4**0.5 != 2)

#What is the boolean output of l_one = [1,2,[3,4]] l_two = [1,2,{'k1':4}] True or False? l_one[2][0] >= l_two[2]['k1']
test_one = [1,2,[3,4]]
test_two = [1,2,{'k1':4}]
print(test_one[2][0] >= test_two[2]['k1'])



