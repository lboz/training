# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:06:53 2019

@author: User
"""
#  pythontutor.com


ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans+1
if ans**2 == x:
    print("Square root of ", x, "is ", ans)
else:
    print(x, " is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean ", -x, " ?")
        
 # slice strings

s = "abcdefgh"
s[::-1] # 'hgfedcba'
s[3:6]  # def   
s[-1]   # h


#############################################
an_letters = "qwertyuiop"
word = input("Enter a word: ")
times = int(input("times 1 to 10: "))
i=0
while i < len(word):
    char = word[i:(i+3)]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word,"!!!")



s = "saffgaosbdfbu"
for index in range(len(s)):
    if s[index] == "i" or s[index] == 'u':
        print("There is an i or u")


s = "saffgaosbdfbu"
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")

#########################################################
        
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


######################################################
    

cube = 29
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guess = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guess += 1
print("num_guess = :", num_guess)
if(abs(guess**3 - cube) >= epsilon):
    print("failed on cube root of ", cube)
else:
    print(guess, " is close to the cube root of ", cube)


#################################################################
    
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))


################################################################
    
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

#################################################################
    
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

############################################
    
# Bisection Search

x = 25
epsilon = 0.01
num_guess = 0
low = 0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print("low = " + str(low) + "; high = " + str(high) + "; ans = " + str(ans))
    num_guess +=1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print("num_guesses = " + str(num_guess))
printgg(str(ans) + " is close to square root of " + str(x))


#####################################################

# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of 
# an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - 
# is its guess too high or too low? Using bisection search,
# the computer will guess the user's secret number!


print("Please think of a number between 0 and 100!")
low = 0
high = 100

ans = ((high+low)//2)

rep = input("Is your secret number " + str(ans) + "?" +  
     "\nEnter 'h' to indicate the guess is too high. " +
     "Enter 'l' to indicate the guess is too low. "  +
     "Enter 'c' to indicate I guessed correctly: ")


while rep:
    if rep == "c":
        print('Game over. Your secret number was: ' + str(ans))
        break
    elif rep not in ("c", "l", "h"):
        rep = input("Sorry, I did not understand your input. \n" + 
                    "Is your secret number " + str(ans) + "?" +  
                      "\nEnter 'h' to indicate the guess is too high. " +
                        "Enter 'l' to indicate the guess is too low. "  +
                        "Enter 'c' to indicate I guessed correctly: ")
    else:
        while rep == "l":
            low = ans
            ans = (low + high)//2
            rep = input("Is your secret number " + str(ans) + "?" +  
                        "\nEnter 'h' to indicate the guess is too high. " +
                        "Enter 'l' to indicate the guess is too low. "  +
                        "Enter 'c' to indicate I guessed correctly: ")
        
        while rep == "h":
            high = ans
            ans = (low + high)//2
            rep = input("Is your secret number " + str(ans) + "?" +  
                            "\nEnter 'h' to indicate the guess is too high. " +
                            "Enter 'l' to indicate the guess is too low. "  +
                            "Enter 'c' to indicate I guessed correctly: ")

        


#####################################
#   float
#####################################
num = 11
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ""
if num == 0:
    result = "0"
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = "-" + result
    
#####################################
# fractions
#####################################

x = float(input("enter a decimal btw 0 and 1: "))
p=0
while((2**p)*x)%1 != 0:
    print("reminder = " + str((2**p)*x - int((2**p)*x)))
    p += 1
num = int(x*(2**p))

result = ''
if num == 0:
    result = "0"
while num > 0:
    result = str(num%2) + result
    num = num/2
result = result[0:-p] + "." + result[-p:]
print("the binary representation of the decimal " + str(x))


############################################
#   Newton - Raphson
############################################
epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y)>= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2)-y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))

###############################################
# Functions - name, param, docstring, body
###############################################
# Decomposition and abstraction

def is_even(i):
    """ 
    text - docstring
    """
    print("hi")
    return i%2 == 0
is_even(3)

#################################################
def square(x):
    '''
    x: int or float
    '''
    return x**2
x=4
square(x)
###################################################
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*(x**2) + (b*x) + c

###################################################
 # if no return -> value NONE

# return VS print   

def func_a():
    print('inside func_a')
def func_b(y):
    print('inside f_b')
    return y
def func_c(z):
    print('inside f_z')
    return z()
print(func_a())
print(5+func_b(2))
print(func_c(func_a))

##########################################
def a(x):
   '''
   x: int or float.
   '''
   return x + 1


def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
  
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y


def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z


def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2  


###############################################
def a(x, y, z):
     if x:
         return y
     else:
         return z



def b(q, r):
    return a(q>r, q, r)


#################################################
a = 10
def f(x):
    return x + a
a = 3
f(1)


x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)

#################################################
# keyword Arguments and default values // specifications
#################################################

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3)


def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3, 0)


def foo(x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)


def foo(x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)
 
####################################################
s = 'abc'
s.capitalize
# <built-in method capitalize of str object at 0x104c35878>
s.capitalize()
# 'Abc'

##########################################################

str1 = 'exterminate!' 
str2 = 'number one - the larch'

str1.upper
str1.upper()
str1
str1.isupper()
str1.islower()
str1.index('e')
str1.count('e')
str1 = str1.replace('e', '*')
str1
 
str2 = str2.capitalize()
str2 
str2.swapcase()
str2.index('n')
str2.find('N')
str2.index('!')
str2.find('!')
str2.replace('one', 'seven')

######################################################
#  Write a Python function, fourthPower, that takes in one number and returns 
# that value raised to the fourth power. You should use the square procedure 
# that you defined in an earlier exercise (you don't need to redefine square 
# in this box; when you call square, the grader will use our definition). 

def square(x):
    '''
    x: int or float
    '''
    return x**2

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(x)*square(x)
x=3
fourthPower(x)

############################################################
#  Write a Python function, odd, that takes in one number and returns True 
# when the number is odd and False otherwise. You should use the % (mod) 
# operator, not if. This function takes in one number and returns a boolean. 

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x%2 != 0
x=3
odd(x)

#########################################################
# Recursion
#########################################################

def mult(a,b):
    if b==1:
        return a
    else:
        return a+mult(a,b-1)
############################################
# recursion
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

# iteration
def fact(n):
    prod = 1
    for i in range(1,n+1):
        prod *=i
    return prod
print(fact(4))
##############################################
    
# Write an iterative function iterPower(base, exp) that calculates the exponential
# baseexp by simply using successive multiplication. For example, iterPower(base, exp) 
# should compute baseexp by multiplying base times itself exp times. 
# Write such a function below. This function should take in two values - base 
# can be a float or an integer; exp will be an integer ≥ 0. It should return 
# one numerical value. Your code must be iterative - use of the ** operator is not allowed. 

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    prod = 1
    for i in range(1, exp+1):
        prod *=base
        i+=1
    return prod
print(iterPower(3,3))

################################################

# Write a function recurPower(base, exp) which computes baseexp by recursively
# calling itself to solve a smaller version of the same problem, and then 
# multiplying the result by base to solve the initial problem. This function 
# should take in two values - base can be a float or an integer; exp will be 
# an integer ≥0. It should return one numerical value. Your code must be recursive
# - use of the ** operator or looping constructs is not allowed. 

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if base == 1:
        return 1
    elif exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base*recurPower(base, exp-1)
print(recurPower(-2,3))

############################################################
# Mathematical Induction - Towers of Hanoi
############################################################

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)
print(towers(4, "P1", "P2", "P3"))        

#################################################################
# he greatest common divisor of two positive integers is the largest integer 
# that divides each of them without remainder. For example, 
# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1
# Write an iterative function, gcdIter(a, b), that implements this idea. 
# One easy way to do this is to begin with a test value equal to the smaller 
# of the two input arguments, and iteratively reduce this test value by 1 
# until you either reach a case where the test divides both a and b without 
# remainder, or you reach 1. 

def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
 while a != b: 
        if a > b:
           a = a - b
        else:
           b = b - a
    return a   
print(gcdIter(17, 12))       


###################################################################
# The greatest common divisor of two positive integers is the largest integer
# that divides each of them without remainder. For example,
# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1
# A clever mathematical trick (due to Euclid) makes it easy to find greatest
# common divisors. Suppose that a and b are two positive integers:
# If b = 0, then the answer is a
# Otherwise, gcd(a, b) is the same as gcd(b, a % b)
# See this website for an example of Euclid's algorithm being used to find the gcd.
# Write a function gcdRecur(a, b) that implements this idea recursively. 
# This function takes in two positive integers and returns one integer.

def gcdRecur(a, b):
    ''' a, b: positive integers
        returns: a positive integer, the greatest common divisor of a & b.'''
    if b == 0:
        return a
    else: 
        return gcdRecur(b,a%b)
print(gcdRecur(6, 0)) 

###########################################################################
# Fibonacci
###########################################################################

def fib(x):
    """ assumes x an int >= 0
        returns Fibonacci of x """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
print(fib(4))

###########################################################################
# Palindrome
###########################################################################

def isPalindrome(s):
    def toChar(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwyz':
                ans = ans + c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChar(s))
print(isPalindrome("abcba"))

###########################################################################
# Divide and Conquer
###########################################################################

# We can use the idea of bisection search to determine if a character is in
# a string, so long as the string is sorted in alphabetical order.
# First, test the middle character of a string against the character you're 
# looking for (the "test character"). If they are the same, we are done - we've 
# found the character we're looking for! If they're not the same, check if 
# the test character is "smaller" than the middle character. If so, we need 
# only consider the lower half of the string; otherwise, we only consider 
# the upper half of the string. (Note that you can compare characters using
# Python's < function.) Implement the function isIn(char, aStr) which implements
# the above idea recursively to test if char is in aStr. char will be a single
# character and aStr will be a string that is in alphabetical order. 
# The function should return a boolean value. As you design the function, 
# think very carefully about what the base cases should be.

''' version 1 '''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    char = char.lower()
    aStr = aStr.lower()
    if char in aStr:
        return True
    else:
        return False
print(isIn("x","acxd"))      

########################################################################

''' version 2 - recursive call'''
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) != 0:
        var = len(aStr)
        result = aStr[var//2]
        x = 'abcdefghijklmnopqrstuvxwyz'
        y=x.index(char)
        z=x.index(result)
        if y == z:
            return True
        else:
            return bool(isIn(char, aStr[:(var//2)]) + isIn(char, aStr[((var//2)+1):len(aStr)])) 
    else:
        return False    
print(isIn("x", "axyz"))

##########################################################################
# Modules - - import file
##########################################################################
import circle  # a module / file
###
from circle import *


##########################################################################
# file handle
##########################################################################
nameHandle = open('file','w')       # 'w' - open for writing
for i in range(2):
    name = input('Enter name: '
    nameHandle.write(name + '\')
nameHandle.close()
           
      
nameHandle = open('file','w')       # 'r' - read the file 
for line in nameHandle:
    print(line)
nameHandle.close()

##########################################################################
##########################################################################
# A regular polygon has n number of sides. Each side has length s.
# The area of a regular polygon is: (0.25∗n∗s)/(2tan(π/n))
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular 
# polygon. The function returns the sum, rounded to 4 decimal places.

import math
def polysum(n, s):
    pArea = ((0.25 * n * s * s)/(math.tan(math.pi/n)))
    pPer = n*s
    tot = pArea + (pPer**2)
    return round(tot,4)
print(polysum(2,2))

math.pi


############################################################################
# Write a program to calculate the credit card balance after one year if a 
# person only pays the minimum monthly payment required by the credit card 
# company each month.
# The following variables contain values as described below:
#   balance - the outstanding balance on the credit card
#   annualInterestRate - annual interest rate as a decimal
#   monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly payment and remaining 
# balance. At the end of 12 months, print out the remaining balance. 
# Be sure to print out no more than two decimal digits of accuracy - so print
# Remaining balance: 813.41 instead of Remaining balance: 813.4141998135 
# So your program only prints out one thing: the remaining balance at 
# the end of the year in the format:
# Remaining balance: 4784.0
# A summary of the required math is found below:
#   Monthly interest rate= (Annual interest rate) / 12.0
#   Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#   Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#   Updated balance each month = (Monthly unpaid balance) +
#                                (Monthly interest rate x Monthly unpaid balance)
# We provide sample test cases below. We suggest you develop your code on your 
# own machine, and make sure your code passes the sample test cases, before you
# paste it into the box below. 

"""
          balance = 42
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
          # Result Your Code Should Generate Below:
	      Remaining balance: 31.38
          
          To make sure you are doing calculation correctly, this is the 
          # remaining balance you should be getting at each month for this example
            Month 1 Remaining balance: 40.99
            Month 2 Remaining balance: 40.01
            Month 3 Remaining balance: 39.05
            Month 4 Remaining balance: 38.11
            Month 5 Remaining balance: 37.2
            Month 6 Remaining balance: 36.3
            Month 7 Remaining balance: 35.43
            Month 8 Remaining balance: 34.58
            Month 9 Remaining balance: 33.75
            Month 10 Remaining balance: 32.94
            Month 11 Remaining balance: 32.15
            Month 12 Remaining balance: 31.38
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
i=0
monthlyInterestRate = annualInterestRate/12.0

while i < 12:
    paid = round((balance * monthlyPaymentRate),2)
    unpaidBalance = round((balance - paid),2)
    restToPay = round((unpaidBalance + (monthlyInterestRate * unpaidBalance)),2)
    balance = restToPay
    i += 1
print(" Remaining balance: " + str(round(restToPay,2)))


# V2

intst = annualInterestRate / 12
bal = balance
pay = monthlyPaymentRate

for i in range(12):
    bal *= (1 - pay) * (1 + intst)

print("Remaining balance: {:0.2f}".format(bal))


#######################################################################
# Now write a program that calculates the minimum fixed monthly payment needed
# in order pay off a credit card balance within 12 months. By a fixed monthly
# payment, we mean a single number which does not change each month, 
# but instead is a constant amount that will be paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
#    balance - the outstanding balance on the credit card
#    annualInterestRate - annual interest rate as a decimal
# The program should print out one line: the lowest monthly payment that
# will pay off all debt in under 1 year, for example:
#   Lowest Payment: 180 
# Assume that the interest is compounded monthly according to the balance 
# at the end of the month (after the payment for that month is made). 
# The monthly payment must be a multiple of $10 and is the same for all months.
# Notice that it is possible for the balance to become negative using
# this payment scheme, which is okay. A summary of the required math is 
# found below:
#  Monthly interest rate = (Annual interest rate) / 12.0
#  Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#  Updated balance each month = (Monthly unpaid balance) +
#                               (Monthly interest rate x Monthly unpaid balance)


balance = 3926
annualInterestRate = 0.2
paid = (balance/12)-((balance/12)%10)
i=0
monthlyInterestRate = annualInterestRate/12.0
tempBal = balance
restToPay = balance

while restToPay >= 0:
    while i < 12:
        unpaidBalance = round((tempBal - paid),2)
        restToPay = round((unpaidBalance + (monthlyInterestRate * unpaidBalance)),2)
        tempBal = restToPay
        i += 1
    paid += 10
    tempBal = balance
    i = 0
paid -= 10
print("Lowest Payment: " + str(int(paid)))


# V2
int = annualInterestRate / 12
bal = 1
payment = 0

while bal > 0:
    bal = balance
    payment += 10
    for i in range(12):
        bal = ((bal - payment) * (1 + int))

print("Lowest Payment: {:0.2f}".format(payment))       


# V3
monthlyIntRate = annualInterestRate/12
pay = 0
bal = balance
while bal>0:
    bal = balance
    pay += 10
    for i in range(12):
        mub = bal - pay
        bal = mub + mub*monthlyIntRate
print("Lowest Payment: %i" % pay) 

#############################################################################
# Using Bisection Search to Make the Program Faster 

# The following variables contain values as described below:
#     balance - the outstanding balance on the credit card
#     annualInterestRate - annual interest rate as a decimal
# To recap the problem: we are searching for the smallest monthly payment
# such that we can pay off the entire balance within a year. What is a
# reasonable lower bound for this payment value? $0 is the obvious anwer,
# but you can do better than that. If there was no interest, the debt can be
# paid off by monthly payments of one-twelfth of the original balance,
# so we must pay at least this much every month. One-twelfth of the original
# balance is a good lower bound.
# What is a good upper bound? Imagine that instead of paying monthly,
# we paid off the entire balance at the end of the year. What we ultimately
# pay must be greater than what we would've paid in monthly installments,
# because the interest was compounded on the balance we didn't pay off each
# month. So a good upper bound for the monthly payment would be one-twelfth
# of the balance, after having its interest compounded monthly for an entire year.
# In short:
#    Monthly interest rate = (Annual interest rate) / 12.0
#    Monthly payment lower bound = Balance / 12
#    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
# Write a program that uses these bounds and bisection search (for more info
# check out the Wikipedia page on bisection search) to find the smallest
# monthly payment to the cent (no more multiples of $10) such that we can pay
# off the debt within a year. Try it out with large inputs, and notice how
# fast it is (try the same large inputs in your solution to Problem 2 to
# compare!). Produce the same return value as you did in Problem 2.
# Note that if you do not use bisection search, your code will not run -
# your code only has 30 seconds to run on our servers.

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
lowPaid = (balance/12)
highPaid = (balance * (1 + monthlyInterestRate)**12)/12
paid = (lowPaid + highPaid)/2
i=0
tempBal = balance
restToPay = balance

while restToPay != 0:
    while i < 12:
        paid = (lowPaid + highPaid)/2
        unpaidBalance = (tempBal - paid)
        restToPay = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        tempBal = restToPay
        i += 1  
        
    if restToPay > 0.09: 
        i = 0
        lowPaid = paid
        highPaid = paid + restToPay/10
        tempBal = balance
    elif restToPay < (-0.09):
        i = 0
        highPaid = paid
        lowPaid = paid + (restToPay)/10
        tempBal = balance
    else: break
print("Lowest Payment: " + str(round(paid,2)))


# V2
upper = balance
lower = 0
while True:
    bal = balance
    payment = (lower + upper) / 2
    for i in range(12):
        bal = ((bal - payment) * (1 + annualInterestRate/12))
    if bal < -0.001:
        upper = payment
    elif bal > 0.001:
        lower = payment
    else:
        break
print("Lowest: {:0.2f}".format(payment))


# V3
balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
monthlyLower = balance/12
monthlyUpper = (balance * (1+monthlyInterestRate)**12)/12.0

while True:     
     updatedBalance = balance
     for i in range(12):
        payment = (monthlyUpper + monthlyLower)/2.0 
        monthlyUnpaidBalance = updatedBalance - payment
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
     if updatedBalance < -0.01:
        monthlyUpper = payment
     elif updatedBalance > 0.01:
        monthlyLower = payment
     else:
         break

print("Lowest {:0.2f}".format(payment))


# V4
mir = annualInterestRate/12.0   
lb = balance/12                 
ub = balance*((1+mir)**12)/12.0  
bal = balance
while bal!=0:
    bal = balance
    avg = (lb + ub)/2
    for i in range(12):
        mub = bal - avg
        bal = round((mub + mub*mir),2)
    if bal>0:
        lb = avg
    elif bal<0:
        ub = avg
print("Lowest payment: %.2f" % avg)
##################################################################












