from modules.initializer import Initializer
from modules.transition_matrix import TransitionMatrix

import pandas as pd



def main():
    config_df = pd.read_csv('config.csv', delimiter=";")

    initializer = Initializer(config_df)
    atoms = initializer.distribute(end=1000, step=200)

    matrix = TransitionMatrix(atoms).data
    print(matrix)


if __name__ == "__main__":
    main()