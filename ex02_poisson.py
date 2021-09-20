# 02 - A Poisson process in simpy

'''
A Poisson process is defined by three conditions:
1. The cumulative number of events at time 0 is zero.
2. The number of events in two disjoint intervals are independent.
3. The number of events in an interval of length t is a Poisson
   random variable with mean lambd*t (we would use lambda but
   that is a reserved keyword in Python).

We use the fact that inter-arrivals in a Poisson process are
independent and exponentially distributed with mean 1/lambd.
'''

import simpy
import random

# Poisson process generator
def generator(env, lambd):
    nArrivals = 0
    while True:
        yield env.timeout(random.expovariate(lambd))
        nArrivals += 1
        print(nArrivals, env.now)

env = simpy.Environment()
env.process(generator(env, 1))
print('arr','time')
env.run(until=20)
