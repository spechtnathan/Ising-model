import plotext as plt

class display_plotext:
    def __init__(self, width=100, height=20, theme="clear"):
        self.width = width
        self.height = height
        self.theme = theme

    def _apply_base_style(self):
        plt.clf()
        if self.theme:
            plt.theme(self.theme)
        if self.width and self.height:
            plt.plotsize(self.width, self.height)

    def plot_energy(self, energy_over_time, title="Energy over time", marker="braille"):
        self._apply_base_style()
        plt.plot(energy_over_time, marker=marker)
        plt.title(title)
        plt.xlabel("Step")
        plt.ylabel("Energy")
        plt.show()

    def plot_magnetization(self, magnetization_over_time, title="Magnetization over time", marker="braille"):
        self._apply_base_style()
        plt.plot(magnetization_over_time, marker=marker)
        plt.title(title)
        plt.xlabel("Step")
        plt.ylabel("Magnetization")
        plt.show()

    def _plot_lattice(self, mat, title, marker):
        xs, ys = [], []
        for r in range(1, mat.N + 1):
            row = mat.S[r]
            y = mat.N - r
            for c in range(1, mat.N + 1):
                if row[c] == 1:
                    xs.append(c - 1)
                    ys.append(y)
        if xs:
            plt.scatter(xs, ys, marker=marker)
        plt.title(title)
        plt.xlim(0, mat.N - 1)
        plt.ylim(0, mat.N - 1)
        plt.xticks([])
        plt.yticks([])

    def plot_material(self, mat, title="Ising lattice", marker="fhd"):
        self._apply_base_style()
        self._plot_lattice(mat, title, marker)
        plt.show()

    def plot_dashboard(self, mat, energy_over_time, marker="braille", lattice_marker="fhd"):
        plt.clf()
        if self.theme:
            plt.theme(self.theme)
        if self.width and self.height:
            plt.plotsize(self.width, self.height)

        plt.subplots(1, 2)

        plt.subplot(1, 1)
        self._plot_lattice(mat, f"Ising lattice (T={mat.T}, J={mat.J}, B={mat.B})", lattice_marker)

        plt.subplot(1, 2)
        plt.plot(energy_over_time, marker=marker)
        plt.title("Energy over time")
        plt.xlabel("Step")
        plt.ylabel("Energy")

        plt.show()