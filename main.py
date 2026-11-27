import numpy as np
import matplotlib.pyplot as plt
from simulation import *


s = simulation(N=200, J=1, B=1, T=73, S0=-1)
s.step(50000)

plt.plot(np.arange(len(s.energyOverTime)), s.energyOverTime)
plt.show()