import random
from modules.atom import Atom


class Initializer:

    def __init__(self, config: object):
        self.elements = config.elements
        self.weights = config.weights 

    def distribute(self, start: int = 0, end: int = 10, step: int = 1):
        """
        Distribution params
        start - an integer number specifying at which position to start. Default is 0.
        stop - an integer number specifying at which position to stop (not included). Default is 10.
        step - an integer number specifying the incrementation. Default is 1.
        """

        atoms: list[Atom] = []

        id = 1
        for z in range(start, end, step):
            for y in range(start, end, step):
                for x in range(start, end, step):

                    type = random.choices(self.elements, weights=self.weights)[0]
                    type_id = self.elements.index(type)
                    
                    atom = Atom(id=id, type_id=type_id, coords=(x, y, z))
                    atoms.append(atom)
                    id += 1

        return atoms