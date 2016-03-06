import random, pylab

# def makeNormal(mean, sd, numSamples):
#     samples = []
#     for i in range(numSamples):
#         samples.append(random.gauss(mean, sd))
#     pylab.hist(samples, bins = 101)
#
# random.seed(0)
# makeNormal(0.0, 1.0, 100000)
# pylab.show()

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])

def rollDie2(numRoll):
    sum = 0.0
    for i in range(numRoll):
        result = random.random()
        if result < 0.55:
            sum += 1
        else:
            sum -= 1
    return sum

def makesumsim( numTrial = 100):
    sumList = []
    for i in range(numTrial):
        #sumList.append(rollDie() + rollDie())
        sumList.append(rollDie2(5))
    return sumList


def makePlot(sumList):
    pylab.hist(sumList, bins = 100)

random.seed(0)
makePlot(makesumsim(100))
pylab.show()
# print makesumsim(100)

