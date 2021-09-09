# 01 - the random library

# Make sure to use Python 3, not 2.
# For full documentation, see https://docs.python.org/3/library/random.html

import random

# Set the random seed for the same results each time
random.seed(1)
print("Uniformly distributed random variate between 0 (inclusive) and 1 (exclusive):", random.random())

# sample(seq,k) chooses k samples from seq without replacement
print("Random ordering of 0..5:", random.sample(range(6),6))

# Random coin flip
print("Random coin flip:", random.choice(['heads', 'tails']))

# Random sequence of 10 coin flips
# choices(seq,k) chooses k samples from seq with replacement
print("Random coin flip:", random.choices(['H', 'T'], k=10))

# Exponential distribution
print("Exponential random variates with mean 0.25:",
      random.expovariate(4),
      random.expovariate(4),
      random.expovariate(4),
      random.expovariate(4))
print("Exponential random variates with mean 4:",
      random.expovariate(1/4),
      random.expovariate(1/4),
      random.expovariate(1/4),
      random.expovariate(1/4))
