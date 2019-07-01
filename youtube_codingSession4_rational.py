# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 08:56:29 2019
https://www.youtube.com/watch?v=QWW503WoPS8

@author: lb

Rationals
"""

# Implement the Rational class to represent a rational number with a numerator
# and a denominator. The methods of this class will be to implement + - * / 
# and print (via __str__) and also simplify() on a Rational number. 
# To demonstrate inheritance, implement 
#   subclasses StringRational, WholeNumber, and MixedNumber.
# Some examples: 8/7 represented by Rational(8,7)
#                8/7 represented by StringRational('8/7')
#                3/1 represented by WholeNumber(3)
#                8/7 represented by MixedNumber(1,1,7)
# and this subclass should overload the __str__ method to print 1+1/7
from fractions import gcd

class Rational(object):
    def __init__(self, num, denom):
        # defensing programming - prevent bugging inputs
        assert denom !=0, "Denominator must not be 0"
        self.n = num
        self.d = denom
        
    # called when we use the word "print" on the Rational class
    def __str__(self):
        return (str(self.n) + '/' + str(self.d))
    
    def __add__(self, other_rational):
        ''' implements the + operator between 2 Ratioanals'''
        new_n = self.n * other_rational.d + self.d * other_rational.n
        new_d = self.d * other_rational.d
        return Rational(new_n, new_d)
    
    def __sub__(self, other_rational):
        ''' implements the - operator between 2 Ratioanals'''
        new_n = self.n * other_rational.d - self.d * other_rational.n
        new_d = self.d * other_rational.d
        return Rational(new_n, new_d)
    
    def __mul__(self, other_rational):
        ''' implements the * operator between 2 Ratioanals'''
        new_n = self.n * other_rational.n
        new_d = self.d * other_rational.d
        return Rational(new_n, new_d)
    
    def __div__(self, other_rational):
        ''' implements the / operator between 2 Ratioanals'''
        new_n = self.n * other_rational.d
        new_d = self.d * other_rational.d
        return Rational(new_n, new_d)
    
    def simplify(self):
        divisor = gcd(self.n, self.d)
        new_n = self.n/divisor
        new_d = self.d/divisor
        return Rational(new_n, new_d)
 
    
class StringRational(Rational):
    def __init__(self,str_rational):
        # parse the string input to get nun and denom
        split_str = str_rational.split('/')
        num = int(split_str[0])
        denom = int(split_str[1])
        Rational.__init__(self, num, denom)
  
    
class WholeNumber(Rational):
    def __init__(self, number):
        Rational.__init__(self, number, 1)


class MixedNumber(Rational):
    def __init__(self, whole, num, denom):
        self.w = whole
        Rational.__init__(self, num, denom)
    def __str__(self):
        return str(self.w) + '+' + str(self.n) + '/' + str(self.d)
    def __add__(self, other_mixed):
        new_n = self.n * other_mixed.d + self.d * other_mixed.n
        new_d = self.d * other_mixed.d
        r = Rational(new_n, new_d)
        r_s = r.simplify()
        # extract whole part and reminder part from r_s
        whole = r_s.n // r_s.d
        # % = reminder operator
        frac = r_s.n%r_s.d
        total_whole = whole + self.w + other_mixed.w
        return MixedNumber(total_whole, frac, r_s.d)
        
        
# verifications
        
r1 = Rational(2,5)
r2 = Rational(4,5)
print(r1)
print(r2)
r3 = r1 + r2
print(r3)
r3_s = r3.simplify()
print(r3_s)
print('******')
s1 = StringRational('3/5')
s2 = StringRational('4/5')
print(s1)
print(s2)
s3 = s1 + s2
print(s3)
print('******')
w1 = WholeNumber(6) #  = 6/1
w2 = WholeNumber(4)
print(w1)
print(w2)
w3 = w1+w2
print(w3)
print('******')
m1 = MixedNumber(1,1,2)  # 1+5/7
m2 = MixedNumber(3,2,3) 
print(m1)
print(m2)
m3 = m1+m2
print(m3)




















