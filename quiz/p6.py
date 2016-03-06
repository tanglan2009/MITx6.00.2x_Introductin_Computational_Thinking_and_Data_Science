import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title= None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title is not None:
        pylab.title(title)
    pylab.hist(values, bins = numBins)
    pylab.show()

#makeHistogram([1,2], 4, "Aaa", "Bbb")
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    # maxCounts = []
    # for j in range(numTrials):
    #     numList = []
    #     maxCountsPerTrial = None
    #     # maxNumber = None
    #     for i in range(numRolls):
    #         numList.append(die.roll())
    #     for number in die.possibleVals:
    #         count = numList.count(number)
    #         if count > maxCountsPerTrial:
    #             maxCountsPerTrial = count
    #             # maxNumber = number
    #     # maxCounts.append(maxCountsPerTrial)
    #     # for num in numList:
    #     #     if numList.count(num) > maxCountsPerTrial:
    #     #         maxCountsPerTrial = numList.count(num)
    #     maxCounts.append(maxCountsPerTrial)
    #
    #     # sum += maxCountsPerTrial
    # makeHistogram(maxCounts, numBins = 10, xLabel = 'longest run', yLabel = 'numTrial', title= None)
    # return getMeanAndStd(maxCounts)[0]

    runs = []
    for _ in xrange(numTrials):
        rolls = []
        for __ in xrange(numRolls):
            rolls.append(die.roll())
        runs.append(longest_run(rolls))
    makeHistogram(runs, 10, "size of longest run", "number of runs")
    return sum(runs)/float(len(runs))

def longest_run(l):
    longest = 1
    current = 1
    hold_value = l[0]
    for i in xrange(1,len(l)):
        if l[i] == hold_value:
             current += 1
        else:
            hold_value = l[i]
            if current > longest: longest = current
            current = 1
    if current > longest: longest = current
    return longest

# One test case

print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)
# print getAverage(Die([1,2,3,4,5,6]), 50, 1000)