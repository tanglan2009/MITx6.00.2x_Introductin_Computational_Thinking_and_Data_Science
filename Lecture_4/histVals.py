import random,  pylab
vals = []
for i in range(100000):
    num = random.random()
    vals.append(num)
pylab.hist(vals, bins = 11)
# xmin, xmax = pylab.xlim()
# ymin, ymax = pylab.ylim()
# print 'x-range =', xmin, '-', xmax
# print 'y-range =', ymin, '-', ymax
#pylab.figure
pylab.hist(vals, bins = 11)
pylab.show()