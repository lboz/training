# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:06:53 2019

@author: Lia Bozneanu
"""
#  pythontutor.com


#######################################################################
# Tuples, lists, mutability, cloning
#######################################################################

# Tuples - used to swap variable values

# immitable, cannot change element values
te = ()           # () - thes sign it is a tuple
("one",)          # takes an extra "," to say this is a tuple
t = (2, "one", 3)
t1 = (5, 6)
t+t1
t
t[1:2]            # gives "('one',)" 
        
# iterate

def getData(aTuple):[]
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return(min_nums, max_nums, unique_words)
(small, large, words) = getData(((1, 'mine'),
                                 (2, 'yours'),
                                 (3, 'ours'),
                                 (7, 'mine')))

small
large
words
words

#####################################
x = (1, 2, (3, 'John', 4), 'Hi')
x[-1]
x[2][2]
x[-1][-1]
x[-1][2]
x[0:1]
x[0:-1]
len(x)
2 in x
3 in x
x[0] = 8
x[2][-1]

######################################

T = (10,20,30,40,50)
for var in T:
   print (T.index(var),var)
   
   
for var in range(len(T)):
  print (var,T[var])  
  
  
for var in enumerate(T):
  print (var)
  

L = range(10)
L[::2]
[0, 2, 4, 6, 8]
  
########################################################################
# Write a procedure called oddTuples, which takes a tuple as input, and returns
# a new tuple as output, where every other element of the input tuple is copied,
# starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test',
# 'tuple'), then evaluating oddTuples on this input would return the tuple
# ('I', 'a', 'tuple'). 


# A FAIRE


def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]

print(oddTuples((8, 19, 0, 12, 4, 4, 17, 14, 12, 6)))

########################################################################

list1 = [["h1",["h2","h3"], "h4"],"h5"]
"h3" in list1
"h1" in list1
########################################################################
# Lists - mutable
########################################################################

L = [2,1,3]
L[1] = 5
L

total = 0
    for i in range(len(L)):
        total += L[i]
    print(total)
    
total = 0
    for i in L:
        total += i
    print(total)
    
###############
x = [1, 2, [3, 'John', 4], 'Hi'] 
x[0]    
x[-1]
x[2][2]
x[-1][-1]
x[-1][2]
x[0:1]
x[0:-1]
len(x)
2 in x
3 in x
x[0] = 8
x
x[2][-1]


########################################################################
# List Operations
########################################################################
#append
L = [2,1,3]
L
L.append(5)     
L
# concatenate
L1 = [4,5,6]
L2 = L+L1
L2

L1.extend([0,6])

L1
L2

# remove specific index
del(L1[3])
L1

L = [2, 1, 3, 5, 4, 5, 6, 0, 6]

# remove element at end of the list
L.pop()
L

# remove specific element
L.remove(5)
L

########################################################################
# Lists and strings
########################################################################

s = 'abc'
list(s)

s = "I < 3 cs"
list(s)

# split a list
s.split('<')

# join
L = ['a', 'b', 'c']
''.join(L)
'_'.join(L)

# sorting
L = ['x', 'b', 'c']
sorted(L)       # initial L doesn't change
L

L.sort()        # initial L changes
L

# reverse
L.reverse()
L

# insert
L.insert(0, 100)
L

# count 
L.count('a')




########################################################################
# ex:

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']  

listA.sort
listA.sort()
listA
listA.insert(0, 100)
listA.remove(3)
listA.append(7)
listA
listA + listB
listB.sort()
listB.pop() 
listB.remove('a')
listA.extend([4, 1, 6, 3, 4])
listA.count(4)
listA.index(1)
listA.pop(4)
listA.reverse()
listA

########################################################################
# Mutation, Aliasing, Cloning
########################################################################
# Aliasis
# we change the alias, the list will also change
L = [1,2,3]
M = L

# Print is not == 
# even though the same print, not the same structure (2 different lists)

# Cloning
L = [1,2,3]
M = L[:]
M

# Lists of lists.. of lists  - mutation
warm = ['yellow','orange']
hot = ['red']
brightcolors = [warm]
warm

brightcolors
brightcolors.append(hot)
print(brightcolors)

hot.append('pink')
print(hot)
print(brightcolors)


print(hot + warm)
print(hot)

# mutation and iteration
# remove duplicates - 
def removeDups(L1,L2):  
    L1_copy = L1[:]             # clone the table first!!!
    for e in L1_copy:
        if e in L2:
            L.remove(e)
            

########################################################################
# ex.:
aList = [0, 1, 2, 3, 4, 5]
bList = aList
bList
aList[2] = 'hello'
aList
aList == bList

aList is bList
aList
bList

cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
cList == dList          # true
cList is dList          # false
cList[2] = 20
cList
dList

########################################################################
# Functions as Objects, Dictionaries
########################################################################

# Functions - first class objects
def applyToEach(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])
        return L
L = [1,-2,3.4]
print(applyToEach(L, abs))
applyToEach(L, fact)
applyToEach(L, fib)

# List of functions
def applyFuns(L, x):
    for f in L:
        print(f(x))
        
# generalization of hops
       
map(abs,[1,-2,3,-4])
#################
for elt in map(abs, [1,-2,3,-4]):
    print(elt)
#################    
L1 = [1,28,36]
L2 = [2,57,91]
    for elt in map(min, L1, L2):
        print(elt)
        
#########################################################################
# ex.:
        
testList = [1, -4, 8, -9]
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def timesFive(a):
    return a * 5

applyToEach(testList, timesFive)        


######

def absL(a):
    return abs(a)
    
applyToEach(testList, absL) 


######

def plus1(a):
    return a +1
applyToEach(testList, plus1) 

print(testList)
#   [2, -3, 9, -8]


######

def sqL(a):
    return a**2
applyToEach(testList, sqL) 

print(testList)
#   [1, 16, 64, 81]


################################################

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

applyEachTo([inc, square, halve, abs], -3)
applyEachTo([inc, square, halve, abs], 3.0)
applyEachTo([inc, max, int], -3)

#########################################################################
# Dictionaries - key + value
#########################################################################
grades = {'Ana': 'B', 'Katy':'A'}
grades
grades['Ana']
grades['Sylvain'] = 'A'               # add an entry
'Ana' in grades
'John' in grades
del(grades['Ana'])                  # delete en entry
grades

grades.keys()
grades.values()

###############

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'

animals
animals['c']

animals['donkey']

len(animals)

animals['a'] = 'anteater'
animals['a']
animals

len(animals['a'])

'baboon' in animals
'donkey' in animals.values()

'b' in animals

animals.keys()

del animals['b']
len(animals)

animals.values()

###############
# creating a dictionary

def lyrics_to_freq(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

# most common words
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

# mutating the dictionary
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

#########
# ex. 1:
#########
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals
    
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for i in aDict:
        for j in aDict[i]:
            count +=1
        
    return count        

print(how_many(animals))         # returns 6


# V2

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result


# V3:
    
def how_many(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result



#########
# ex. 2:
######### 

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
#len(animals['dog'])

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    d1 = {}
    for i in aDict:
        count = 0
        for j in aDict[i]:
            count+=1
        d1[i] = [count]
    
    return max(d1, key = d1.get)           

print(biggest(animals))


# V2
    
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result

#########################################################################
# Fibonacci et Dictionaries - memoization
#########################################################################
''' refaire!!!'''
def fib_effic(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_effic(n-1, d) + fib_effic(n-2, d)
        d[n] = ans
        return ans
d = {1:1, 2:2}
#argToUse = 50
print(fib_effic(5,d))        
#########################################################################
# Global Variables
#########################################################################       
        
        
        
        
        
        
###############################################################################
a = {1:'Tom', 2:'Jack'}
a.keys()
a.values()
a.items()
a.pop()

# aliasing - shallow[???] and copy???
a = [1,2,3]
id(a)
b = a
b.append(6)
a        
b        
id(b)        
id(a) 

# shallow copy
c = a[:]       
c.append(7)        
c        
a        
id(c)        
        
        
a = [1,2,3]
b = a
c = a[:]
a == b
a is b
a == c
a is c        
        
# importing modules and indentations        
import math        

from math import ceil, pi
ceil(1.7)
pi

from math import ceil as c, pi as p
p
c(1.7)

from math import *

import mymath


for i in range(4):
    for j in range(4):
        for k in range(4):
            print(i, j, k)


# variables scope
# in order to use a global variable in a function - "global d" inside the function

            
            















        
        
        
        
        
        
        
        
        


