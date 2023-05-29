import numpy as np
from scipy.spatial.qhull import Delaunay


class TransitionMatrix:

    def __init__(self, atoms: list):
        self.atoms = atoms
        self.data = self.compute_transition_matrix()
        
    def compute_transition_matrix(self) -> np.array:
        points = np.array([atom.coords() for atom in self.atoms])
        tri = Delaunay(points)

        types = [atom.type_id for atom in self.atoms]
        unique_types = list(set(types))
        n_types = len(unique_types)
        transition_matrix = np.zeros((n_types, n_types))
        for simplex in tri.simplices:
            simplex_types = [types[i] for i in simplex]
            for i in range(len(simplex_types) - 1):
                current_type = simplex_types[i]
                next_type = simplex_types[i + 1]
                current_index = unique_types.index(current_type)
                next_index = unique_types.index(next_type)
                transition_matrix[current_index, next_index] += 1
        transition_matrix /= np.sum(transition_matrix, axis=1, keepdims=True)

        return transition_matrix