import numpy as np

class lattice:
    def __init__(self, N, J, B, T, S0):
        self.N = N
        self.J = J
        self.B = B
        self.T = T

        self.grid = np.ones((N, N)) * S0

        # TODO watch for values of S0

    def compute_energy(self):
        Energy = - self.J * np.sum(self.grid * (np.roll(self.grid, -1, axis=0) + np.roll(self.grid, -1, axis=1)))
        Energy += - self.B * np.sum(self.grid)
        return Energy

    def compute_magnetization(self):
        Magnetization = np.sum(self.grid)
        return Magnetization

s = lattice(5, 1,1,1, -1)

print(s.grid)