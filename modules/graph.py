import queue
import numpy as np
import math


class Graph:
    
    def __init__(self, atoms: list):
        self.atoms = atoms

    def get_distance(self, A, B) -> float:
        dx = A.coords.x - B.coords.x
        dy = A.coords.y - B.coords.y
        dz = A.coords.z - B.coords.z
        return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


    def traversal(self, start: int, n_len: int = 26) -> list:
        """
        Traversal params
        start - an integer number specifying at which position to start.
        n_len - an integer number specifying amount of neighbours. Default is 26.
        """
         
        parent = self.atoms[start]
        parent.parent = parent

        q = queue.PriorityQueue()
        q.put((1, 0, parent))

        i = 1
        while not q.empty():
            _, _, parent = q.get()
            
            distances, neighbours = [], []

            for neighbour in self.atoms:
                if neighbour is not parent:
                    d = self.get_distance(parent, neighbour)
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