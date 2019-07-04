# -*- coding: utf-8 -*-
"""
Created on Wed July 07 14:06:53 2019

@author: Lia Bozneanu
"""
#  pythontutor.com

###############################################################################
# Testing and Debugging 
###############################################################################
"""
- ensure code runs
- have a set of expected results
- classes of tests:
    - unit testing  - validate each piece of program 
                    - testing each function separately
    - regression testing - add test for bugs as you find them
                         - catch reintroduced errors that were previously fixed
    - integration testing - test the overall program 

- testing approaches:
    - intuition about natural boundaries
    - black box testing - explore paths through specification
        * designed w/o looking at the code
        * can be reused if implementation changes
        * path through specification - boundaries, empty lists, singleton list, 
                                       large numbers, small numbers, etc      
    - glass box testing - explore path through code
        * use code directly to guide the design
        * called "path-complete" if every potential path through code is
          tested as least once
        * drawbacks: - go through loops arbitrarily many times
                     - missing paths
        * guidelines: - branches
                      - for loops
                      - while loops
                    
- Bugs: - isolate
        - eradicate
        - re-test
    * overt bugs - code crashes or runs forever
    * covert bugs - have a wrong return
    ** persistent bugs - 
    ** intermittent bugs - 
    - overt and persistent
    - overt and intermittent
 
Debugging
- tools - IDLE
        - Python Tutor
        - print statement - function, parameters, results; halfway in code..
        - be systematic
- error messages:
    - IndexError - beyond the limits of a list
    - TypeError - coonvert an inappropriate type
    - NameError - non-existing variable
    - TypeError - mixing data types w/o appropriate coercion
    - SyntaxError - parenthesis, quotations, etc.
- logic errors:
    - think before writing 
    - draw the pictures
    - explain the code a rubber ducky ;)
- steps:
    - study the program
    - scientific method - study the available data
                        - form hypothesis
                        - repeatable experiments
                        - pick simplest input to test with
                        - keep record of tests / modifications
- debugging as search - narrow down the code - binary search
    - temp = x   <>  temp = x[:]
- Pragmatic hints:
    - usual suspects
    - ask why the code is doing what it is
    - eliminate locations
    - explain to somebody else
    - do not believe the documentation
    - take a break and come back later   
"""

###############################################################################
# Exceptions 
###############################################################################
"""
- Exceptions:
    - IndexError - beyond the limits of a list
    - TypeError - coonvert an inappropriate type
    - NameError - non-existing variable
    - TypeError - mixing data types w/o appropriate coercion
    - ValueError - value is illegal
    - IOError - ex.: file not found
    
    * stop execution -> raise an exception
    * dealing with exceptions
    * except - else - finally

* exception usage - control input (ex.: except IOError:
                                        print('cannot open...'))
                  - control flow
"""
###############################################################################
# Assertions - defensive programming
###############################################################################
"""
- AssertionError - assert statement
- ensure the execution halts if an expected condition is not met
- check inputs to functions procedures, but can be used anywhere
- check outputs of a function to avoid propagating bad values
- make it easier to locate a source of a bug

**** where to use
- supplement to testing
- raise exceptions if bad data input
- check types of arg of values
- check that invariants on data structures are met
- check constraints on return values
- check for violations of constraints on procedure (ex.: no duplicates in a list)
"""

###############################################################################
#  
###############################################################################
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count
print(integerDivision(5, 3))

##########################################

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
rem(2, 5)
rem(5, 5)
rem(7, 5)

##########################################

def f(n):
   """
   n: integer, n >= 0.
   return f(0) = 1 // f(1) = 1 // f(3) = 6
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)
f(3)


###############################################################################
# Exceptions
###############################################################################

''' raise an exception '''

try:
    a = int(input("tell me a number: "))
    b = int(input("tell me another number:"))
    print(a/b)
    print("ok")
except:
    print("not ok")
print("outside")

#######

try:
    a = int(input("tell me a number: "))
    b = int(input("tell me another number:"))
    print(a/b)
    print("ok")
except ValueError:
    print("Could not convert to a number")
except ZeroDivisionError:    
    print("Can't divide by zero")
except:    
    print("Something went very wrong")


###############
# input control
###############
    
data = []

file_name = input("Provide a name of a file of data ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')             #remove trailing
            data.append(addIt)
finally:
    fh.close() # close file even if fail

gradesData = []
if data:
    for student in data:
        try:
            name = student[0:-1]                    # multiple names
            grades = int(student[-1])
            gradesData.append([name, [grades]]) 
        except ValueError:
            gradesData.append([student[:], []])     # no grades
   
    
###############
# control flow
###############    
# raise our own error values
            
def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NaN = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

#######
    
def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats 

#def avg(grades):
#    return sum(grades)/len(grades)

test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]], 
           [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
           [['captain', 'america'], [8.0,10.0,96.0]],
           [['deadpool'], []]]

#def avg(grades):
#    try:
#        return sum(grades)/len(grades)
#    except ZeroDivisionError:
#        print('no grades data')


def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0

get_stats(test_grades)

##########

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

fancy_divide([0, 2, 4], 1)
fancy_divide([0, 2, 4], 4)
fancy_divide([0, 2, 4], 0)

##########

def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
        
fancy_divide([0, 2, 4], 1)
fancy_divide([0, 2, 4], 4)
fancy_divide([0, 2, 4], 0)

##########

def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

fancy_divide([0, 2, 4], 1)
fancy_divide([0, 2, 4], 4)
fancy_divide([0, 2, 4], 0)

##########

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)

fancy_divide([0, 2, 4], 0)

##########

def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)

fancy_divide([0, 2, 4], 0)

##########

""" Your task is to change the definition of simple_divide so that the call
    does not raise an exception. When dividing by 0, fancy_divide should return
    a list with all 0 elements. Any other error cases should still raise
    exceptions. You should only handle the ZeroDivisionError. 
"""
def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]

def simple_divide(item, denom):
    try:
        itemi = item / denom
    except ZeroDivisionError:
        itemi = 0
    return itemi

print(fancy_divide([0, 2, 4],0))

###############################################################################
# Assertions
###############################################################################

def avg(grades):
    assert not len(grades) == 0, 'no grades data'      # if no grades data, print this message
    return sum(grades)/len(grades)                     # otherwise runs ok

##########
    
def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers 

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')
      
##########

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers        
      
normalize([0, 0, 0])      

