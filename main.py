from copy import deepcopy
from material import material

s0 = material(40)
s0.random()
energyOverTime = []
minEnergy =  9999999
maxEnergy = -9999999
for i in range(4):
    for j in range(1000):
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


height = 20
width = 100
dots = [(round(a / len(energyOverTime) * width), round((b - minEnergy) / (maxEnergy - minEnergy)*height)) for a, b in enumerate(energyOverTime)]

graph = str(maxEnergy) + "\n"
for l in range(height):
    for c in range(width):
        f = False
        for i in range(len(dots)):
            if dots[i] == (c, height - l):
                graph += "█"
                f = True
                break
        if not f:
            graph += " "
    graph += "\n"

xLabel = str(minEnergy) + "/0"
xLabel += " " * (width - len(xLabel) - len(str(len(energyOverTime)))) + str(len(energyOverTime))
graph += xLabel
print(graph)
