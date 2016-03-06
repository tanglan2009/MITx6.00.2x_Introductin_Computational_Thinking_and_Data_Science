import random
tots = [0.00] * 3
maxVals = [0.0] * 3
mean = 100.0
stdDevs = [0.0, 20.0, 40.0]
for i in range(1000):
    for j in range(len(tots)):
        next = random.gauss(mean, stdDevs[j])
        print  "next", next
        tots[j] += next
        if next > maxVals[j]:
            maxVals[j] = next
print tots


# i = 0
# j = 0 #len(j)= 3
# next = random.gauss(100.0, stdDevs[0])
# next = 100.0
# tots[0]=100.0
# maxVals[0] = 100.0
#
# j = 1
# next = random.gauss(100.0, stdDevs[1])
# tots[1]=0.00 + random.gauss(100.0, 20)
# tots[1] = 80 - 120
#
# j = 2
# next = random.gauss(100.0, 40.0)
# tots = 0.00 + random.gauss(100.0, 40.0)
# tots[2] = 60 -140
#
# i = 1
# j = 0
# tots[0]=100.0+100.0
import random
tots = [0.00]*3
maxVals = [0.0]*3
mean = 100.0
stdDevs = [0.0, 20.0, 40.0]
for i in range(1000):
    for j in range(len(tots)):
        next = random.gauss(mean, stdDevs[j])
        tots[j] += next
        if next > maxVals[j]:
            maxVals[j] = next
print tots


