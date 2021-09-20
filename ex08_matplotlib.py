# Example 08: plotting using Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# For convienience, the output of Example 7 is already saved in a text file
x, y1, yerr1, y2, yerr2 = np.loadtxt('ex07_mmkk_mdkk.txt',unpack=True)

plt.errorbar(x,y1,yerr1,fmt='b',capsize=8)
plt.errorbar(x,y2,yerr2,fmt='r--',capsize=5)
plt.xlabel('λ, Arrival rate', fontsize = 14) # check Unicode support
plt.ylabel('Request blocking probability', fontsize = 14)
plt.show()
