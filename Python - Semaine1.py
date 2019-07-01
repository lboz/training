# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:35:35 2019

@author: Lia Bozneanu
"""

x = 10
if x > 7:
   print("Yep")
else:
   print("Nope")
   
"""
"""
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

#####################################

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

#####################################

temp = 120
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable") 
else:
   print("Cold")
   
#####################################
   
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons += 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))

"""
"""

cube = 257
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0 :
        guess=-guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))

###########################################################
# ex 
###########################################################    
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


"""
"""
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
"""
"""
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break

"""
"""
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))

"""
"""
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))


"""
"""
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))


# Problem 1

"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.\
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',\
your program should print: "Number of vowels: 5"
"""

s = 'hihhhheeeehooooooooooo'
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
 
print('Number of voewls: ' + str(numVowels))


# Problem 2

"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. \
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
bob = "bob"
numBob = 0
i=0

while i < len(s):
    char = s[i:(i+3)]
    if char == bob:
        numBob += 1
    i+=1
print('Number of times ' + bob + ' occurs is: ' + str(numBob))

########################################

s = 'azcbobobobobobboboboegghakl'
numBob = 0
i=0

while i < len(s):
    char = s[i:(i+3)]
    if char == "bob":
        numBob += 1
    i+=1
print('Number of times "bob" occurs is: ' + str(numBob))

#############################################

# Problem 3

"""
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which\
the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl',\
then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', \
then your program should print
Longest substring in alphabetical order is: abc
"""

s = 'abcdefghijklmnopqrstuvwxy'
char1 = []
char2 = []
i = 0
j = 1

for i in range(len(s)):
    for j in range(1, len(s)+1):
        if s[i:j] != s[0:0]:
            print(s[i:j])
            char = s[i:j]
            x=list(char)
            if list(char) == sorted(char):
                char1.append(char)
                char2.append(len(char))
        j+=1
    i+=1 
x=max(char2)
index = char2.index(x)
fin = char1[index]
print('Longest substring in alphabetical order is: ' + str(fin))

########################################################################


iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 



iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 



import string
string.ascii_lowercase



















