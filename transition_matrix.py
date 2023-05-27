import numpy as np
from scipy.spatial.qhull import Delaunay


def trans_matrix(atoms_origin):
    # Compute the Delaunay triangulation
    points = np.array([(atom.coords.x, atom.coords.y, atom.coords.z) for atom in atoms_origin])
    tri = Delaunay(points)

    # Build the Markov chain
    types = [atom.type_id for atom in atoms_origin]
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
