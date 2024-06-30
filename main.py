class Rotor:
    def __init__(self, nom):
        self.nom = nom

class Enigma:
    def __init__(self):
        self.rotors = []
        self.position_rotors = []
    
    def rotors(self, alignements_rotors):
        self.rotors.clear()
        for rotor in alignements_rotors:
            self.rotors.append(rotor)
    
    def changer_position_rotor(self, rotor, position):
        assert rotor in [0, 1, 2] # vérifier que le rotor est bien installé dans la machine
        self.position_rotors[rotor] = position

def lettre_en_nombre(lettre):
    assert "A" <= lettre <= "Z"
    return ord(lettre) - ord("A")

def nombre_en_lettre(nombre):
    assert 0 <= nombre <= 25
    return chr(nombre + ord("A"))