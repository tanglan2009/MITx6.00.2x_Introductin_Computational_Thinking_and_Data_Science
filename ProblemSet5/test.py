import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import *

fh = open('mit_map.txt')
for line in fh:
    numList = line.split()
    srcNode = int(numList[0])
    destNode = int(numList[1])
    totalDistance = int(numList[2])
    outdoorDistance = int(numList[3])
print srcNode, destNode, totalDistance, outdoorDistance


mitMap = WeightedDigraph()
na = Node('32')
nb = Node('36')
nc = Node('57')
nd = Node('76')
mitMap.addNode(na)
mitMap.addNode(nb)
mitMap.addNode(nc)
e1 = WeightedEdge(na, nb, 70, 0)
print e1
print e1.getTotalDistance()
print e1.getOutdoorDistance()
e2 = WeightedEdge(nb, na, 70, 0)
e3 = WeightedEdge(na, nc, 30, 0)
print e2
print e3
mitMap.addEdge(e1)
mitMap.addEdge(e2)
mitMap.addEdge(e3)
print mitMap

# 32 36 70 0
# 36 32 70 0
# 32 57 30 0
# 57 32 30 0
# 32 76 80 50