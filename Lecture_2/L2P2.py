import random
print random.randint(1, 5)
print random.choice(['apple', 'banana', 'cat'])

def genEven():
    xList = []
    for x in range(100):
        if x%2 == 0:
            xList.append(x)
    return random.choice(xList)