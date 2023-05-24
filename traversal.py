import queue
import numpy as np
import copy
import math


def distance(A, B):
    dx = A.coords.x - B.coords.x
    dy = A.coords.y - B.coords.y
    dz = A.coords.z - B.coords.z
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


def traversal(atoms_origin: list, start: int, n_len: int = 26):
    atoms = copy.deepcopy(atoms_origin)

    parent = atoms[start]
    parent.parent = parent

    q = queue.PriorityQueue()
    q.put((1, 0, parent))  # (self order, child order, parent)

    i = 1
    while not q.empty():
        _, _, parent = q.get()
        
        distances, neighbours = [], []

        for neighbour in atoms:
            if neighbour is not parent:
                d = distance(parent, neighbour)
                distances.append(d)
                neighbours.append(neighbour)
        
        distances = np.array(distances)
        neighbours = np.array(neighbours)

        sorted_indices = np.argsort(distances)
        children = neighbours[sorted_indices][:n_len]

        j = 1
        for child in children:
            if child.parent is None:
                child.parent = parent
                q.put((i, j, child))
                j += 1
            else:
                children = np.delete(children, np.where(children == child))
        i += 1

        yield children