import pylab, random

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    #print discardHeader
    for line in dataFile:
        d, m = line.split()
       # print d, m
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

print getData('springData.txt')

def plotData(fileName):
    xVals, yVals = getData(fileName)
    print xVals
    print yVals
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    print xVals
    print yVals
    # force = []
    # for val in xVals:
    #     val = val * 9.81
    #     force.append(val)

    xVals = xVals * 9.81        # convert mass to force (F = mg)
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters')

# plotData('springData.txt')
# pylab.show()

def testErrors(ntrials = 10000, npts = 100):
    results = [0] * ntrials
    for i in xrange(ntrials):
        s = 0           # sum of random points
        for j in xrange(npts):