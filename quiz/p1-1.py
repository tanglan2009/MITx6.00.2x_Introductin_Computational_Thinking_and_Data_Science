import random



def f(x):
    # x is an integer
    return int(x + random.choice([0.25, 0.5, 0.75]))


print f(1)
print f(2)
print f(3)