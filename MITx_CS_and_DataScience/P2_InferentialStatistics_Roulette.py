'''
Inferential Statistics
---------------------------
Law of Large Numbers - in repeted independent tests with the same actual 
probability p of a particular outcome in each test, the chance that the 
fraction of times that outcome occurs differs from p converges to zero as 
the number of trials goes to infinity

Gambler's Fallacy
Regression to the mean
Central Limit Theorem (CLT)

Empirical Rule:
    - ~ 68% of data within 1 STDV of the mean
    - ~ 95% of data within 1.96 STDV of the mean
    - ~ 99.7% of data within 3 STDV of the mean

Normal Distributions 

SciPy library
    scipy.integrate.quad
    
NIPS, CVPR, ICML, ICLR, ICCV et ACL    
'''
import random

class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1,37):
            self.pockets.append(i)
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
        self.pocketOdds = len(self.pockets) - 1.0
    def spin(self):
        self.ball = random.choice(self.pockets)
    def isBlack(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10)\
            or (self.ball>18 and self.ball<=28)):
            return self.ball%2 == 0
        else:
            return self.ball%2 == 1
    def isRed(self):
        return type(self.ball) == int and not self.isBlack()
    def betBlack(self, amt):
        if self.isBlack():
            return amt*self.blackOdds
        else: return -amt
    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds
        else: return -amt*self.redOdds
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else: return -amt
    def __str__(self):
        return 'Fair Roulette'

def playRoulette(game, numSpins, toPrint = True):
    luckyNumber = '2'
    bet = 1
    totRed, totBlack, totPocket = 0.0, 0.0, 0.0
    for i in range(numSpins):
        game.spin()
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPocket += game.betPocket(luckyNumber, bet)
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting red =',
              str(100*totRed/numSpins) + '%')
        print('Expected return betting black =', 
              str(100*totBlack/numSpins) + '%')
        print('Expected return betting', luckyNumber, '=',\
              str(100*totPocket/numSpins) + '%\n')
    return (totRed/numSpins, totBlack/numSpins, totPocket/numSpins)

#numSpins = 1000000
#game = FairRoulette()
#playRoulette(game, numSpins)

class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return 'European Roulette'

class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self):
        return 'American Roulette'

def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = []
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize, toPrint)
        pocketReturns.append(trialVals[2])
    return pocketReturns

random.seed(0)
numTrials = 20
resultDict = {}
games = (FairRoulette, EuRoulette, AmRoulette)
for G in games:
    resultDict[G().__str__()] = []
for numSpins in (100, 1000, 10000, 100000):
    print('\nSimulate betting a pocket for', numTrials,
          'trials of',
          numSpins, 'spins each')
    for G in games:
        pocketReturns = findPocketReturn(G(), numTrials,
                                         numSpins, False)
        print('Exp. return for', G(), '=',
             str(100*sum(pocketReturns)/float(len(pocketReturns))) + '%')

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

#random.seed(0)
#numTrials = 20
#resultDict = {}
#games = (FairRoulette, EuRoulette, AmRoulette)
#for G in games:
#    resultDict[G().__str__()] = []
#for numSpins in (100, 1000, 10000):
#    print('\nSimulate betting a pocket for', numTrials,
#          'trials of', numSpins, 'spins each')
#    for G in games:
#        pocketReturns = findPocketReturn(G(), 20, numSpins, False)
#        mean, std = getMeanAndStd(pocketReturns)
#        resultDict[G().__str__()].append((numSpins,
#                                          100*mean, 100*std))
#        print('Exp. return for', G(), '=', str(round(100*mean, 3))
#              + '%,', '+/- ' + str(round(100*1.96*std, 3))
#              + '% with 95% confidence')
              

def plotReturn(resultDict):
    for k in resultDict:
        xVals, yVals, eVals = [], [], []
        for trial in resultDict[k]:
            xVals.append(trial[0])
            yVals.append(trial[1])
            eVals.append(trial[2])
        pylab.errorbar(xVals, yVals, yerr = eVals, label = k, marker = 'o')
    pylab.legend()
    pylab.xlabel('Spins per trial', fontsize = 'x-large')
    pylab.ylabel('Expected percentage return', fontsize = 'x-large')
    pylab.title('Expected Return Betting a Pocket', fontsize = 'x-large')
    pylab.semilogx()
    minX, maxX = pylab.xlim()
    pylab.xlim(1, maxX + 100000)
#    
#plotReturn(resultDict)
#assert False

def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random() 
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color = color, label = legend,
               weights = pylab.array(len(means)*[1.0])/len(means),
               hatch = style)
    return getMeanAndStd(means)
 
#mean, std = plotMeans(1, 100000, 11, '1 die', 'b', '*')
#print('Mean of rolling 1 die =', mean, 'Std =', std)
#mean, std = plotMeans(50, 100000, 11, 'Mean of 50 dice', 'r', '//')
#print('Mean of rolling 50 dice =', mean, 'Std =', std)
#pylab.title('Rolling Continuous Dice')
#pylab.xlabel('Value')
#pylab.ylabel('Probability')
#pylab.legend()


def leaveAhead(game, stake, bet, numTrials):
    numAhead = 0.0
    for t in range(numTrials):
        bankRoll = stake
        curBet = bet
        while bankRoll > 0 and bankRoll <= 2*stake:
            game.spin()
            outcome = game.betBlack(curBet)
            bankRoll += outcome
            if outcome < 0:
                curBet = min(2*curBet, bankRoll)
            #print curBet, bankRoll
        if bankRoll > stake:
            numAhead += 1
    return numAhead/numTrials

#stake = 1
#bet = 1
#numTrials = 100000
#successProb, stakes = [], []
#for i in range(10):
#    stakes.append(10**i)
#    successProb.append(leaveAhead(AmRoulette(), 10**i, bet, numTrials))
#pylab.plot(stakes, successProb)
#pylab.xlabel('Bankroll')
#pylab.ylabel('Probability of Winning')
#pylab.semilogx()
#pylab.show()

###############################################################################
###############################################################################

import random, pylab

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
#set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1

dist = []
for i in range(100000):
    # generating normal distributions
    dist.append(random.gauss(0, 30))
pylab.hist(dist, 30)

import scipy.integrate

def gaussian(x, mu, sigma):
    # ex - if Uniform Distribution
#    return 37
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2
    
def checkEmpirical(numTrials):
  for t in range(numTrials):
     mu = random.randint(-10, 10)
     sigma = random.randint(1, 10)
     print('For mu =', mu, 'and sigma =', sigma)
     for numStd in (1, 1.96, 3):
        area = scipy.integrate.quad(gaussian,
                                    mu-numStd*sigma,
                                    mu+numStd*sigma,
                                    (mu, sigma))[0]
        print('  Fraction within', numStd, 'std =', round(area, 4))
 
checkEmpirical(3)


###############################################################################
###############################################################################
'''    
Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and 
outputs the standard deviation of the lengths of the strings. 
Return float('NaN') if L is empty.
'''

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if (len(L) == 0):
        return float('NaN')
    
    # compute mean first
    sumVals = 0
    for s in L:
        sumVals += len(s)
    meanVals = sumVals / len(L)

    # compute variance (average squared deviation from mean)
    sumDevSquared = 0
    for s in L:
        sumDevSquared += (len(s) - meanVals)**2
    variance = sumDevSquared / len(L)

    # standard deviation is the square root of the variance
    stdDev = variance**(.5)

    return stdDev








