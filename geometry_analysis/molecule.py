"""
molecule.py
A python package for the MolSSI Software Summer School.
Contains a molecule class
"""

import numpy as np
from .measure import calculate_distance,calculate_angle
class Molecule:
    def __init__(self, name, symbols, coordinates):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name is not a string.")

        self.symbols = symbols
        self._coordinates = coordinates
        self.bonds = self.build_bond_list()

    @property
    def num_atoms(self):
        return len(self._coordinates)

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, new_coordinates):
        self._coordinates = new_coordinates
        self.bonds = self.build_bond_list()

    def build_bond_list(self, max_bond=2.93, min_bond=0):
        """
        Build a list of bonds based on a distance criteria.
        Atoms within a specified distance of one another will be considered bonded.
        Parameters
        ----------
        max_bond : float, optional
        min_bond : float, optional
        Returns
        -------
        bond_list : list
            List of bonded atoms. Returned as list of tuples where the values are the atom indices.
        """

        bonds = {}
        print ("In molecule")
        print (self._coordinates)

        for atom1 in range(self.num_atoms):
            for atom2 in range(atom1, self.num_atoms):
                distance = calculate_distance(self._coordinates[atom1], self._coordinates[atom2])
                print ([self._coordinates[atom1],self._coordinates[atom2],distance])

                if distance > min_bond and distance < max_bond:
                    bonds[(atom1, atom2)] = distance

        return bonds


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    import sys
    print (sys.version)
    name = 'water'
    symbols = ['H','O','H']
    coordinates = np.array([[2,0,0],[0,0,0],[-2,0,0]])
    water_molecule = Molecule(name, symbols, coordinates)
    new_coordinates = np.array([[5,0,0],[0,0,0],[-2,0,0]])
    water_molecule.coordinates = new_coordinates
    pass
