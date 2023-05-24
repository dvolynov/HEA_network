import random
from config import ATOM_TYPES
from atom import Atom


def distributuion(start: int = 0, end: int = 10, step: int = 1):
    atoms: list[Atom] = []

    types_len = len(ATOM_TYPES) - 1

    id = 1
    for z in range(start, end, step):
        for y in range(start, end, step):
            for x in range(start, end, step):

                type_id = random.randint(0, types_len)
                
                atom = Atom(id=id, type_id=type_id, coords=(x, y, z))
                atoms.append(atom)
                id += 1

    return atoms