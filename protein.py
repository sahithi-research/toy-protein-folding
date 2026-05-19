import numpy as np


class Protein:
    def __init__(self, length=15):
        self.length = length

        self.positions = np.array(
            [[i, 0] for i in range(length)],
            dtype=float
        )

    def calculate_energy(self):
        energy = 0

        for i in range(self.length):
            for j in range(i + 2, self.length):

                distance = np.linalg.norm(
                    self.positions[i] - self.positions[j]
                )

                if distance < 2:
                    energy += 1 / distance

        return energy

    def random_move(self):
        index = np.random.randint(1, self.length - 1)

        move = np.random.uniform(-1, 1, size=2)

        old_position = self.positions[index].copy()

        self.positions[index] += move

        return index, old_position

    def restore_position(self, index, old_position):
        self.positions[index] = old_position