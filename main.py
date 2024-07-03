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

class Rotor:
    def __init__(self, nom : str, permutations : list, encoches : list, position = 0):
        self.nom = nom
        self.permutations = permutations
        self.encoches = encoches
        self.position = position
    
    def tourner_rotor(self) -> bool:
        self.permutations.append(self.permutations.pop(0))
        tourner_suivant = False
        if self.position in self.encoches: #Si il faut tourner le deuxième rotor
            tourner_suivant = True
        self.position = (self.position + 1) % 26
        return tourner_suivant
    
    def permuter_lettre(self, lettre : str) -> str:
        return nombre_en_lettre(self.permutations[lettre_en_nombre(lettre)])
    
    def permuter_lettre_inverse(self, lettre : str) -> str:
        return nombre_en_lettre(self.permutations.index(lettre_en_nombre(lettre)))
    

class Enigma:
    def __init__(self, reflecteur : list):
        self.rotors = []
        self.reflecteur = reflecteur
        self.permutation = [i for i in range (26)]
    
    def choix_rotors(self, alignements_rotors : str):
        rotors = alignements_rotors.split("-")
        assert len(rotors) == 3
        for rotor in rotors:
            for i in range(len(liste_rotor)):
                if liste_rotor[i].nom == rotor:
                    self.rotors.append(liste_rotor[i])
        return self.rotors
    
    def changer_position_rotor(self, rotor, position):
        assert rotor in [0, 1, 2] # vérifier que le rotor est bien installé dans la machine
        self.rotors[rotor].position = position
        return
    
    def permuter_lettre(self, lettre):
        return nombre_en_lettre(self.permutation[lettre_en_nombre(lettre)])
    
    def ajouter_permutation(self, lettre_a, lettre_b):
        a = lettre_en_nombre(lettre_a)
        b = lettre_en_nombre(lettre_b)
        self.permutation[a] = b
        self.permutation[b] = a
        return


def lettre_en_nombre(lettre : str) -> int:
    assert "A" <= lettre <= "Z"
    return ord(lettre) - ord("A")

def nombre_en_lettre(nombre : int) -> str:
    assert 0 <= nombre <= 25
    return chr(nombre + ord("A"))

def traduire_lettre(enigma : Enigma, lettre : str) -> str:
    tourner = enigma.rotors[0].tourner_rotor()
    if tourner:
        tourner = enigma.rotors[1].tourner_rotor()
    if tourner:
        enigma.rotors[2].tourner_rotor()
    # La lettre pase dans les permutations
    lettre = enigma.permuter_lettre(lettre)
    print("Première permutation :", lettre)
    # La lettre permutée passe dans les rotors
    lettre = enigma.rotors[0].permuter_lettre(lettre)
    print("Premier rotor :", lettre)
    lettre = enigma.rotors[1].permuter_lettre(lettre)
    print("Deuxième rotor :", lettre)
    lettre = enigma.rotors[2].permuter_lettre(lettre)
    print("Troisième rotor :", lettre)
    # La lettre modifiée par les rotors passe dans le réflecteur
    lettre = nombre_en_lettre(enigma.reflecteur[lettre_en_nombre(lettre)])
    print("Réflecteur :", lettre)
    # La lettre passe dans les rotors à l'envers
    lettre = enigma.rotors[2].permuter_lettre_inverse(lettre)
    print("Troisième rotor inverse :", lettre)
    lettre = enigma.rotors[1].permuter_lettre_inverse(lettre)
    print("Deuxième rotor inverse :", lettre)
    lettre = enigma.rotors[0].permuter_lettre_inverse(lettre)
    print("Premier rotor inverse :", lettre)
    # La lettre repasse dans les permutations
    lettre = enigma.permuter_lettre(lettre)
    print("Dernière permutation :", lettre)
    return lettre
    
def initialiser_enigma(enigma : Enigma, rotors : str, positions : str, liste_permutations = []):
    liste_positions = positions.split("-")
    for permutation in liste_permutations:
        enigma.ajouter_permutation(permutation[0], permutation[1])
    enigma.choix_rotors(rotors)
    for i in range(3):
        enigma.changer_position_rotor(i, int(liste_positions[i]))
    return
    
    

enigma1 = Enigma(reflecteurB)
liste_rotor = [Rotor("I", rotorI, [16]), Rotor("II", rotorII, [4]), Rotor("III", rotorIII, [21]), Rotor("IV", rotorIV, [9]), Rotor("V", rotorV, [25]), Rotor("VI", rotorVI, [25, 12]), Rotor("VII", rotorVII, [25, 12]), Rotor("VIII", rotorVIII, [25, 12])]
rotors1 = input("Choisissez les rotors (I-VI-III) : ")
positions1 = input("Choisissez les positions des rotors (10-15-23) : ")
initialiser_enigma(enigma1, rotors1, positions1, ["AC", "BE"])
lettre1 = input("Entrez une lettre à chiffrer : ")
traduire_lettre(enigma1, lettre1)


