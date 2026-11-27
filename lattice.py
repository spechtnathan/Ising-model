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
        self.energy = 0

        # TODO watch for values of S0
        if S0 not in [-1,0,1]:
            pass

        self.grid = np.ones((N + 2, N + 2)) * S0
        # Defined border conditions, no interaction between opposite sides
        self.grid[0, :] = 0
        self.grid[-1, :] = 0
        self.grid[:, 0] = 0
        self.grid[:, -1] = 0

        self.compute_energy()


    def compute_energy(self):
        """
        Compute the energy of the lattice
        """
        
        # Interaction energy
        # Sum of products of nearest neighbors (np.roll shifts the grid)
        Energy = - self.J * np.sum(self.grid * (np.roll(self.grid, -1, axis=0) + np.roll(self.grid, -1, axis=1)))
        # Magnetic field energy
        Energy += - self.B * np.sum(self.grid)
        # Cache the total energy
        self.energy = Energy
        return Energy

    def compute_magnetization(self):
        """
        Compute the magnetization of the lattice
        """
        # Sum of all spins
        Magnetization = np.sum(self.grid)
        return Magnetization

    rng = np.random.default_rng()

    def step(self):
        # change one random spin
        row = self.rng.integers(1, self.N + 1)
        column = self.rng.integers(1, self.N + 1)
        self.grid[row][column] *= -1 

        # Compute Energy difference
        # dE = - 2 * J * (s1 + s2 + s3 + s4) - 2 * B * s0 with s0 the spin changed and s1 to s4 neirest neighbors
        # Times 2 to cancel previous energy
        #    1               |     1                |
        #  1 1 1 E = 4J + 5B |  1 -1 1 E = -4J + 3B | dE = -8J -2B 
        #    1               |     1                |
        dE = - self.J * 2 * (self.grid[row-1][column] + self.grid[row+1][column] + self.grid[row][column-1] + self.grid[row][column+1]) * self.grid[row][column]
        dE -= self.B * self.grid[row][column] * 2

        # accept or reject regarding the energy change
        if dE < 0 or self.rng.random() < np.exp(-dE / self.T):
            self.energy += dE
        else:
            self.grid[row][column] *= -1 # change back the spin if rejected