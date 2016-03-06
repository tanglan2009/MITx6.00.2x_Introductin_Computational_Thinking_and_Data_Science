import random

def pickBall():
    ballsInTheBucket = ['r', 'r', 'r','r', 'g', 'g', 'g','g']
    chosenBalls = []
    for pick in range(3):       # For three trials, pick a ball
        ball = random.choice(ballsInTheBucket)
        # Remove the chosen ball from the bucket
        ballsInTheBucket.remove(ball)
        # add the ball to the chosenBalls LIST
        chosenBalls.append(ball)
    if chosenBalls[0]== chosenBalls[1] == chosenBalls [2]:
        return True
    return False



def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    numTrue = 0
    for trial in range(numTrials):
        if pickBall():
            numTrue += 1
    return float(numTrue)/numTrials
print noReplacementSimulation(10000)
