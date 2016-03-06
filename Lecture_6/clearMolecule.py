import pylab, random
def clear(n, p, steps):
    """Assumes n & steps positive ints, p a float
        n: the initial number of molecules
        p: the probability of a molecule being cleared
        steps: the length of the simulation"""
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*(1-p)**t)
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    #pylab.semilogy()

    pylab.title('Clearance of Drug')
#
# clear(1000, 0.01, 1000)
# pylab.show()


# monty carlos simulation
def clearSim(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numLeft = numRemaining[-1]
        for m in range(numRemaining[-1]):
            if random.random()<= clearProb:
                numLeft -= 1
        if t != 0 and t%100 == 0:
            numLeft += numLeft
        numRemaining.append(numLeft)
    pylab.plot(numRemaining, 'ro', label = 'Simulation')

clear(1000, 0.01, 500)
clearSim(1000, 0.01, 500)
pylab.xlabel('Number of Steps')
pylab.ylabel('Number of Molecules')
pylab.legend()
pylab.show()