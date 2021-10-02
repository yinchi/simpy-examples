# Example 09: two arrival processes

'''
So far, we have modelled systems with a single arrival
process.  Here, we model two arrival processes.  We see
that the Simpy environment automatically triggers events
from both processes in the correct order.

This behavior has already been seen in the previous queue
examples, where *each* arrival spawns its own process to:

1. Queue for service (if the queue is full, but has a buffer).
2. Obtain the required resource.
3. Wait for the designated service time.
4. Release the obtained resource.

Here, since there are only two processes and all events
occur at *known* times, it should be easier to understand
the internal workings of the Simpy simulation.

Note that events can be scheduled for the same time.  Simpy
does not guarantee which event will be triggered first.
'''

import simpy

def generator(env, t, s):
    while True:
        yield env.timeout(t)
        print('Generator', s, 'at time:', env.now)

env = simpy.Environment()

# Create two arrival processes
env.process(generator(env, 1, 'A')) # generate arrivals every second
env.process(generator(env, 5, 'B')) # generate arrivals every 5 seconds

env.run(until=20)