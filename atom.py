class Coords:

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


class Atom:

    def __init__(self, id: int, type_id: int, coords: tuple[int], parent: int = None):
        self.id      = id
        self.type_id = type_id
        self.coords  = Coords(*coords)
        self.parent  = parent