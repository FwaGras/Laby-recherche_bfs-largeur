class PileVide(Exception):
    """
    extraction à partir d'une pile vide
    """
    pass

class Pile:
    def __init__(self):
        self.memoire = []
        self.taille = 0
    def __repr__(self):
        mem =""
        for i in range(len(self.memoire)):
            mem += self.memoire[i] 
        return mem
    def estVide(self):
        return self.taille == 0
    def ajoute(self,x):
        self.memoire.append(x)
        self.taille += 1
        return None
    def extrait(self):
        if self.taille == 0:
            raise PileVide
        else:
            x = self.memoire.pop()
            self.taille -= 1
            return x

class FileVide(Exception):
    """
        extraction à partir d'une file vide
    """
    pass

class File:
    def __init__(self):
        self.pA = Pile()
        self.pB = Pile()
        self.taille = 0
    def estVide(self):
        return self.taille == 0
    def ajoute(self,x):
        self.pA.ajoute(x)
        self.taille += 1
        return None
    def extrait(self):
        if self.taille == 0:
            raise FileVide
        elif self.pB.estVide():
            while not self.pA.estVide():
                self.pB.ajoute(self.pA.extrait())
        x = self.pB.extrait() # ce n'est pas une erreur d'indentation !
        self.taille -= 1
        return x
