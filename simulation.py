import numpy as np


class MonteCarloSimulation:
    def __init__(self, protein, temperature=1.0):
        self.protein = protein
        self.temperature = temperature

    def step(self):
        old_energy = self.protein.calculate_energy()

        index, old_position = self.protein.random_move()

        new_energy = self.protein.calculate_energy()

        delta_energy = new_energy - old_energy

        if delta_energy < 0:
            return True

        probability = np.exp(-delta_energy / self.temperature)

        if np.random.rand() < probability:
            return True

        self.protein.restore_position(index, old_position)

        return False