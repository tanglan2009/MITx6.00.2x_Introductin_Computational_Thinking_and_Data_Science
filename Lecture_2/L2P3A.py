import random
def deterministicNumber():
    """Deterministically generates and returns an evern number between 8 and 21"""
    numberList = []
    for i in range(9, 21):
        if i%2 ==0:
            numberList.append(i)
    for num in numberList:
        return num