from display import display_plotext
from material import material

class experience:
    def __init__(self, N, B, T):
        self.material = material(N, B, T)
        self.material.set_all(spin = 1)
        self.energyOverTime = []

    def step(self, n):
        for i in range(n):
            self.material.mutate()
            self.energyOverTime.append(self.material.energy)

ex = experience(100, 0, 5)

for i in range(1000):
    ex.step(1000)
    display = display_plotext(width=None, height=12)
    display.plot_material(ex.material, marker="braille")

display = display_plotext(width=120, height=24)
display.plot_dashboard(ex.material, ex.energyOverTime)
