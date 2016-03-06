# copute the coefficient of variation of [10, 4, 12, 15, 20, 5] to 3 decimal places.
L = [10, 4, 12, 15, 20, 5]
tot = 0
for ele in L:
    tot += ele

tot = (10+4+12+15+20+5)
print tot
mean = tot/len(L)
print mean
summation = (10-11)**2 + (4-11)**2 +(12-11)**2+(15-11)**2 + (20-11)**2+(5-11)**2
print summation
stdD= (summation/6)**0.5
print  stdD
coef = 5.477/mean
print coef

# mean = tot/len(L)
# summation = 0
# for ele in L:
#     summation += (ele - mean)**2/len(L)
#
# stdDv = summation**0.5
# coefficient = stdDv/mean
# print coefficient

