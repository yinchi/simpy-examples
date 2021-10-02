# Example 10: queue with two different request types

'''
Here, we model a queue with two different request types
(0 and 1). We set a reservation treshold such that Type 1
requests cannot use the last `res1` idle servers in the
queue.
'''

import simpy
import random

class SimStats:
    def __init__(self):
        self.nArrived = [0, 0]
        self.nBlocked = [0, 0]

# Poisson process generator
def generator(env, stats, q, typeID, lambd, tau, res):
    while True:
        yield env.timeout(random.expovariate(lambd))
        r = request(env, stats, q, typeID,
                    random.expovariate(1/tau),
                    res)
        env.process(r)

# Request handling
def request(env, stats, q, typeID, serviceTime, res):
    stats.nArrived[typeID] += 1
    if q.count < q.capacity - res:
        with q.request() as req:
            yield req # get the resource
            yield env.timeout(serviceTime) # hold the resource for the specified time
            # resource automatically released at end of "with" block
    else:
        stats.nBlocked[typeID] += 1

if __name__ == "__main__":
    lambd0 = 3
    lambd1 = 3
    tau0 = 1
    tau1 = 1
    res0 = 0
    res1 = 1

    # Generating confidence intervals is left as an excercise.
    env = simpy.Environment()
    stats = SimStats()
    q = simpy.Resource(env, capacity = 10)
    env.process(generator(env, stats, q, 0, lambd0, tau0, res0))
    env.process(generator(env, stats, q, 1, lambd1, tau1, res1))
    env.run(until=100_000)

    print('Blocking probabilities:', stats.nBlocked[0]/stats.nArrived[0], stats.nBlocked[1]/stats.nArrived[1])