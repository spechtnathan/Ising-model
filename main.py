import numpy as np
from random import random

# Spin lattice of a material
class lattice:
    # N : The number of electrons on the side of the square lattice
    # J : The interaction strength between two spin neighbors
    # B : The magnetic field encompassing the material
    # T : The temperture of the material
    # S0: The initial state of the material, -1: Down, 0: Random, 1: Up
    def __init__(self, N, J, B, T, S0):
        self.N = N
        self.J = J
        self.B = B
        self.T = T

        # TODO watch for values of S0
        if S0 not in [-1,0,1]:
            pass

        self.grid = np.ones((N, N)) * S0


    def compute_energy(self):
        """
        Compute the energy of the lattice
        """

        # TODO no interaction between opposite sides

        Energy = - self.J * np.sum(self.grid * (np.roll(self.grid, -1, axis=0) + np.roll(self.grid, -1, axis=1)))
        Energy += - self.B * np.sum(self.grid)
        return Energy

    def compute_magnetization(self):
        """
        Compute the magnetization of the lattice
        """
        Magnetization = np.sum(self.grid)
        return Magnetization

    def step(self):
        # change one random spin
        pos = (random.randint(0, self.N - 1), random.randint(0, self.N - 1))

        # Compute Energy difference
        # dE = - 2 * J * (s1 + s2 + s3 + s4) - 2 * B * s0 with s0 the spin changed and s1 to s4 neirest neighbors
        # Times 2 to cancel previous energy
        #    1                     1
        #  1 1 1 E = 4J + 5B   1 -1 1 E = -4J + 3B ; dE = -8J -2B 
        #    1                     1
        dE = - self.J * 2 * (self.grid[pos[0]-1][pos[1]] + self.grid[pos[0]+1][pos[1]] + self.S[pos[0]][pos[1]-1] + self.S[pos[0]][pos[1]+1]) * self.S[pos[0]][pos[1]]
        dE -= self.B * self.S[pos[0]][pos[1]] * 2

        # accept or reject regarding the energy change
        self.grid[pos[0]][pos[1]] *= -1

        pass


class simulation(lattice):
    def __init__(self, N, J, B, T, S0):
        super().__init__(N, J, B, T, S0)

    def step(n):
        for i in range(n):
            super().step()


s = simulation(5, 1, 1, 1, -1)
s.step(5000)
print(s.grid)