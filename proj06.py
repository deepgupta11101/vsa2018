# Name:
# Date:

# proj05: functions and lists

# Part I

def divisors(num):
    """
    Takes a number and returns all divisors of the number, ordered least to greatest
    :param num: int
    :return: list (int)
    """
    ret = []
    d = 2

    ret.append(1)
    if num>2:
        while d<num:
            if num % d ==0:
                ret.append(d)
            d+=1
    if num!=1:
        ret.append(num)

    # Fill in the function and change the return statment.
    return ret

def prime(num):
    """
    Takes a number and returns True if the number is prime, otherwise False
    :param num: int
    :return: bool
    """
    lst = divisors(num)
    if num<2:
        return False
    elif num==2:
        return True
    else:
        if len(lst)==2:
            return True
    return False

    # Fill in the function and change the return statment.
    return False


# Part II:
# REVIEW: Conditionals, for loops, lists, and functions
#
# INSTRUCTIONS:
#
# 1.  Make the string "sentence_string" into a list called "sentence_list" sentence_list
# should be a list of each letter in the string: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'm',
# 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'M', 'o', 'n', 't', 'y', ' ', 'P',
# 'y', 't', 'h', 'o', 'n', '.']
#
# Hint: Use a for loop and with an append function: list.append(letter)
#
sentence_string = "Hello, my name is Monty Python."
sentence_list = []
for ltr in sentence_string:
    sentence_list.append(ltr)
print sentence_list




# 2. Print every item of sentence_list on a separate line using a for loop, like this:
# H
# e
# l
# l
# o
# ,
#
# m
# y
#  .... keeps going on from here.
for item in sentence_list:
    print item



# 3: Write a for loop that goes through each letter in the list vowels. If the current
# letter is 'b', print out the index of the current letter (should print out the
# number 1).
#
vowels = ['a', 'b', 'i', 'o', 'u', 'y']
counter = 0
for ltr in vowels:
    if ltr=='b':
        print counter
        vowels[counter]= 'e'

    counter+=1



# 4: use the index found to change the list vowels so that the b is replaced with an e.



# 5: Loop through each letter in the sentence_string. For each letter, check to see if the
#  number is in the vowels list. If the letter is in the vowels list, add one to a
# counter. Print out the counter at the end of the loop. This counter should show how
# many vowels are in sentence_string.
counter = 0
for ltr in sentence_string:
    if ltr in vowels:
        counter+=1
print counter


# 6: Make a new function called "vowelFinder" that will return a list of  the vowels
# found in a list (no duplicates).The function's parameters should be "list" and "vowels."


#  Example:
# vowelList = vowelFinder(sentence_list, vowels)
# print vowelList

# ['a', 'e', 'i', 'o', 'y']

def vowelFinder(lst, vowels):
    ret = []
    counter = 0
    for item in lst:
        if item in vowels:
            ret.append(lst[counter])
            vowels.remove(item)
        counter+=1
    ret=sorted(ret)
    print ret
    return ret