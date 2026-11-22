from math import log, sqrt
import plotext as plt
from material import material


def test_recovery(T, N=20, heat_sweeps=80, cool_sweeps=40, T_cool=0.5, trials=3):
    """
    Start fully magnetized (+1), heat at temperature T, then cool back to T_cool.
    Returns (avg_magnetization_at_T, avg_recovered_magnetization).
    """
    steps_per_sweep = N * N
    m_hot_total = 0.0
    m_rec_total = 0.0

    for _ in range(trials):
        mat = material(N=N, B=0, T=T)
        mat.set_all(spin=1)

        # Heat phase: equilibrate at T
        mat.mutate(heat_sweeps * steps_per_sweep)
        m_hot_total += mat.magnetization

        # Cool phase: see if the material recovers its +1 orientation
        mat.T = T_cool
        mat.mutate(cool_sweeps * steps_per_sweep)
        m_rec_total += mat.magnetization

    return m_hot_total / trials, m_rec_total / trials


def find_max_recovery_temp(
    t_min=1.0,
    t_max=3.4,
    t_step=0.15,
    N=20,
    recovery_threshold=0.5,
):
    temps = []
    m_hot_list = []
    m_rec_list = []

    print(f"{'T':>6} | {'M (at T)':>10} | {'M (cooled)':>10} | Status")
    print("-" * 44)

    t = t_min
    max_recoverable_t = None
    while t <= t_max + 1e-9:
        m_hot, m_rec = test_recovery(t, N=N)
        recovered = m_rec >= recovery_threshold
        if recovered:
            max_recoverable_t = t

        temps.append(round(t, 3))
        m_hot_list.append(m_hot)
        m_rec_list.append(m_rec)

        status = "RECOVERED" if recovered else "LOST"
        print(f"{t:6.2f} | {m_hot:10.3f} | {m_rec:10.3f} | {status}")
        t += t_step

    tc_theory = 2.0 / log(1.0 + sqrt(2.0))
    print("-" * 44)
    print(f"Estimated max recovery temperature : {max_recoverable_t:.2f}" if max_recoverable_t else "No temperature recovered.")
    print(f"Theoretical 2D Ising Curie temp Tc : {tc_theory:.3f}")

    # Plot results in terminal
    plt.clf()
    plt.theme("clear")
    plt.plotsize(100, 20)
    plt.plot(temps, m_hot_list, label="M at T", marker="braille")
    plt.plot(temps, m_rec_list, label="M after cooling", marker="braille")
    plt.vline(tc_theory, color="red")
    plt.title(f"Magnetization & Recovery vs Temperature (N={N}, B=0)")
    plt.xlabel("Temperature T")
    plt.ylabel("Magnetization M")
    plt.ylim(-0.2, 1.1)
    plt.show()


if __name__ == "__main__":
    find_max_recovery_temp()
