# 03 - An M/M/k queue with abandonment in simpy

'''
An M/M/k queue has Poisson arrivals, exponentially distributed
service times, and k servers.  Requests will remain in the queue
until served or until some exponentially distributed 'patience'
time has elapsed.

Note that queueing systems with Poisson arrivals exhibit the
"PASTA" property (Poisson arrivals see time averages).  For example,
the mean queue length seen by new arrivals (excluding the new arrival)
is the mean queue length over time.

For a regular M/M/k queue, set the patience paramter to float('inf').
See Section 9 of the Zukerman textbook
(http://www.ee.cityu.edu.hk/~zukerman/classnotes.pdf)
for more on the M/M/k queue, including formulas for the mean wait time
and mean buffer length.

Parameters:
lambd - arrival rate (again we would use lambda but it is a reserved
        keyword in Python
tau   - mean service rate
patience - mean request patience

'''

import simpy
import random
from runstats import Statistics

class SimStats:
    def __init__(self):
        self.nArrived = 0
        self.nAbandoned = 0
        self.wait = Statistics() # wait of requests that do not abandon
        self.waitAbandoned = Statistics() # wait of requests that do abandon
        self.waitAll = Statistics() # wait of all requests
        self.bufferLen = Statistics() # queue buffer length seen by new requests

# Poisson process generator
def generator(env, stats, q, lambd, tau, patience):
    while True:
        yield env.timeout(random.expovariate(lambd))
        r = request(env,
                    stats,
                    q,
                    serviceTime = random.expovariate(1/tau),
                    patience = random.expovariate(1/patience))
        env.process(r)

# Request handling
def request(env, stats, q, serviceTime, patience):
    stats.nArrived += 1
    if (stats.nArrived % 100_000 == 0):
        print(stats.nArrived,'arrivals at time',env.now)
    arrTime = env.now

    # q.users returns requests in service, q.queue returns requests in the buffer
    stats.bufferLen.push(len(q.queue))

    with q.request() as req:
        results = yield req | env.timeout(patience)
        t = env.now - arrTime
        stats.waitAll.push(t)

        if req in results: # we got service
            stats.wait.push(t)
            yield env.timeout(serviceTime)

        else: # we abandoned
            stats.waitAbandoned.push(t)
            stats.nAbandoned += 1

        # resource unit automatically released here

env = simpy.Environment()
stats = SimStats()
q = simpy.Resource(env, capacity = 10)
env.process(generator(env, stats, q, lambd = 9, tau = 1, patience = 0.1))
env.run(until=100_000)

print('Abandonment rate:', stats.nAbandoned/stats.nArrived)
print('Mean wait of served/in service requests:', stats.wait.mean())
print('Mean wait of abandoned requests:', stats.waitAbandoned.mean())
print('Mean wait of all requests:', stats.waitAll.mean())
print('Mean buffer length:', stats.bufferLen.mean())
