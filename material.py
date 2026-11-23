import random
from math import exp

class material:
    def __init__(self, N = 20, J = 1, B = 1, T = 1):
        self.N = N
        self.S = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
        self.J = J
        self.B = B
        self.T = T
        self.__spin_sum = 0
        self.__energy = self._compute_energy()
    
    def random(self):
        spin_sum = 0
        for i in range(self.N):
            for j in range(self.N):
                s = 2 * random.randint(0, 1) - 1
                self.S[i + 1][j + 1] = s
                spin_sum += s
        self.__spin_sum = spin_sum
        self.__energy = self._compute_energy()

    def set_all(self, spin = 1):
        for i in range(self.N):
            for j in range(self.N):
                self.S[i + 1][j + 1] = spin
        self.__spin_sum = spin * self.N * self.N
        self.__energy = self._compute_energy()

    def mutate(self, N = 1):
        for n in range(N):
            pos = (random.randint(1, self.N), random.randint(1, self.N))
            self.S[pos[0]][pos[1]] *= -1
            dE = - self.J * 2 * (self.S[pos[0]-1][pos[1]] + self.S[pos[0]+1][pos[1]] + self.S[pos[0]][pos[1]-1] + self.S[pos[0]][pos[1]+1]) * self.S[pos[0]][pos[1]]
            dE -= self.B * self.S[pos[0]][pos[1]] * 2

            if dE < 0 or (self.T > 0 and random.random() < exp(-dE / self.T)):
                self.__energy += dE # Accept the spin change
                self.__spin_sum += 2 * self.S[pos[0]][pos[1]]
            else:
                self.S[pos[0]][pos[1]] *= -1 # Reject the spin change

    @property
    def energy(self):
        return self.__energy

    @property
    def magnetization(self):
        return self.__spin_sum / (self.N * self.N)

    def _compute_energy(self):
        inner = 0
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                inner += self.S[i][j] * self.S[i][j+1]
                inner += self.S[i][j] * self.S[i][j-1]
                inner += self.S[i][j] * self.S[i+1][j]
                inner += self.S[i][j] * self.S[i-1][j]
        inner /= 2 # because each interaction was counted twice
        inner *= - self.J

        outer = 0

        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                outer += self.S[i][j]
        
        outer *= - self.B

        self.__energy = inner + outer
        return self.__energy


    def __repr__(self):
        graph = f">\n"
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                graph += "█" if self.S[i][j] == 1 else " "
            graph += "\n"
        return graph + "<"