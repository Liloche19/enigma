rotorI = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
rotorII = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 12, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
rotorIII = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
rotorIV = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]
rotorV = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
rotorVI = [9, 15, 6, 21, 14, 20, 12, 5, 24, 16, 1, 4, 13, 7, 25, 17, 3, 10, 0, 18, 23, 11, 8, 2, 19, 22]
rotorVII = [13, 25, 9, 7, 6, 17, 2, 23, 12, 24, 18, 22, 1, 14, 20, 5, 0, 8, 21, 11, 15, 4, 10, 16, 3, 19]
rotorVIII = [5, 10, 16, 7, 19, 11, 23, 14, 2, 1, 9, 18, 15, 3, 25, 17, 0, 12, 4, 22, 13, 8, 20, 24, 6, 21]

reflecteurB = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
reflecteurC = [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]

class Enigma:
    def __init__(self):
        self.rotors = []
        self.position_rotors = []
        self.permutation = [i for i in range (26)]
    
    def rotors(self, alignements_rotors):
        self.rotors.clear()
        for rotor in alignements_rotors:
            self.rotors.append(rotor)
    
    def changer_position_rotor(self, rotor, position):
        assert rotor in [0, 1, 2] # vérifier que le rotor est bien installé dans la machine
        self.position_rotors[rotor] = position
    
    def permuter_lettre(self, lettre):
        return nombre_en_lettre(self.permutation[lettre_en_nombre(lettre)])
    
    def ajouter_permutation(self, lettre_a, lettre_b):
        a = lettre_en_nombre(lettre_a)
        b = lettre_en_nombre(lettre_b)
        self.permutation[a] = b
        self.permutation[b] = a
        return


def lettre_en_nombre(lettre):
    assert "A" <= lettre <= "Z"
    return ord(lettre) - ord("A")

def nombre_en_lettre(nombre):
    assert 0 <= nombre <= 25
    return chr(nombre + ord("A"))

def donner_liste(string):
    lst = []
    for e in string:
        lst.append(lettre_en_nombre(e))
    return lst

enigma = Enigma()
enigma.ajouter_permutation("A", "C")