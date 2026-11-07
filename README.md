# Ising-model

**Background**

The Ising model simulates ferromagnetic properties in a material. It is a simple approach used to study certain macroscopic properties of the material, notably its phase transition.

The model consists of a lattice (a grid) where each site is occupied by a magnetic dipole (a spin) that can be in one of two states: $+1$ or $-1$. The dynamics of the system tend to minimize the energy:

$$E = -J \sum_{\langle i,j \rangle} s_i s_j - B \sum_i s_i$$

where $J$ is the interaction strength between spins, $s_i$ is the spin at site $i$, $\sum_{\langle i,j \rangle}$ denotes the sum over nearest neighbors, and $B$ is the interaction strength with an external magnetic field. Conversely, temperature tends to increase chaos.

**Project Objectives**

The objective of this project is to simulate a spin lattice whose evolution is governed by the Ising model. This implementation will be carried out using the Metropolis algorithm.

This simulation will then be used to study the evolution of certain macroscopic properties (magnetization, total energy, etc.) as a function of external parameters. You should observe the signatures of a phase transition.

**Instructions — Tools**

The Metropolis algorithm works as follows:

1. **Initialization:** Generate an initial configuration $S_0 = (s_1, \dots, s_N)$, for example by choosing spins randomly or aligning all spins in the same direction.


2. **Modify a spin:** Randomly select a spin and flip it to generate a new configuration $S_1$.


3. **Accept or Reject:** Evaluate the total energy change $\Delta E = E_1 - E_0$ between $S_1$ and $S_0$. If energy decreases, accept the change; if it increases, accept it with probability $w = e^{-\Delta E/T}$ (at temperature $T$), or revert.


4. **Repeat:** Repeat the previous steps until attempting to modify a set percentage of the lattice (a high percentage makes the code much more costly) to obtain the state at time $t+1$.


5. **Time evolution:** Model the time evolution of the lattice.



**Guidelines**

Implement the Metropolis algorithm and test your simulation for different initial configurations and different parameters ($B = 0$ or strong $B$; weak $J$ or strong $J$, etc.). Plot the evolution of the energy and the magnetization ($M = \sum_i s_i$) over time.

To explore your simulation:

* You should observe the emergence of structure when the temperature drops below a certain value (critical temperature), accompanied by an abrupt change in the behavior of total energy and magnetization.


* Starting from a state where all spins are aligned (the energy-minimizing state), you can observe that it is necessary to pass through a temperature above the critical value to change the state of the lattice.



Particular attention must be paid to the graphical representation of your results.
