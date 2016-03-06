
def stdDev(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X
    """
    mean = float(sum(X))/len(X)
    print 'mean = ', mean
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    print tot
    #return (tot/len(X))**0.5

print stdDev([0,1,2,3,4,5,6,7,8])
print stdDev([5,10,10,10,15])
print stdDev([0,1,2,4,6,8])
print stdDev([6,7,11,12,13,15])
print stdDev([9,0,0,3,3,3,6,6])