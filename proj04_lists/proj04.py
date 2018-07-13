# coding=utf-8
# Name:
# Date:
import string
"""
proj04

practice with lists

# """
# var  = []
var2 = ["a",  "b", "cat", 3]
#
# print var2[0]



# #slice of list
#
#print var2[0:2]
# includes 0, not location 2



# #shorthand
# #all but the first
# print var2[1:]
# # all but the last item
# print var[:-1]



# #replace
# var2[0] = "tree"
# print var2
#
# #loop
#
# for item in var2:
#     if item == "cat:":
#         item == "dog"
#     print item



# # to change
#
# counter = 0
# for item in var2:
#     if item == "cat":
#         var2[counter] = "dog"
#     counter = counter + 1
#     elif item == "tree":
#         var2[counter] = "flower"
#     counter = counter + 1

# counter is to keep track of the index


# #Part I
# #Take a list, say for example this one:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# #and write a program that prints out all the elements of the list that are less than 5.
#

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
for item in a:
     if item < 5:
         print item
#
# #
#
#
#
# #Part II
# # Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # and write a program that creates and prints a list that contains only the elements
# # that are common between the lists (without duplicates).
# # Make sure your program works on two lists of different sizes.
newList= []
for item in b:
    for object in c:
        if item == object and item not in newList:
            newList.append(item)
print newList







#
#
# #Part III
# # Take a list, say for example this one:

# # # and write a program that replaces all “a” with “*”.
# #

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
#
for item in range(len(d)):
    if d[item]== "a":
        d[item] = "*"
print d



#
#
#
#
#
#
#
# #Part IV
# #Ask the user for a string, and print out whether this string is a palindrome or not.
#
#

userString = list(raw_input("Enter a word: "))
counter = 0
for thing in userString:
    if thing == ' ':
        userString.pop(counter)
    counter+=1
print userString
rev = []
rev = userString[:]
rev.reverse()

if userString == rev:
    print "This is a palindrome."
else:
    print "This is not a palindrome."





















#
#
#
#
#
#
