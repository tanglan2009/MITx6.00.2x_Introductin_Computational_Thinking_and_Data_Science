import random

# def rollDie():
#     """Returns an int between 1 and 6."""                   # underdetermined
def rollDie():
    """Returns a random int between 1 and 6."""             # Nondetermnistic
    return random.randint(1, 6)

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    return result

print rollN(5)

def getTarget(goal):
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries += 1
        result = rollN(numRolls)
        if result == goal:
            return numTries

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        total += getTarget(goal)
    aveNumTries = total /float(numTrials)
    print 'Porbability =', 1.0/aveNumTries


print runSim('11111', 100)
print runSim('54324', 100)