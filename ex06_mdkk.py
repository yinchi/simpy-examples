# 06 M/D/k/k queue

'''
The M/D/k/k queue is similar to the M/M/k/k queue from Example 4,
except the service times are now constant (deterministic) rather
than random.
'''

import simpy
import random

class SimStats:
    def __init__(self):
        self.nArrived = 0
        self.nBlocked = 0

# Poisson process generator
def generator(env, stats, q, lambd, tau):
    while True:
        yield env.timeout(random.expovariate(lambd))
        r = request(env, stats, q,
                    serviceTime = 1/tau)
        env.process(r)

# Request handling
def request(env, stats, q, serviceTime):
    stats.nArrived += 1
    #if (stats.nArrived % 100_000 == 0):
        #print(stats.nArrived,'arrivals at time',env.now)
    arrTime = env.now

    if q.count < q.capacity:
        with q.request() as req:
            yield req # get the resource
            yield env.timeout(serviceTime) # hold the resource for the specified time
            # resource automatically released at end of "with" block
    else:
        stats.nBlocked += 1

def erlangB(load,nServers):
    inv = 1
    for m in range(1,nServers+1): # range does not include the last number, so we need to add 1
        inv = 1 + m/load * inv
    return 1/inv

if __name__ == "__main__":
    lambd = 9
    tau = 1

    env = simpy.Environment()
    stats = SimStats()
    q = simpy.Resource(env, capacity = 10)
    env.process(generator(env, stats, q, lambd, tau))
    env.run(until=100_000)

    print('Blocking probability:', stats.nBlocked/stats.nArrived)
    print('Exact solution:', erlangB(lambd*tau, q.capacity))
