from modules.initializer import Initializer
from modules.transition_matrix import TransitionMatrix
from modules.config import Config

import numpy as np


def main():
    all_elements = np.load('all_elements.npy')

    config = Config("Al2Fe3Mn5")

    initializer = Initializer(config)

    atoms = initializer.distribute(end=1000, step=200)

    matrix = TransitionMatrix(atoms, config).data
    print(matrix)


if __name__ == "__main__":
    main()