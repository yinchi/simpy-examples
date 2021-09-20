# 07 M/M/k/k vs M/D/k/k

'''
Because of insensitivity, the request blocking probability of the
M/G/k/k queue, of which the M/M/k/k and M/D/k/k queues are subtypes,
is insensitive to the shape of the service time distribution apart
from the mean.

Here, we use confidence intervals to demonstrate this for different
arrival rates.  We will plot the results in Example 8.
'''

import simpy
import numpy as np
import ex04_mmkk as mmkk
import ex06_mdkk as mdkk
from ex05_confidence_intervals import ci

def mean_err(ci):
    # convert confidence interval from (min,max) to (mean,error_bound)
    return (np.mean(ci), np.max(ci) - np.mean(ci))

def sim_mmkk(lambd, tau = 1):
    mmkk_results = np.empty(10)
    for i in range(10):
        mmkk_env = simpy.Environment()
        mmkk_stats = mmkk.SimStats()
        mmkk_q = simpy.Resource(mmkk_env, capacity = 10)
        mmkk_env.process(mmkk.generator(mmkk_env, mmkk_stats, mmkk_q, lambd, tau))
        mmkk_env.run(until=100_000.0/lambd)
        mmkk_results[i] = mmkk_stats.nBlocked/mmkk_stats.nArrived
    return mean_err(ci(mmkk_results))

def sim_mdkk(lambd, tau = 1):
    mdkk_results = np.empty(10)
    for i in range(10):
        mdkk_env = simpy.Environment()
        mdkk_stats = mdkk.SimStats()
        mdkk_q = simpy.Resource(mdkk_env, capacity = 10)
        mdkk_env.process(mdkk.generator(mdkk_env, mdkk_stats, mdkk_q, lambd, tau))
        mdkk_env.run(until=100_000.0/lambd)
        mdkk_results[i] = mdkk_stats.nBlocked/mdkk_stats.nArrived
    return mean_err(ci(mdkk_results))

# lambd = 3 to 15.1 by 1 (we make the endpoint a bit bigger than 15 to ensure 15 is included in the range)
for lambd in np.arange(3,15.1,1):
    print(lambd, *sim_mmkk(lambd), *sim_mdkk(lambd))
