
'''
Inferential Statistics
-------------------------------
- population - a set of examples
- sample - a proper subset of a population
    - random sample - tends to exhibit the same properties as the population 
                      from which it is drawn
  
The Central Limit Theorem (CLT)
- the means of the samples in a set of samples (the sample means) will be
  approximately normally distributed
- this normal distribution will have a mean close to the mean of the population
- the variance of the sample means will be close to the variance of the 
  population divided by the sample size

Monte Carlo
- 


'''

import pylab

#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
pylab.rcParams['lines.markersize'] = 10
#set number of times marker is shown when displaying legend
pylab.rcParams['legend.numpoints'] = 1

import random, numpy

def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = numpy.std(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. = ' + str(curEst) +\
          ', Std. dev. = ' + str(round(sDev, 6))\
          + ', Needles = ' + str(numNeedles))
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/1.96:
        curEst, sDev = getEst(numNeedles, numTrials)
        # method - double the size in order to have good results very quickly
        numNeedles *= 2
    return curEst

random.seed(0)
estPi(0.005, 100)


def integrate(f, a, b, step):
    yVals, xVals = [], []
    xVal = a
    while xVal <= b:
        xVals.append(xVal)
        yVals.append(f(xVal))
        xVal += step
    pylab.plot(xVals, yVals)
    pylab.title('sin(x)')
    pylab.xlim(a, b)
    xUnders, yUnders, xOvers, yOvers = [],[],[],[]
    for i in range(500):
        xVal = random.uniform(a, b)
        yVal = random.uniform(0, 1)
        if yVal < f(xVal):
            xUnders.append(xVal)
            yUnders.append(yVal)
        else:
            xOvers.append(xVal)
            yOvers.append(yVal)
    pylab.plot(xUnders, yUnders, 'ro')
    pylab.plot(xOvers, yOvers, 'ko')
    pylab.xlim(a, b)
    ratio = len(xUnders)/(len(xUnders) + len(yUnders))
    print(ratio)
    print(ratio*b)
    
def one(x):
    return 0.9
    
#integrate(one, 0, math.pi, 0.001)
    
###############################################################################
###############################################################################
    
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

#L = [1,1,1,1,2]
#pylab.hist(L)
#factor = pylab.array(len(L)*[1])/len(L)
#print(factor)
#pylab.figure()
#pylab.hist(L, weights = factor)

def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random() 
        means.append(vals/float(numDice))
    # weights keyword - scaled to probabilities rather than to absolute counts
    # hatch keyword - to visual distinguish one histogram from another
    pylab.hist(means, numBins, color = color, label = legend,
               weights = pylab.array(len(means)*[1])/len(means),
               hatch = style)
    return getMeanAndStd(means)
 
#mean, std = plotMeans(1, 1000000, 19, '1 die', 'b', '*')
#print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)
#mean, std = plotMeans(50, 1000000, 19, 'Mean of 50 dice', 'r', '//')
#print('Mean of rolling 50 dice =', str(mean) + ',', 'Std =', std)
#pylab.title('Rolling Continuous Dice')
#pylab.xlabel('Value')
#pylab.ylabel('Probability')
#pylab.legend() 
