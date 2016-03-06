import pylab
hand = open('testText')
for line in hand:
    line = line.rstrip()
    word = line.split(' ')
    print word
    letterE = []
    for letter in word:
        if letter == 'e' or letter == 'a' or letter == 'o':
            letterE.append(letter)
    pylab.hist(letterE, bins= 10)
    pylab.xlim(-1.0, 2.0)
    pylab.show()