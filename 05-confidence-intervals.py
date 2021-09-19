# 05 Confidence intervals

'''
If we assume that a particular distribution is normal, then
the Student's t-distribution can be used to compute
the confidence interval for the mean of the distribution.

A n% confidence interval means that the
true mean of a distribution falls within the
computed confidence interval with an estimated 95%
probability.

Confidence intervals are often used to describe the
uncertainty in sampled values such as survey data
or simulation results.
'''

import numpy as np
import scipy.stats as st

def ci(data):
    return st.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(data), scale=st.sem(data))

def between(x,ci):
    return x >= ci[0] and x <= ci[1]

def test(mu,sigma):
    # mu and sigma are the true mean and sample deviation

    # empirical means
    m = np.empty(10)

    # generate distributions
    for i in range(10):
        s = np.random.normal(mu, sigma, 10)
        m[i] = np.mean(s)

    # Is the true mean within the C.I. of the empirical means (m)?
    return between(mu, ci(m))

count = 0
nTests = 10000

for x in range(nTests):
    if test(0,1):
        count += 1
print('Proportion of tests where the 95% confidence interval includes the true mean:', count/nTests)
