import random
from config import ATOM_TYPES
from atom import Atom


def distributuion(start: int = 0, end: int = 10, step: int = 1):
    atoms: list[Atom] = []

    keys = list(ATOM_TYPES.keys())
    weights = list(ATOM_TYPES.values())

    id = 1
    for z in range(start, end, step):
        for y in range(start, end, step):
            for x in range(start, end, step):

                type = random.choices(keys, weights=weights)[0]
                type_id = keys.index(type)
                
                atom = Atom(id=id, type_id=type_id, coords=(x, y, z))
                atoms.append(atom)
                id += 1

    return atoms