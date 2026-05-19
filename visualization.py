import matplotlib.pyplot as plt


def plot_protein(protein):
    positions = protein.positions

    x = positions[:, 0]
    y = positions[:, 1]

    plt.clf()

    plt.plot(x, y, marker="o")

    plt.title("Toy Protein Folding Simulation")

    plt.xlim(-10, 20)
    plt.ylim(-10, 20)

    plt.pause(0.1)