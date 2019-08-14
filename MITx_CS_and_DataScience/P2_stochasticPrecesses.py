# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:46:17 2019

@author: User
"""

''' 
Stochastic thinking
- Copenhagen Doctrine - at its most fundamental level, the behavior of the
                        physical world cannot be predicted
- Predictive nondeterminism 
- Stochastic Precesses - ongoing process where the next state might depend on
                         both the previous states and some random element
- Morals:
    - it takes a lot of trials to get a good estimate of the frequency of
      occurrence of a rare event
    - sample probability <> actual probability

    
'''

import random
random.seed()

def rollDie():
    """ returns a random int btw 1 and 6
        nondeterministic implementation"""
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

print(testRoll(5))    



import random
random.seed(0)
 
def rollDie():
    """returns a random int between 1 and 6
       deterministic implementation """
    return random.choice([1,2,3,4,5,6])
 
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)
print(testRoll(5))     

###############################################################################
###############################################################################

import random
random.seed()

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability =',
          round(1/(6**len(goal)), 8)) 
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability  =',
          round(estProbability, 8))


random.seed(0)
def runSim1(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability =',
          round(1/(6**len(goal)), 8)) 
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability  =',
          round(estProbability, 4))
    
runSim1('11111', 1000000)
runSim('11111', 1000000)

###############################################################################
###############################################################################

random.seed()
def fracBoxCars(numTests):
    numBoxCars = 0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars/numTests
    
print('Frequency of double 6 =',
      str(fracBoxCars(100000)*100) + '%')


    
#runSim('11111', 1000)

random.seed(0)
def fracBoxCars(numTests):
    numBoxCars = 0.0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars/numTests
    
print('Frequency of double 6 =',
      str(fracBoxCars(100000)*100) + '%')


    
import random
random.randint(1, 5)

random.choice(['apple', 'banana', 'cat'])

# random even number
random.randrange(0,100,2)   
random.choice(range(0, 100, 2))

random.randrange(10,21,2)  

# deterministic program - returns an even number between 9 and 21.
def deterministicNumber():
    random.seed(0) # This will be discussed in the video "Drunken Simulations"
    return 2 * random.randint(5, 10)
print(deterministicNumber())


# uniformly distributed stochastic program - returns an even number between 9 and 21.
import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return 2 * random.randint(5, 10)
# OR
#   return random.randrange(10, 22, 2)
#   return random.randrange(10,21,2)

###############################################################################
d1 = {}
for i in range(10000):
    x = random.randrange(10) 
    d1[x] = d1.get(x, 0) + 1
d2 = {}
for i in range(10000):
    x = int(random.random()*10)
    d2[x] = d2.get(x, 0) + 1
d3 = {}
for i in range(10000):
    x = random.randint(0, 10)
    d3[x] = d3.get(x, 0) + 1
###############################################################################
    
# probability to have 111111
    ''' 1/(6**5) = 0.0001286...'''

