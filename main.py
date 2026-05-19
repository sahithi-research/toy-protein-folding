import matplotlib.pyplot as plt

from protein import Protein
from simulation import MonteCarloSimulation
from visualization import plot_protein


protein = Protein(length=15)

simulation = MonteCarloSimulation(protein)

plt.figure()

for step in range(300):

    simulation.step()

    if step % 5 == 0:
        plot_protein(protein)

plt.show()