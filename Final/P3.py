import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
     # TO DO
    pRabbitReproduction = 1.0 - CURRENTRABBITPOP/MAXRABBITPOP
    for i in range(CURRENTRABBITPOP):
        if random.random() < pRabbitReproduction:
            CURRENTRABBITPOP += 1
        if CURRENTRABBITPOP =


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    pFoxEatsRabbit = CURRENTRABBITPOP/float(MAXRABBITPOP)
    for i in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10 and random.random() < pFoxEatsRabbit:
            CURRENTRABBITPOP -= 1
            if random.random() < 1/float(3):
                CURRENTFOXPOP += 1
        else:
            if CURRENTFOXPOP > 10 and random.random() < 9/float(10):
                CURRENTFOXPOP -= 1

def runSimulation(timeSteps):
    rabbitPop = []
    foxPop = []
    for i in range(timeSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitPop.append(CURRENTRABBITPOP)
        foxPop.append(CURRENTFOXPOP)
    return(rabbitPop, foxPop)


