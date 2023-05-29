import random
from modules.atom import Atom


class Initializer:

    def __init__(self, df):
        self.df = df

    def distribute(self, start: int = 0, end: int = 10, step: int = 1):
        """
        Distribution params
        start - an integer number specifying at which position to start. Default is 0.
        stop - an integer number specifying at which position to stop (not included). Default is 10.
        step - an integer number specifying the incrementation. Default is 1.
        """

        atoms: list[Atom] = []

        names = list(self.df['Name'].values)
        weights = list(self.df['Weight'].values)

        id = 1
        for z in range(start, end, step):
            for y in range(start, end, step):
                for x in range(start, end, step):

                    type = random.choices(names, weights=weights)[0]
                    type_id = names.index(type)
                    
                    atom = Atom(id=id, type_id=type_id, coords=(x, y, z))
                    atoms.append(atom)
                    id += 1

        return atoms