# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello my dear friend") # this is a comment for this command

word = "'trible quotes'"
print('''This is a test of the format function \n and the {0:_^40}.
What's the result?'''.format(word))

string = r"use \n and \t in your string"
print(string)


i=1
print(i)
i=i+23
print(i)

print(2<<3)
print(16>>4)
print(not 3>2)


a = "hello23"
if a == "hello":
    print("hello!")
elif a == "bye":
    print("Good bye!")
else:
    print("I don't get you.")

print("This is it.")

check = True
if check:
    print("You are right.[{0}]".format(check))
else:
    print("It is wrong.")


a = 0
while a<=199:
    print("Running. The current value is {0}.".format(0^a))
    a += 1
else:
    print("This is the end of the loop.")
print("All Done")


print(list(range(1, 20, 3)))


for a in range(0, 30, 3):
#    print("Current value {0}%2 = {1}".format(a, a%2))
#    print("odd number: {0}".format(a%2 == 1))
    odd = (a%2 == 1)
    if odd:
        print("In loop odd number {0}".format(a))
    else:
        print("In loop even number {0}".format(a))


#defineing function
def testFun(a, b):
    print("this is a test of function. a = {0} and b = {1}".format(a, b))
#end of the function

testFun(1, 2)
testFun("hello", "good bye")


#Test the parameters
def testFunction(*values1, **nameList):
    '''This function is used to test the daynamic parameters '''
    for a in values1:
        print("the value is {0}".format(a))

    for first_part, second_part in nameList.items():
        print("The name list - {0} {1}".format(first_part, second_part))
#end of function

testFunction(1, 2, 3, 9, "speical", Ken=11, Wing=12, Steve=13, Stan=14)
print(testFunction.__doc__)


#Use sys and os
import os
import sys

def test():
    print("the system path is [", sys.path,  "]\n")
    print("The current working folder is [", os.getcwd(), "]")
#end of the function

test()


import test_module_2
test_module_2.saySth()


dir()



# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ')

for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])

olditem = shoplist[0]
print("length of the list =", len(shoplist))
del shoplist[0]
print("length of the list =", len(shoplist), " after deleting the firs item.")
print('I bought the', olditem)
print('My shopping list is now', shoplist)

# Tuple test scripts
testlist = (2, 2, 3, 4,)
print(testlist)
print("length of this tuple is ", len(testlist))
testlist[2]


# Dictionary test scripts
# 'ab' is short for 'a'ddress'b'ook

ab = {
      'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }
ab['Matsumoto']

def printDict(aDict):
    print("Printing the dictionary object. Size is {}".format(len(aDict)))
    for key_id, value in aDict.items():
        print("[{}] = {}".format(key_id, value))
    print("\n")
#end of the function

printDict(ab)
del ab['Larry']
ab['Ken'] = 'kenneth.smith@123.com'
ab['Steve'] = 'Steve.smith@123.com'
ab['Spammer'] = 'unknown'
printDict(ab)


# Sequence test scripts
name = 'swaroop'
print('test 1 = {}'.format(name[1:3:1]))
print('test 2 = {}'.format(name[::1]))
print('test 3 = {}'.format(name[::-1]))
print('test 4 = {}'.format(name[1::-1]))
print('test 5 = {}'.format(name[-11:])) #index out of range will stay at the beginning/end of hte sequence
print('test 6 = {}'.format(name[6:]))


alist = [1, 2, 3, 1, 2, 3, 4]
set1 = set(alist)
set1

set2 = set('abc')
alist = ('def', 'kkk')
set3 = set2 | set(alist)
set3

name = 'Kenneth'
name.find('ne')
delimiter = ', '
myList = ['hello', 'good bye', 'see you']
delimiter.join(myList)
