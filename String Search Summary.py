# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 05:43:04 2019
@author: lb

String Search Summary
"""

""" 
    Counting up the number of vowels contained in a string s. 
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
    For example, if s = 'azcbobobegghakl', your program should print:
    Number of vowels: 5
"""

# V1 - creates a new list to append the vowels
s = 'azcbobobegghakl'
# transforms the string in lower case
s = s.lower()
count = 0

for letter in s:
    if letter in ('aeiou'):
        count+=1

print('Number of vowels: ', str(count))


# V2
s = 'azcbobobegghakl'
def num_vowels(s):
    if not s:
        return 0 
    else:
        return (s[0] in 'aeiou') + num_vowels(s[1:])

print('Number of vowels:', num_vowels(s))


###############################################################################

""" 
   Write a program that prints the number of times the string 'bob' occurs in s
   For example, if s = 'azcbobobegghakl', then your program should print
   Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
# transforms the string in lower case
s = s.lower()
bob = "bob"
numBob = 0
i = 0

while i < len(s):
    char = s[i:(i+3)]
    if char == bob:
        numBob+=1
    i +=1

print('Number of times ' + bob + ' occurs is: ' + str(numBob))


# v2
def num_bobs(s):
    return 0 if not s else \
           (s[:3] == 'bob') + num_bobs(s[1:])

print('Number of times bob occurs is:', num_bobs(s))


# V3
times=0
for i in range(0,len(s)-2+1):
    if s[i:i+3]=="bob":
        times+=1
print("Number of times bob occurs is: "+ str(times))

###############################################################################

""" 
   Longest substring of s in which the letters occur in alphabetical order. 
   For example, if s = 'azcbobobegghakl', then your program should print:
   Longest substring in alphabetical order is: beggh
   In the case of ties, print the first substring. 
   For example, if s = 'abcbcd', then your program should print
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


# V2 - with tuples
s = 'abcdefghijklmnopqrstuvwxy'
def longest(s, cur='', lngst=''):
    if not s:
        return max(lngst, cur, key=len)
    else:
        if not cur or s[0] < cur[-1]:
            lngst = max(lngst, cur, key=len)
            cur = ''
        return longest(s[1:], cur+s[0], lngst)

print('Longest substring in alphabetical order is:', longest(s))

# V3
longest=[]
for i in range(0, len(s)):
    length = 1
    while ((i+length)<len(s)) and max(s[i:i+length])<=s[i+length]:
        length += 1
    longest.append(length)
max_length=max(longest)
start=longest.index(max(longest))
print("Longest substring in alphabetical order is: " + str(s[start:start+max_length]))

# V4

longest, current = "", ""
for i in range(len(s)):
    current += s[i] 
    if  (i == len(s) - 1) or (s[i] > s[i + 1]):
        if len(longest) < len(current):
            longest = current
        current = ""
print("Longest substring in alphabetical order is: ", longest)



###############################################################################

""" 
   Determine if a character is in a string, so long as the string is sorted
   in alphabetical order. 
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # aStr is not empty
    if len(aStr) != 0:
        var = len(aStr)
        # integer result - using "//"
        result = aStr[var//2]
        x = 'abcdefghijklmnopqrstuvxwyz'
        y=x.index(char)
        z=x.index(result)
        # aStr has 1 char
        if y == z:
            return True
        # aStr has 2+ char
        else:
            return bool(isIn(char, aStr[:(var//2)]) + isIn(char, aStr[((var//2)+1):len(aStr)])) 
    # if aStr is empty
    else:
        return False

# V2
        def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])