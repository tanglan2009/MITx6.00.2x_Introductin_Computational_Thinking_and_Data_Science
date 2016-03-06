import random


#def getAverage(numRolls = 50, numTrials):
maxCounts = []
for j in range(5):
    numList = []
    maxCountsPerTrial = None
    for i in range(22):
        numList.append(random.choice([1,2,3,3,4,4,5,6,6,6,7]))
    print numList
    print numList.count(1), numList.count(2), numList.count(3), numList.count(4), numList.count(5), numList.count(6), numList.count(7)
    for num in numList:
        if numList.count(num) > maxCountsPerTrial:
            maxCountsPerTrial = numList.count(num)
    maxCounts.append(maxCountsPerTrial)

print maxCounts
