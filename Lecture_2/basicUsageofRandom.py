import random
print random.random()               # Random float x, 0.0 <= x < 1.0
print random.uniform(1, 10)         # Random float x, 1.0 <= x < 10.0
print random.randint(1, 10)         # Integer from 1 to 10, endpoints included
print random.randrange(0, 101, 2)      # Even integer from 0 to 100
print random.choice('abcdefghij')       # Choose a random element

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print items

print random.sample([1, 2, 3, 4, 5], 3)       # Choose 3 elements