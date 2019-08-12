# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:06:53 2019

@author: Lia Bozneanu
"""
#  pythontutor.com


#######################################################################
# Data Visualization - PYLAB
#######################################################################
# the lists have to have the same len

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExpon = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExpon.append(1.5**i)

plt.plot(mySamples, myLinear)

# overlapping 
plt.plot(mySamples, myLinear)

plt.figure('lin')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.plot(mySamples, myQuadratic)
plt.figure('cub')
plt.plot(mySamples, myCubic)
plt.figure('exp')
plt.plot(mySamples, myExpon)

plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.title('Linear')
plt.plot(mySamples, myLinear)

# clear the window
plt.clf()

# comparing results
plt.figure('lin')
plt.clf()
plt.ylim(0,1000)                # same y axes
plt.title('Linear')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0,1000)
plt.title('Quadratic')
plt.plot(mySamples, myQuadratic)

# overlaying plots
plt.figure('lin quad')
plt.clf()
plt.title('Linear vs Quadratic')
plt.plot(mySamples, myLinear, label = 'linear')
plt.plot(mySamples, myQuadratic, label = "quadratic")
plt.legend(loc = 'upper left')  # decide the legend location

plt.figure('cube exp')
plt.clf()
plt.title('Cubic vs Exponential')       
plt.plot(mySamples, myCubic, label = 'Cubic')
plt.plot(mySamples, myExpon, label = 'Expo')
plt.legend()                    # Python decides the location

# controlling display parameters
plt.figure('lin quad')
plt.clf()
plt.title('Linear vs Quadratic')
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.plot(mySamples, myQuadratic, 'ro', label = "quadratic", linewidth = 1.0)
plt.legend(loc = 'upper left')  # decide the legend location

plt.figure('cube exp')
plt.clf()
plt.title('Cubic vs Exponential')       
plt.plot(mySamples, myCubic, 'g^', label = 'Cubic', linewidth = 3.0)
plt.plot(mySamples, myExpon, 'k--', label = 'Expo', linewidth = 4.0)
plt.legend()      

# subplots
plt.figure('lin quad')
plt.clf()
# inside of figure ... display 2 rows and 1 colomn + location 1
plt.subplot(211)
plt.title('Linear vs Quadratic')
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.subplot(212)
plt.plot(mySamples, myQuadratic, 'ro', label = "quadratic", linewidth = 1.0)
plt.legend(loc = 'upper left')  # decide the legend location

plt.figure('cube exp')
plt.clf()
plt.subplot(121)
plt.title('Cubic vs Exponential')       
plt.plot(mySamples, myCubic, 'g^', label = 'Cubic', linewidth = 3.0)
# change the scale
plt.yscale('log')
plt.subplot(122)
plt.plot(mySamples, myExpon, 'k--', label = 'Expo', linewidth = 4.0)
plt.legend()  

###############################################################################
# retire exercice
###############################################################################

def retire(monthly, rate, terms):
    savings = []
    base = []
    mRate = rate/12
    for i in range(terms):
        base +=[i]
        savings = ((savings[-1]*(1+mRate))+monthly)
    return base, savings

# different monthly amount, same interest rate
def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire: ' +str(monthly))
        plt.legend(loc = 'upper left')

displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40* 12)
        
# same monthly amount, different interest rates
def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire: ' +str(month) + ': ' + str(int(rate*100)))
        plt.legend(loc = 'upper left')

displayRetireWRates(800, [.03, .05, .07], 40* 12)

# display results for both cases




