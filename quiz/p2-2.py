import random
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])


def checkPascal(numTrials):

    """Assumes numTrials an int > 0
 Prints an estimate of the probability of winning"""

    proList = []
    for j in range(numTrials):
        numWins = 0.0

        d1 = rollDie()
        d2 = rollDie()
        d3 = rollDie()
        if (d1 == 6 and d2 == 6) or (d1 == 6 and d3 == 6) or (d2 == 6 and d3 == 6):
            numWins += 1
        proList.append(float(numWins)/(6*6*6))
    print proList
    print 'Probability of winning =', float(numWins)/numTrials

print checkPascal(1000)