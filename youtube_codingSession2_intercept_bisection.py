# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:41:10 2019
youtube video: 
https://www.youtube.com/watch?v=BbeUNS4wSyA
49min
@author: User
"""

# Given a linear function with a positive slope that intercepts the x axis 
# between 0 and 100, find the point where it intercepts without solving for x.
# Use bisection search Find 'a' such that f(a) = 0 to some certainty 'epsilon'

def f(x):
    return -5+2.77*x

def g(x):
    return -5+0.08*x

# function that computes x intercept using bisection
def intercept_bisection(func, epsilon):
    ''' func is a function
        epsilon is some small float
    '''
    low = 0
    high = 100
    mid = (low + high)/2
    # remember to take abs value of f(x) 
    while (abs(func(mid)) > epsilon):
#       print("low = ", low, "high = " ,high)
        # case where guess was too low
        if func(mid) > 0:
            high = mid
        # case where guess was too high
        elif func(mid) < 0:
            low = mid
        # reclaculate guess with new high and low values
        mid = (low + high)/2
    return mid

print(intercept_bisection(f,0.1))          
    
  