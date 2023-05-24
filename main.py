from initializer import distributuion
from traversal import traversal
from output import plot3d



def main():

    atoms = distributuion(end = 1000, step = 200)

    array = []
    for children in traversal(atoms, start=67):
        array.append(children)
    
    plot3d(array)


if __name__ == "__main__":
    main()