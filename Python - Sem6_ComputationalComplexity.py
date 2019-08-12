# -*- coding: utf-8 -*-
"""
Created on Wed July 17 18:06:53 2019

@author: Lia Bozneanu
"""
#  pythontutor.com


###############################################################################
# Program Efficiency
###############################################################################
"""
- time and space efficiency
* How to evaluate efficiency
    - timer
    - count the operations
    - order of growth
    
- Timing a program
import time
def c_to_f(c):
    ...
    
- Counting operations
- efficiency in terms of input - integer, len(list)
    - best case // worst case // average case - will focus on worst case
- orders of growth - want to put an upper bound on growth
    - order of...
        - constant, linear, quadratic, logarithmic, nlogn, exponential    

- Big OH Notation or O() - the worst case

- Complexity Classes
    - O(1) 
    - O(log n) - bisection search, binary search of a list
    - O(n) - searching a list in sequence, add char to a str, recursive factorial
    - O(n log n) - merge sort
    - O(n**c) - nested loops, recursive function calls
    - O(c**n) - recursive functions where more than one recursive call for each side of the problem

- Search and Sorting Algorithms
    - linear search - brute force search
    - bisection search - sorted lists only

- BOGO Sort
  - monkey sort, slow sort, stupid sort.. 
  - unbounded

- Bubble Sort - starts with biggest number
    - O(n**2)

- Selection Sort - starts with smallest number
    - O(n**2)

- Merge Sort
    - divide-and-conquer
    - O(n log(n))
    
"""

def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total

#####################################
# Assume n has been previously bound to some value
i = 0
while i < 5:
   n *= 2
   i += 1

print(n)

''' O(1)'''

######################################

def iterPower(a, b):
   result = 1
   while b > 0:
      result *= a
      b -= 1
   return result

'''O(b)'''  
#####################################
def recurPower(a, b):
   print(a, b)
   if b == 0:
      return 1
   else:
      return a * recurPower(a, b-1)

'''O(b)'''

#####################################

def recurPowerNew(a, b):
   print(a, b)
   if b == 0:
      return 1
   elif b%2 == 0:
      return recurPowerNew(a*a, b/2)
   else:
      return a * recurPowerNew(a, b-1)

'''O(log(b))'''

#####################################

def lenRecur(s):
   if s == '':
      return 0
   else:
      return 1 + lenRecur(s[1:])

'''O(len(s))'''

#####################################

def isIn(a, s):
   '''
   a is a character, or, singleton string.
   s is a string, sorted in alphabetical order.
   '''
   if len(s) == 0:
      return False
   elif len(s) == 1:
      return a == s
   else:
      test = s[len(s)//2]
      if test == a:
         return True
      elif a < test:
         return isIn(a, s[:len(s)//2])
      else:
         return isIn(a, s[len(s)//2+1:])

'''O(log(len(s)))'''

######################################

def union(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = L1[:]
   for e2 in L2:
      flag = False
      for check in temp:
         if e2 == check:
            flag = True
            break
      if not flag:
         temp.append(e2)
   return temp

'''O(n**2)'''

######################################

def unionNew(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = []
   for e1 in L1:
      flag = False
      for e2 in L2:
         if e1 == e2:
            flag = True
            break
      if not flag:
         temp.append(e1)
   return temp + L2

'''O(n**2)'''

######################################
######################################

def foo(L):
    val = L[0]
    while (True):
        val = L[val]

a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

print(foo(a))   # infinite loop
print(foo(b))   # infinite loop
print(foo(c))   # list index out of range

######################################
# What is the smallest value that num can be such that the number 3 is printed?
# 1
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
num = 0
for i in range(0, num):
    val = L[L[val]]
    print(val)
print(val)

######################################
# What is the smallest value that num can be such that the number 3 is printed?
# impossible
L = [2, 0, 1, 5, 3, 4]
val = 0
num = 0
for i in range(0, num):
    val = L[L[val]]
    print(val)
print(val)

######################################
######################################

#  each function is tested with a list L whose elements 
# are sorted in increasing order. For simplicity, assume
# L is a list of integers
# both return the same answer
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

L = [0, 2, 4, 6, 8, 11]
search(L, 4)

######################################

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

L = [0, 2, 4, 6, 8, 11]
search(L, 4)

######################################
######################################

#  each function is tested with a list L whose elements 
# are sorted in increasing order. For simplicity, assume
# L is a list of integers

#  search and search3 return the same answers provided L
# is non-empty and e is in L. correct 

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

######################################

def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)

######################################
######################################

#  code for selection sort.
# For simplicity, assume L is a list of integers

# the two functions result in the same sorted lists
# newSort may use more - but never fewer - inserts than selSort
# both have the same complexity

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp

######################################
# the alternative
def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1

######################################
######################################
# 2 sorting functions

# same results
# same number of assignments
# same complexity
# not the same no of entries, but one cannot always say which function will
# examine the most entries

def mySort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

L = [2, 0, 1, 5, 3, 4]
print(mySort(L))
######################################

def newSort1(L):
    """ L, list with unique elements """
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            
L = [2, 0, 1, 5, 3, 4]
print(newSort1(L))

######################################
######################################


n=5000
200000*(n**2)
0.001*(n**5)

######################################

n = 10
0.0000001*n+1000000
0.0001*(n**2)
(20000*n)
0.0001*(n**2) + (20000*n) - 90000
n**200 - 2*n**30
5**n
n**5
def modten(n):
    return n%10
print(modten(n))

######################################

n = 10000
0.0000001*n+1000000
0.0001*(n**2)
(20000*n)
0.0001*(n**2) + (20000*n) - 90000
n**200 - 2*n**30
5**n
n**5
def modten(n):
    return n%10
print(modten(n))

######################################
######################################

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

L = [2, 0, 1]
print(search(L, 1))

#################################

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

L = [2, 0, 1]
print(newsearch(L, 1))

######################################
######################################

# ascending order
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
L = [2, 0, 1, 5, 3, 4]
print(swapSort(L))


# descending order
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):     ''' 1 line modification to the fct before'''
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

######################################
######################################
500,000 (this is O(1))
log log n
log n
n
n log n
n**2
n**3
3**n
n**n
2**(n**2)















