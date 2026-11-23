from display import display_plotext
from material import material

class experience:
    def __init__(self, N, J, B, T):
        self.material = material(N, J, B, T)
        self.material.set_all(spin = 1)
        self.energyOverTime = []
        self.magnetizationOverTime = []

    def step(self, n):
        for i in range(n):
            self.material.mutate()
            self.energyOverTime.append(self.material.energy)
            self.magnetizationOverTime.append(self.material.magnetization)

#ex = experience(100, -3, 0)
#
#for i in range(1000):
#    ex.step(1000)
#    display = display_plotext(width=None, height=12)
#    display.plot_material(ex.material, marker="braille")
#
#display = display_plotext(width=120, height=24)
#display.plot_dashboard(ex.material, ex.energyOverTime)

J = int(input("J : "))
B = int(input("B : "))
T = int(input("T : "))

ex = experience(100, J, B, T)

display = display_plotext(width=120, height=24)

for i in range(10):
    ex.step(10000)
    display = display_plotext(width=None, height=12)
    display.plot_material(ex.material, marker="braille")

display.plot_energy(ex.energyOverTime)
display.plot_magnetization(ex.magnetizationOverTime)