import numpy as np

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
        Energy = - self.J * np.sum(self.grid * (np.roll(self.grid, -1, axis=0) + np.roll(self.grid, -1, axis=1)))
        Energy += - self.B * np.sum(self.grid)
        return Energy

    def compute_magnetization(self):
        """
        Compute the magnetization of the lattice
        """
        Magnetization = np.sum(self.grid)
        return Magnetization

    rng = np.random.default_rng()

    def step(self):
        # change one random spin
        row = self.rng.integers(0, self.N)
        column = self.rng.integers(0, self.N)
        self.grid[row][column] *= -1 

        # accept or reject regarding the energy change
        pass


class simulation(lattice):
    def __init__(self, N, J, B, T, S0):
        super().__init__(N, J, B, T, S0)

    def step(self, n):
        for i in range(n):
            super().step()


s = simulation(4, 1, 1, 1, -1)
print(s.grid)
s.step(1)
print(s.grid)