import functools
###Problem 1
#Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list. The function will have an input of a string, and output a list of integers.

phrase = 'How long are the words in this phrase'
word_lengths = list(map(lambda phrase: len(phrase), phrase.split()))
print(word_lengths)

# ###Problem 2
# ### Use reduce to take a list of digits and return the number that they correspond to. Do not convert the integers to strings!

# def digits_to_num(digits):
#     pass

digits_list = [3,4,3,2,1]
digits_to_num = lambda x,y: x * 10 + y
print(functools.reduce(digits_to_num, digits_list))

# ###Problem 3
# ### Use filter to return the words from a list of words which start with a target letter.

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_h = list(filter(lambda word: 'h' in word, l))
print(filter_h)

# ###Problem 4
# # Use zip and list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them. Look at the example output below:

def concatenate(L1, L2, connector):   
    return [word1 + connector + word2 for (word1, word2) in zip(L1, L2)]
print(concatenate(['A','B'],['a','b'],'-'))

# ###Problem 5
# # Use enumerate and other skills to return a dictionary which has the values of the list as keys and the index as the value. You may assume that a value will only appear once in the given list.
def d_list(L): 
    return {key:value for value,key in enumerate(L)}

print(d_list(['a','b','c']))



# ###Problem 6
# # Use enumerate and other skills from above to return the count of the number of items in the list whose value equals its index.

def count_match_index(L): 
    return len([num for count, num in enumerate(L) if num == count])

print(count_match_index([0,2,2,1,5,5,6,10]))
