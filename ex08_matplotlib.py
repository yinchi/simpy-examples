# Example 08: plotting using Matplotlib

'''
Here we plot the results of Example 7, which shows the simulation results
for an M/M/10/10 queue and an M/D/10/10 queue with respect to the offered load.
For convienience, the output of Example 7 is loaded from a text file rather
than running the simulations again.
'''

import numpy as np
import matplotlib.pyplot as plt

# each column of the file is saved to a separate variable
# when unpack = True
x, y1, yerr1, y2, yerr2 = np.loadtxt('ex07_mmkk_mdkk.txt',unpack=True)

plt.errorbar(x,y1,yerr1,fmt='b',capsize=8, label='M/M/10/10')
plt.errorbar(x,y2,yerr2,fmt='r--',capsize=5, label='M/D/10/10')
plt.xlabel('λ, Arrival rate', fontsize = 14) # check Unicode support
plt.ylabel('Request blocking probability', fontsize = 14)
plt.legend(loc='upper left')
plt.show()
