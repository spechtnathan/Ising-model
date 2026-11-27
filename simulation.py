from lattice import *

class simulation:
    def __init__(self, N, J, B, T, S0):
        self.lattice = lattice(N, J, B, T, S0)
        self.energyOverTime = [self.lattice.energy]

    def step(self, n):
        for i in range(n):
            self.lattice.step()
            self.energyOverTime.append(self.lattice.energy)