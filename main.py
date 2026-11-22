import random
from copy import deepcopy

class state:
    def __init__(self, N = 20):
        self.N = N
        self.S = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
    
    def random(self):
        for i in range(self.N):
            for j in range(self.N):
                self.S[i + 1][j + 1] = 2*random.randint(0,1)-1

    def mutate(self, N = 1):
        for n in range(N):
            self.S[random.randint(1, self.N)][random.randint(1, self.N)] *= -1

    def energy(self):
        inner = 0
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                inner += self.S[i][j] * self.S[i][j+1]
                inner += self.S[i][j] * self.S[i][j-1]
                inner += self.S[i][j] * self.S[i+1][j]
                inner += self.S[i][j] * self.S[i-1][j]
        inner /= 2 # because each interaction was counted twice
        J = 1 # the interaction strength between spins
        inner *= -J

        outer = 0

        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                outer += self.S[i][j]
        
        B = 1
        outer *= - B

        return inner + outer

    def __repr__(self):
        str = f">\n"
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                str += "█" if self.S[i][j] == 1 else " "
            str += "\n"
        return str + "<"

s0 = state(30)
s0.random()
energyOverTime = []
minEnergy =  9999999
maxEnergy = -9999999
for i in range(5):
    for j in range(10):
        s = deepcopy(s0)
        s.mutate()
        
        energy = s0.energy()

        if s.energy() < energy:
            s0 = s

        
        energyOverTime.append(energy)
        if maxEnergy < energy:
            maxEnergy = energy
        elif minEnergy > energy:
            minEnergy = energy
    print(s0)

print(energyOverTime)
height = 20
width = len(energyOverTime)
dots = [round((b - minEnergy) / (maxEnergy - minEnergy)*height) for a, b in enumerate(energyOverTime)]
print(dots)
str = ""
for l in range(height):
    for c in range(width):
        if dots[c] == height - l:
            str += "█"
        else:
            str += " "
    str += "\n"

print(str)
