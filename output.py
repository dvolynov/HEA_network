import matplotlib.pyplot as plt
from config import ATOM_TYPES


def plot3d(atoms):
    atom_colors = list(ATOM_TYPES.values())
    x, y, z, colors = [], [], [], []

    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')

    for i, children in enumerate(atoms):
        for atom in children:

            if atom.parent is not None:

                ax.plot(
                    [atom.parent.coords.x, atom.coords.x], 
                    [atom.parent.coords.y, atom.coords.y], 
                    [atom.parent.coords.z, atom.coords.z], 
                    c=atom_colors[atom.parent.type_id]
                )

                x.append(atom.coords.x)
                y.append(atom.coords.y)
                z.append(atom.coords.z)
                
                colors.append(atom_colors[atom.type_id])


    ax.scatter3D(x, y, z, c=colors)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Atoms')

    plt.show()




def only_points(atoms):
    x, y, z, colors = [], [], [], []

    atom_colors = list(ATOM_TYPES.values())

    for atom in atoms:
        x.append(atom.coords.x)
        y.append(atom.coords.y)
        z.append(atom.coords.z)
        colors.append(atom_colors[atom.type_id])

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.scatter3D(x, y, z, c=colors)

    ax.set_title('Plot')

    plt.show()